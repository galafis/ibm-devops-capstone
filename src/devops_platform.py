#!/usr/bin/env python3
"""
IBM DevOps and Software Engineering Professional Certificate Capstone Project
Enterprise DevOps Automation & Software Engineering Platform

This comprehensive DevOps platform demonstrates competencies from the
IBM DevOps and Software Engineering Professional Certificate including:
- Agile development methodologies
- Version control and collaboration
- Continuous integration/continuous deployment
- Infrastructure as code
- Monitoring and observability
- Security and compliance automation
"""

import os
import sys
import json
import logging
import subprocess
import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Any
from flask import Flask, request, jsonify
import yaml

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AgileProjectManager:
    """Agile project management and tracking"""
    
    def __init__(self, db_path='devops_platform.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize project management database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sprints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sprint_name TEXT NOT NULL,
                start_date DATE NOT NULL,
                end_date DATE NOT NULL,
                status TEXT DEFAULT 'planning',
                velocity INTEGER DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_stories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sprint_id INTEGER,
                title TEXT NOT NULL,
                description TEXT,
                story_points INTEGER DEFAULT 1,
                priority TEXT DEFAULT 'medium',
                status TEXT DEFAULT 'backlog',
                assigned_to TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (sprint_id) REFERENCES sprints (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS deployments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_name TEXT NOT NULL,
                version TEXT NOT NULL,
                environment TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                deployed_at DATETIME,
                rollback_version TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
        logger.info("DevOps platform database initialized")
    
    def create_sprint(self, sprint_name: str, duration_weeks: int = 2):
        """Create a new sprint"""
        start_date = datetime.now().date()
        end_date = start_date + timedelta(weeks=duration_weeks)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO sprints (sprint_name, start_date, end_date)
            VALUES (?, ?, ?)
        ''', (sprint_name, start_date, end_date))
        
        sprint_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        logger.info(f"Sprint created: {sprint_name} (ID: {sprint_id})")
        return sprint_id
    
    def add_user_story(self, sprint_id: int, title: str, description: str, 
                      story_points: int = 1, priority: str = 'medium'):
        """Add user story to sprint"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO user_stories 
            (sprint_id, title, description, story_points, priority)
            VALUES (?, ?, ?, ?, ?)
        ''', (sprint_id, title, description, story_points, priority))
        
        story_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        logger.info(f"User story added: {title} (ID: {story_id})")
        return story_id
    
    def get_sprint_metrics(self, sprint_id: int):
        """Get sprint metrics and burndown data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get sprint info
        cursor.execute('SELECT * FROM sprints WHERE id = ?', (sprint_id,))
        sprint = cursor.fetchone()
        
        # Get user stories
        cursor.execute('''
            SELECT status, COUNT(*), SUM(story_points)
            FROM user_stories WHERE sprint_id = ?
            GROUP BY status
        ''', (sprint_id,))
        
        story_metrics = {}
        for row in cursor.fetchall():
            story_metrics[row[0]] = {'count': row[1], 'points': row[2] or 0}
        
        conn.close()
        
        total_points = sum(metrics['points'] for metrics in story_metrics.values())
        completed_points = story_metrics.get('done', {}).get('points', 0)
        
        return {
            'sprint_info': sprint,
            'story_metrics': story_metrics,
            'total_points': total_points,
            'completed_points': completed_points,
            'completion_rate': (completed_points / total_points * 100) if total_points > 0 else 0
        }

class CICDPipelineEngine:
    """CI/CD pipeline automation engine"""
    
    def __init__(self):
        self.pipelines = {}
        self.builds = {}
    
    def create_jenkins_pipeline(self, app_name: str, git_repo: str):
        """Create Jenkins pipeline configuration"""
        jenkinsfile = f"""
pipeline {{
    agent any
    
    environment {{
        APP_NAME = '{app_name}'
        DOCKER_REGISTRY = 'your-registry.com'
        KUBECONFIG = credentials('kubeconfig')
    }}
    
    stages {{
        stage('Checkout') {{
            steps {{
                git branch: 'main', url: '{git_repo}'
            }}
        }}
        
        stage('Test') {{
            steps {{
                script {{
                    sh 'python -m pytest tests/ --junitxml=test-results.xml'
                    sh 'coverage run -m pytest tests/'
                    sh 'coverage xml'
                }}
            }}
            post {{
                always {{
                    junit 'test-results.xml'
                    publishCoverage adapters: [coberturaAdapter('coverage.xml')], sourceFileResolver: sourceFiles('STORE_LAST_BUILD')
                }}
            }}
        }}
        
        stage('Security Scan') {{
            steps {{
                script {{
                    sh 'bandit -r . -f json -o bandit-report.json || true'
                    sh 'safety check --json --output safety-report.json || true'
                }}
            }}
        }}
        
        stage('Build') {{
            steps {{
                script {{
                    def image = docker.build("${{DOCKER_REGISTRY}}/${{APP_NAME}}:${{BUILD_NUMBER}}")
                    docker.withRegistry('https://' + DOCKER_REGISTRY, 'docker-registry-credentials') {{
                        image.push()
                        image.push('latest')
                    }}
                }}
            }}
        }}
        
        stage('Deploy to Staging') {{
            steps {{
                script {{
                    sh '''
                        kubectl set image deployment/${{APP_NAME}} ${{APP_NAME}}=${{DOCKER_REGISTRY}}/${{APP_NAME}}:${{BUILD_NUMBER}} -n staging
                        kubectl rollout status deployment/${{APP_NAME}} -n staging
                    '''
                }}
            }}
        }}
        
        stage('Integration Tests') {{
            steps {{
                script {{
                    sh 'python -m pytest integration_tests/ --junitxml=integration-results.xml'
                }}
            }}
        }}
        
        stage('Deploy to Production') {{
            when {{
                branch 'main'
            }}
            steps {{
                input message: 'Deploy to production?', ok: 'Deploy'
                script {{
                    sh '''
                        kubectl set image deployment/${{APP_NAME}} ${{APP_NAME}}=${{DOCKER_REGISTRY}}/${{APP_NAME}}:${{BUILD_NUMBER}} -n production
                        kubectl rollout status deployment/${{APP_NAME}} -n production
                    '''
                }}
            }}
        }}
    }}
    
    post {{
        always {{
            cleanWs()
        }}
        success {{
            slackSend channel: '#deployments', 
                     color: 'good', 
                     message: "✅ ${{APP_NAME}} build ${{BUILD_NUMBER}} deployed successfully"
        }}
        failure {{
            slackSend channel: '#deployments', 
                     color: 'danger', 
                     message: "❌ ${{APP_NAME}} build ${{BUILD_NUMBER}} failed"
        }}
    }}
}}
"""
        
        self.pipelines[app_name] = {
            'jenkinsfile': jenkinsfile,
            'git_repo': git_repo,
            'status': 'configured',
            'created_at': datetime.now().isoformat()
        }
        
        return jenkinsfile
    
    def create_gitlab_ci_config(self, app_name: str):
        """Create GitLab CI/CD configuration"""
        gitlab_ci = f"""
stages:
  - test
  - security
  - build
  - deploy-staging
  - integration-test
  - deploy-production

variables:
  APP_NAME: {app_name}
  DOCKER_REGISTRY: $CI_REGISTRY
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE
  KUBECONFIG: /etc/kubeconfig

before_script:
  - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY

test:
  stage: test
  image: python:3.9
  script:
    - pip install -r requirements.txt
    - python -m pytest tests/ --junitxml=test-results.xml --cov=. --cov-report=xml
  artifacts:
    reports:
      junit: test-results.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml
  coverage: '/TOTAL.+ ([0-9]{{1,3}}%)/'

security-scan:
  stage: security
  image: python:3.9
  script:
    - pip install bandit safety
    - bandit -r . -f json -o bandit-report.json || true
    - safety check --json --output safety-report.json || true
  artifacts:
    reports:
      sast: bandit-report.json
    paths:
      - safety-report.json

build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t $DOCKER_IMAGE:$CI_COMMIT_SHA .
    - docker push $DOCKER_IMAGE:$CI_COMMIT_SHA
    - docker tag $DOCKER_IMAGE:$CI_COMMIT_SHA $DOCKER_IMAGE:latest
    - docker push $DOCKER_IMAGE:latest

deploy-staging:
  stage: deploy-staging
  image: bitnami/kubectl:latest
  script:
    - kubectl set image deployment/$APP_NAME $APP_NAME=$DOCKER_IMAGE:$CI_COMMIT_SHA -n staging
    - kubectl rollout status deployment/$APP_NAME -n staging
  environment:
    name: staging
    url: https://staging.{app_name}.com

integration-test:
  stage: integration-test
  image: python:3.9
  script:
    - pip install -r requirements.txt
    - python -m pytest integration_tests/
  dependencies:
    - deploy-staging

deploy-production:
  stage: deploy-production
  image: bitnami/kubectl:latest
  script:
    - kubectl set image deployment/$APP_NAME $APP_NAME=$DOCKER_IMAGE:$CI_COMMIT_SHA -n production
    - kubectl rollout status deployment/$APP_NAME -n production
  environment:
    name: production
    url: https://{app_name}.com
  when: manual
  only:
    - main
"""
        
        return gitlab_ci

class InfrastructureAsCode:
    """Infrastructure as Code management"""
    
    def __init__(self):
        self.templates = {}
    
    def create_terraform_infrastructure(self, project_name: str):
        """Create comprehensive Terraform infrastructure"""
        main_tf = f"""
terraform {{
  required_version = ">= 1.0"
  required_providers {{
    aws = {{
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }}
    kubernetes = {{
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }}
  }}
}}

provider "aws" {{
  region = var.aws_region
}}

# VPC Configuration
resource "aws_vpc" "main" {{
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {{
    Name = "{project_name}-vpc"
    Environment = var.environment
  }}
}}

resource "aws_internet_gateway" "main" {{
  vpc_id = aws_vpc.main.id
  
  tags = {{
    Name = "{project_name}-igw"
  }}
}}

resource "aws_subnet" "public" {{
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${{count.index + 1}}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = true
  
  tags = {{
    Name = "{project_name}-public-subnet-${{count.index + 1}}"
    Type = "public"
  }}
}}

resource "aws_subnet" "private" {{
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${{count.index + 10}}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  tags = {{
    Name = "{project_name}-private-subnet-${{count.index + 1}}"
    Type = "private"
  }}
}}

# EKS Cluster
resource "aws_eks_cluster" "main" {{
  name     = "{project_name}-cluster"
  role_arn = aws_iam_role.cluster.arn
  version  = "1.27"
  
  vpc_config {{
    subnet_ids = concat(aws_subnet.public[*].id, aws_subnet.private[*].id)
    endpoint_private_access = true
    endpoint_public_access  = true
  }}
  
  depends_on = [
    aws_iam_role_policy_attachment.cluster_AmazonEKSClusterPolicy,
  ]
}}

resource "aws_eks_node_group" "main" {{
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "{project_name}-nodes"
  node_role_arn   = aws_iam_role.node.arn
  subnet_ids      = aws_subnet.private[*].id
  
  scaling_config {{
    desired_size = 2
    max_size     = 4
    min_size     = 1
  }}
  
  instance_types = ["t3.medium"]
  
  depends_on = [
    aws_iam_role_policy_attachment.node_AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.node_AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.node_AmazonEC2ContainerRegistryReadOnly,
  ]
}}

# RDS Database
resource "aws_db_instance" "main" {{
  identifier = "{project_name}-db"
  
  engine         = "postgres"
  engine_version = "14.9"
  instance_class = "db.t3.micro"
  
  allocated_storage     = 20
  max_allocated_storage = 100
  storage_encrypted     = true
  
  db_name  = "{project_name.replace('-', '_')}"
  username = var.db_username
  password = var.db_password
  
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = aws_db_subnet_group.main.name
  
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"
  
  skip_final_snapshot = true
  
  tags = {{
    Name = "{project_name}-database"
  }}
}}
"""
        
        variables_tf = """
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "development"
}

variable "db_username" {
  description = "Database username"
  type        = string
  default     = "admin"
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}
"""
        
        outputs_tf = f"""
output "cluster_endpoint" {{
  description = "EKS cluster endpoint"
  value       = aws_eks_cluster.main.endpoint
}}

output "cluster_name" {{
  description = "EKS cluster name"
  value       = aws_eks_cluster.main.name
}}

output "database_endpoint" {{
  description = "RDS instance endpoint"
  value       = aws_db_instance.main.endpoint
}}

output "vpc_id" {{
  description = "VPC ID"
  value       = aws_vpc.main.id
}}
"""
        
        self.templates[project_name] = {
            'main.tf': main_tf,
            'variables.tf': variables_tf,
            'outputs.tf': outputs_tf,
            'created_at': datetime.now().isoformat()
        }
        
        return main_tf, variables_tf, outputs_tf

class MonitoringAndObservability:
    """Monitoring and observability platform"""
    
    def __init__(self):
        self.dashboards = {}
        self.alerts = {}
    
    def create_prometheus_config(self, app_name: str):
        """Create Prometheus monitoring configuration"""
        prometheus_config = f"""
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "alert_rules.yml"

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: '{app_name}'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        target_label: __address__

  - job_name: 'kubernetes-nodes'
    kubernetes_sd_configs:
      - role: node
    relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
"""
        
        alert_rules = f"""
groups:
  - name: {app_name}_alerts
    rules:
      - alert: HighCPUUsage
        expr: cpu_usage_percent > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage detected"
          description: "CPU usage is above 80% for more than 5 minutes"
      
      - alert: HighMemoryUsage
        expr: memory_usage_percent > 85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High memory usage detected"
          description: "Memory usage is above 85% for more than 5 minutes"
      
      - alert: ApplicationDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Application is down"
          description: "Application {{{{ $labels.instance }}}} is down"
"""
        
        return prometheus_config, alert_rules
    
    def create_grafana_dashboard(self, app_name: str):
        """Create Grafana dashboard configuration"""
        dashboard = {
            "dashboard": {
                "title": f"{app_name} Application Dashboard",
                "tags": ["devops", "monitoring"],
                "timezone": "browser",
                "panels": [
                    {
                        "title": "CPU Usage",
                        "type": "graph",
                        "targets": [
                            {
                                "expr": f"cpu_usage_percent{{job=\"{app_name}\"}}",
                                "legendFormat": "CPU Usage %"
                            }
                        ],
                        "yAxes": [
                            {"min": 0, "max": 100, "unit": "percent"}
                        ]
                    },
                    {
                        "title": "Memory Usage",
                        "type": "graph",
                        "targets": [
                            {
                                "expr": f"memory_usage_percent{{job=\"{app_name}\"}}",
                                "legendFormat": "Memory Usage %"
                            }
                        ]
                    },
                    {
                        "title": "Request Rate",
                        "type": "graph",
                        "targets": [
                            {
                                "expr": f"rate(http_requests_total{{job=\"{app_name}\"}}[5m])",
                                "legendFormat": "Requests/sec"
                            }
                        ]
                    },
                    {
                        "title": "Response Time",
                        "type": "graph",
                        "targets": [
                            {
                                "expr": f"histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{job=\"{app_name}\"}}[5m]))",
                                "legendFormat": "95th percentile"
                            }
                        ]
                    }
                ]
            }
        }
        
        return dashboard

# Flask API
app = Flask(__name__)

# Initialize platform components
project_manager = AgileProjectManager()
cicd_engine = CICDPipelineEngine()
iac_manager = InfrastructureAsCode()
monitoring = MonitoringAndObservability()

@app.route('/')
def dashboard():
    return jsonify({
        'service': 'IBM DevOps & Software Engineering Platform',
        'version': '1.0.0',
        'status': 'running',
        'capabilities': ['agile', 'cicd', 'infrastructure', 'monitoring'],
        'endpoints': ['/api/sprint', '/api/pipeline', '/api/infrastructure', '/api/monitoring']
    })

@app.route('/api/sprint', methods=['POST'])
def create_sprint():
    try:
        data = request.json
        sprint_name = data.get('sprint_name', 'Sprint 1')
        duration = data.get('duration_weeks', 2)
        
        sprint_id = project_manager.create_sprint(sprint_name, duration)
        
        # Add sample user stories
        stories = [
            {"title": "User authentication system", "points": 5, "priority": "high"},
            {"title": "Dashboard UI implementation", "points": 3, "priority": "medium"},
            {"title": "API endpoint development", "points": 8, "priority": "high"},
            {"title": "Unit test coverage", "points": 2, "priority": "low"}
        ]
        
        for story in stories:
            project_manager.add_user_story(
                sprint_id, story["title"], f"Description for {story['title']}", 
                story["points"], story["priority"]
            )
        
        metrics = project_manager.get_sprint_metrics(sprint_id)
        
        return jsonify({
            'status': 'success',
            'sprint_id': sprint_id,
            'sprint_name': sprint_name,
            'metrics': metrics
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/pipeline', methods=['POST'])
def create_pipeline():
    try:
        data = request.json
        app_name = data.get('app_name', 'sample-app')
        git_repo = data.get('git_repo', 'https://github.com/user/repo.git')
        pipeline_type = data.get('type', 'jenkins')
        
        if pipeline_type == 'jenkins':
            pipeline_config = cicd_engine.create_jenkins_pipeline(app_name, git_repo)
        else:
            pipeline_config = cicd_engine.create_gitlab_ci_config(app_name)
        
        return jsonify({
            'status': 'success',
            'app_name': app_name,
            'pipeline_type': pipeline_type,
            'config': pipeline_config
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/infrastructure', methods=['POST'])
def create_infrastructure():
    try:
        data = request.json
        project_name = data.get('project_name', 'sample-project')
        
        main_tf, variables_tf, outputs_tf = iac_manager.create_terraform_infrastructure(project_name)
        
        return jsonify({
            'status': 'success',
            'project_name': project_name,
            'terraform_files': {
                'main.tf': main_tf[:500] + '...',  # Truncate for response
                'variables.tf': variables_tf,
                'outputs.tf': outputs_tf
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/monitoring', methods=['POST'])
def create_monitoring():
    try:
        data = request.json
        app_name = data.get('app_name', 'sample-app')
        
        prometheus_config, alert_rules = monitoring.create_prometheus_config(app_name)
        grafana_dashboard = monitoring.create_grafana_dashboard(app_name)
        
        return jsonify({
            'status': 'success',
            'app_name': app_name,
            'prometheus_config': prometheus_config[:300] + '...',  # Truncate
            'alert_rules': alert_rules[:300] + '...',
            'grafana_dashboard': grafana_dashboard
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def main():
    print("🔧 IBM DevOps and Software Engineering Professional Certificate Capstone")
    print("⚙️ Enterprise DevOps Automation & Software Engineering Platform")
    print("=" * 70)
    
    # Demo sprint creation
    logger.info("Creating demo sprint...")
    sprint_id = project_manager.create_sprint("Demo Sprint", 2)
    
    # Demo pipeline creation
    logger.info("Creating demo CI/CD pipeline...")
    jenkins_pipeline = cicd_engine.create_jenkins_pipeline('demo-app', 'https://github.com/demo/app.git')
    
    # Demo infrastructure
    logger.info("Creating demo infrastructure...")
    main_tf, _, _ = iac_manager.create_terraform_infrastructure('demo-project')
    
    # Demo monitoring
    logger.info("Creating demo monitoring...")
    prometheus_config, _ = monitoring.create_prometheus_config('demo-app')
    
    print(f"\n✅ DevOps platform configured successfully!")
    print(f"📋 Sprints: 1 demo sprint created")
    print(f"🔄 Pipelines: {len(cicd_engine.pipelines)} configured")
    print(f"🏗️ Infrastructure: {len(iac_manager.templates)} templates")
    print(f"📊 Monitoring: Prometheus and Grafana configured")
    
    logger.info("Starting DevOps Platform API on http://localhost:5005")
    app.run(host='0.0.0.0', port=5005, debug=False)

if __name__ == '__main__':
    main()

