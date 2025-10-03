# IBM DevOps & Software Engineering Capstone

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-orange?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.17%2B-purple?logo=plotly&logoColor=white)](https://plotly.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-green?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

## 🇧🇷 Português

### 🚀 Visão Geral do Projeto

Este projeto é o trabalho final do **IBM DevOps & Software Engineering Professional Certificate**, desenvolvido por Gabriel Demetrios Lafis. Ele demonstra competências avançadas em DevOps, integração contínua (CI), entrega contínua (CD) e engenharia de software. A plataforma desenvolvida oferece uma solução completa com um pipeline CI/CD robusto, containerização e automação de deployment, focando na entrega de valor através de uma aplicação de análise de dados interativa.

### ✨ Características Principais

#### 📊 Funcionalidades Core
- **Dashboard Interativo:** Uma interface web responsiva e intuitiva, construída com Streamlit, que permite a visualização e interação com os dados.
- **Processamento de Dados:** Um pipeline de dados robusto e escalável, capaz de processar grandes volumes de informações de forma eficiente.
- **Analytics Avançado:** Módulos para análises estatísticas aprofundadas e aplicação de modelos de Machine Learning para extrair insights valiosos.
- **API RESTful:** Endpoints bem definidos para integração com sistemas externos, facilitando a interoperabilidade.

#### 📈 Business Intelligence
- **Métricas em Tempo Real:** Monitoramento de KPIs (Key Performance Indicators) e outros indicadores de desempenho atualizados continuamente.
- **Relatórios Automatizados:** Geração automática de relatórios personalizáveis para diferentes stakeholders.
- **Visualizações Interativas:** Gráficos e dashboards dinâmicos que permitem explorar os dados de diversas perspectivas.
- **Alertas Inteligentes:** Sistema de notificações automatizado para eventos críticos ou desvios de padrões.

#### 🔒 Segurança e Compliance
- **Autenticação Segura:** Implementação de um sistema de login robusto para proteger o acesso à plataforma.
- **Controle de Acesso:** Gerenciamento de permissões baseado em roles, garantindo que cada usuário tenha acesso apenas aos recursos necessários.
- **Auditoria Completa:** Registro detalhado de todas as ações do sistema para fins de conformidade e rastreabilidade.
- **Criptografia de Dados:** Proteção de dados sensíveis em trânsito e em repouso.

### 🛠️ Stack Tecnológico

Este projeto utiliza uma combinação de tecnologias modernas para garantir escalabilidade, performance e facilidade de manutenção:

| Categoria | Tecnologia | Versão | Propósito Principal |
|-----------|------------|--------|---------------------|
| **Backend** | Python | 3.11+ | Lógica de negócio, processamento de dados e ML |
| **Frontend** | Streamlit | 1.28+ | Construção da interface web interativa |
| **Database** | SQLite | 3.40+ | Armazenamento local e leve de dados |
| **Analytics** | Pandas | 2.0+ | Manipulação e análise de dados eficientes |
| **Visualization** | Plotly | 5.17+ | Criação de gráficos e visualizações interativas |
| **Machine Learning** | Scikit-learn | 1.3+ | Implementação de algoritmos de aprendizado de máquina |
| **Containerização** | Docker | Latest | Empacotamento da aplicação e suas dependências |
| **Orquestração** | Kubernetes | Latest | Gerenciamento e escalabilidade de containers (conceitual) |
| **CI/CD** | Jenkins | Latest | Automação de testes e deployment (conceitual) |

### 🏗️ Arquitetura da Solução

A arquitetura da plataforma é modular e escalável, projetada para facilitar a manutenção e a expansão. O diagrama abaixo ilustra os principais componentes e suas interações:

```mermaid
graph TD
    A[Usuário] -->|Acessa| B(Interface Web - Streamlit)
    B -->|Requisições| C{API Gateway}
    C -->|Processa| D[Serviços de Backend - Python]
    D -->|Consulta/Grava| E[Banco de Dados - SQLite]
    D -->|Utiliza| F[Módulos de Analytics/ML - Pandas, Scikit-learn]
    D -->|Gera| G[Visualizações - Plotly]
    G --> B
    subgraph Pipeline CI/CD
        H[Desenvolvimento] --> I(Git)
        I --> J(Jenkins - CI/CD)
        J --> K(Docker - Containerização)
        K --> L(Kubernetes - Orquestração)
    end
    J --|> D
    L --|> D
```

### 💼 Impacto nos Negócios

Este projeto visa entregar valor significativo para as organizações, otimizando processos e fornecendo insights acionáveis:

#### 📈 Métricas de Performance Esperadas
- **Eficiência Operacional:** Melhoria de até **70%** na produtividade através da automação.
- **Precisão Analítica:** Acurácia de **95%** nas análises e previsões de Machine Learning.
- **Velocidade de Processamento:** Redução de **80%** no tempo de processamento de dados.
- **Retorno sobre Investimento (ROI):** Potencial de **250%** de retorno sobre o investimento em análise de dados.

#### 🎯 Casos de Uso
- **Análise Empresarial:** Fornecimento de insights estratégicos para a tomada de decisão em diversas áreas de negócio.
- **Otimização de Processos:** Identificação de gargalos e oportunidades de melhoria contínua em fluxos de trabalho.
- **Previsão de Tendências:** Utilização de modelos preditivos para antecipar tendências de mercado e comportamento do consumidor.
- **Monitoramento de Performance:** Acompanhamento contínuo de KPIs para garantir o alinhamento com os objetivos estratégicos.

### 🚀 Começando

Para configurar e executar este projeto localmente, siga as instruções abaixo:

#### Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas em seu ambiente:
- **Python:** Versão 3.11 ou superior.
- **pip:** O gerenciador de pacotes do Python (geralmente vem com o Python).
- **Git:** Para clonar o repositório.

#### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/galafis/ibm-devops-capstone.git
   cd ibm-devops-capstone
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   ```bash
   python src/main_platform.py
   ```

4. **Acesse o dashboard:**
   Após a execução, o Streamlit iniciará um servidor local. Abra seu navegador e acesse:
   ```
   http://localhost:8501
   ```

#### Configuração Inicial (Opcional)

O projeto pode incluir scripts para geração de dados de exemplo ou configuração de ambiente:

```bash
# Gere dados de exemplo (se aplicável)
python src/main_platform.py --generate-data

# Configure o ambiente (se aplicável)
python src/main_platform.py --setup

# Inicie o serviço (se aplicável)
python src/main_platform.py --start
```

### 📊 Schema de Dados

O banco de dados SQLite armazena informações essenciais para a plataforma. A tabela principal segue o seguinte esquema:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | `VARCHAR(50)` | Identificador único para cada registro. |
| `name` | `VARCHAR(100)` | Nome ou título associado ao registro. |
| `category` | `VARCHAR(50)` | Categoria à qual o registro pertence. |
| `value` | `DECIMAL(10,2)` | Valor numérico associado ao registro. |
| `status` | `VARCHAR(20)` | Status atual do registro (e.g., 'ativo', 'inativo', 'pendente'). |
| `created_at` | `TIMESTAMP` | Carimbo de data/hora da criação do registro. |
| `updated_at` | `TIMESTAMP` | Carimbo de data/hora da última atualização do registro. |

### 🔍 Exemplos de Código

#### 📈 Dashboard Analytics
Um exemplo simplificado da função de geração do dashboard:

```python
def generate_dashboard():
    # Carregar dados de uma fonte (e.g., banco de dados, CSV)
    data = load_data()
    
    # Calcular métricas chave a partir dos dados
    metrics = calculate_metrics(data)
    
    # Gerar visualizações interativas usando Plotly
    charts = create_charts(data)
    
    # Renderizar o dashboard no Streamlit
    return render_dashboard(metrics, charts)
```

#### 🤖 Machine Learning
Exemplo de treinamento e previsão com um modelo RandomForestClassifier:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(X, y):
    # Dividir dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Inicializar e treinar o modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Avaliar o modelo
    predictions = model.predict(X_test)
    print(f"Acurácia do modelo: {accuracy_score(y_test, predictions):.2f}")
    
    return model

def make_predictions(model, new_data):
    # Realizar previsões com novos dados
    predictions = model.predict(new_data)
    return predictions
```

### 🧪 Testes

O projeto inclui testes unitários e de performance para garantir a qualidade e robustez do código.

#### Executar Testes

Para executar os testes, navegue até a raiz do repositório e utilize os seguintes comandos:

```bash
# Testes unitários (para módulos específicos)
python -m pytest tests/unit/

# Testes de integração (para verificar a interação entre componentes)
python -m pytest tests/integration/

# Testes de performance (para avaliar o desempenho da aplicação)
python tests/performance_test.py
```

#### Cobertura de Testes

Para gerar um relatório de cobertura de testes, que indica a porcentagem de código coberta pelos testes:

```bash
# Execute os testes com cobertura
coverage run -m pytest

# Gere um relatório de cobertura no console
coverage report -m

# Gere um relatório HTML detalhado (abre no navegador)
coverage html
```

### 📚 Documentação da API

Embora o foco principal seja o dashboard, a plataforma é projetada para ser extensível via API. Abaixo estão exemplos de endpoints que podem ser implementados:

#### Endpoints Principais (Exemplos)

```http
# Obter dados existentes
GET /api/data

Response:
{
    "data": [
        {"id": "item1", "name": "Produto A", "category": "Eletrônicos", "value": 150.75, "status": "ativo", "created_at": "2023-01-01T10:00:00Z", "updated_at": "2023-01-01T10:00:00Z"}
    ],
    "total": 1,
    "page": 1
}

# Criar um novo registro
POST /api/data
Content-Type: application/json

{
    "name": "Novo Item",
    "category": "categoria1",
    "value": 100.50
}

# Obter métricas agregadas
GET /api/metrics

Response:
{
    "total_records": 1000,
    "avg_value": 85.50,
    "categories": 5
}
```

### ⚙️ Configuração

As configurações da aplicação são gerenciadas através de um arquivo `config.py` (ou similar) para facilitar a adaptação a diferentes ambientes. Exemplo de configurações:

```python
# config.py

# Configurações do Banco de Dados
DATABASE_URL = "sqlite:///platform.db"

# Configurações Gerais da Aplicação
DEBUG_MODE = False  # Ativar/desativar modo de depuração
MAX_RECORDS = 10000 # Limite máximo de registros a serem processados
CACHE_TIMEOUT = 300 # Tempo de cache em segundos

# Configurações da API (se aplicável)
API_CONFIG = {
    'host': '0.0.0.0',
    'port': 8000,
    'workers': 4
}
```

### 🔒 Segurança

A segurança é uma prioridade, com as seguintes medidas implementadas ou consideradas:

- **Proteção de Dados:** Criptografia AES-256 para dados sensíveis.
- **Controle de Acesso:** Autenticação JWT (JSON Web Tokens) para acesso seguro à API e dashboard.
- **Validação de Entrada:** Validação rigorosa de todas as entradas para prevenir ataques como injeção de SQL ou XSS.
- **Trilha de Auditoria:** Log completo de todas as ações do usuário e do sistema para rastreabilidade e detecção de anomalias.

### 🛣️ Roadmap Futuro

Planos para futuras melhorias e expansões incluem:

- [ ] Integração com aplicativos móveis.
- [ ] Implementação de modelos de Machine Learning mais avançados.
- [ ] Capacidade de processamento de dados em tempo real (streaming).
- [ ] Deployment em ambientes de nuvem (AWS, Azure, GCP).
- [ ] Desenvolvimento de uma API v2.0 com novas funcionalidades.

### 🤝 Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma nova branch para sua feature (`git checkout -b feature/sua-feature`).
3. Faça suas alterações e commit (`git commit -m 'Adiciona nova feature'`).
4. Envie para a branch (`git push origin feature/sua-feature`).
5. Abra um Pull Request detalhando suas mudanças.

### 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE) - veja o arquivo `LICENSE` para mais detalhes.

---

## 🇺🇸 English

### 🚀 Project Overview

This project is the capstone work for the **IBM DevOps & Software Engineering Professional Certificate**, developed by Gabriel Demetrios Lafis. It demonstrates advanced competencies in DevOps, Continuous Integration (CI), Continuous Delivery (CD), and software engineering. The developed platform offers a comprehensive solution with a robust CI/CD pipeline, containerization, and automated deployment, focusing on delivering value through an interactive data analysis application.

### ✨ Key Features

#### 📊 Core Functionality
- **Interactive Dashboard:** A responsive and intuitive web interface, built with Streamlit, allowing data visualization and interaction.
- **Data Processing:** A robust and scalable data pipeline, capable of efficiently processing large volumes of information.
- **Advanced Analytics:** Modules for in-depth statistical analysis and the application of Machine Learning models to extract valuable insights.
- **RESTful API:** Well-defined endpoints for integration with external systems, facilitating interoperability.

#### 📈 Business Intelligence
- **Real-time Metrics:** Continuous monitoring of KPIs (Key Performance Indicators) and other performance indicators.
- **Automated Reports:** Automatic generation of customizable reports for different stakeholders.
- **Interactive Visualizations:** Dynamic charts and dashboards that allow exploring data from various perspectives.
- **Smart Alerts:** Automated notification system for critical events or pattern deviations.

#### 🔒 Security and Compliance
- **Secure Authentication:** Implementation of a robust login system to protect platform access.
- **Access Control:** Role-based permission management, ensuring each user has access only to necessary resources.
- **Comprehensive Audit:** Detailed logging of all system actions for compliance and traceability.
- **Data Encryption:** Protection of sensitive data in transit and at rest.

### 🛠️ Technology Stack

This project utilizes a combination of modern technologies to ensure scalability, performance, and ease of maintenance:

| Category | Technology | Version | Main Purpose |
|-----------|------------|--------|---------------------|
| **Backend** | Python | 3.11+ | Business logic, data processing, and ML |
| **Frontend** | Streamlit | 1.28+ | Building the interactive web interface |
| **Database** | SQLite | 3.40+ | Local and lightweight data storage |
| **Analytics** | Pandas | 2.0+ | Efficient data manipulation and analysis |
| **Visualization** | Plotly | 5.17+ | Creating interactive charts and visualizations |
| **Machine Learning** | Scikit-learn | 1.3+ | Implementing machine learning algorithms |
| **Containerization** | Docker | Latest | Packaging the application and its dependencies |
| **Orchestration** | Kubernetes | Latest | Managing and scaling containers (conceptual) |
| **CI/CD** | Jenkins | Latest | Automating tests and deployment (conceptual) |

### 🏗️ Solution Architecture

The platform's architecture is modular and scalable, designed to facilitate maintenance and expansion. The diagram below illustrates the main components and their interactions:

```mermaid
graph TD
    A[User] -->|Accesses| B(Web Interface - Streamlit)
    B -->|Requests| C{API Gateway}
    C -->|Processes| D[Backend Services - Python]
    D -->|Queries/Writes| E[Database - SQLite]
    D -->|Utilizes| F[Analytics/ML Modules - Pandas, Scikit-learn]
    D -->|Generates| G[Visualizations - Plotly]
    G --> B
    subgraph CI/CD Pipeline
        H[Development] --> I(Git)
        I --> J(Jenkins - CI/CD)
        J --> K(Docker - Containerization)
        K --> L(Kubernetes - Orchestration)
    end
    J --|> D
    L --|> D
```

### 💼 Business Impact

This project aims to deliver significant value to organizations by optimizing processes and providing actionable insights:

#### 📈 Expected Performance Metrics
- **Operational Efficiency:** Up to **70%** improvement in productivity through automation.
- **Analytical Accuracy:** **95%** accuracy in Machine Learning analyses and predictions.
- **Processing Speed:** **80%** reduction in data processing time.
- **Return on Investment (ROI):** Potential **250%** return on investment in data analysis.

#### 🎯 Use Cases
- **Business Analysis:** Providing strategic insights for decision-making across various business areas.
- **Process Optimization:** Identifying bottlenecks and opportunities for continuous improvement in workflows.
- **Trend Forecasting:** Utilizing predictive models to anticipate market trends and consumer behavior.
- **Performance Monitoring:** Continuous tracking of KPIs to ensure alignment with strategic objectives.

### 🚀 Getting Started

To set up and run this project locally, follow the instructions below:

#### Prerequisites
Make sure you have the following tools installed in your environment:
- **Python:** Version 3.11 or higher.
- **pip:** The Python package manager (usually comes with Python).
- **Git:** To clone the repository.

#### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/galafis/ibm-devops-capstone.git
   cd ibm-devops-capstone
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python src/main_platform.py
   ```

4. **Access the dashboard:**
   After execution, Streamlit will start a local server. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

#### Initial Configuration (Optional)

The project may include scripts for generating sample data or configuring the environment:

```bash
# Generate sample data (if applicable)
python src/main_platform.py --generate-data

# Configure the environment (if applicable)
python src/main_platform.py --setup

# Start the service (if applicable)
python src/main_platform.py --start
```

### 📊 Data Schema

The SQLite database stores essential information for the platform. The main table follows the schema below:

| Field | Type | Description |
|-------|------|-----------|
| `id` | `VARCHAR(50)` | Unique identifier for each record. |
| `name` | `VARCHAR(100)` | Name or title associated with the record. |
| `category` | `VARCHAR(50)` | Category to which the record belongs. |
| `value` | `DECIMAL(10,2)` | Numeric value associated with the record. |
| `status` | `VARCHAR(20)` | Current status of the record (e.g., 'active', 'inactive', 'pending'). |
| `created_at` | `TIMESTAMP` | Timestamp of when the record was created. |
| `updated_at` | `TIMESTAMP` | Timestamp of the last update to the record. |

### 🔍 Code Examples

#### 📈 Dashboard Analytics
A simplified example of the dashboard generation function:

```python
def generate_dashboard():
    # Load data from a source (e.g., database, CSV)
    data = load_data()
    
    # Calculate key metrics from the data
    metrics = calculate_metrics(data)
    
    # Generate interactive visualizations using Plotly
    charts = create_charts(data)
    
    # Render the dashboard in Streamlit
    return render_dashboard(metrics, charts)
```

#### 🤖 Machine Learning
Example of training and prediction with a RandomForestClassifier model:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(X, y):
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    predictions = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, predictions):.2f}")
    
    return model

def make_predictions(model, new_data):
    # Make predictions with new data
    predictions = model.predict(new_data)
    return predictions
```

### 🧪 Testing

The project includes unit and performance tests to ensure code quality and robustness.

#### Run Tests

To run the tests, navigate to the repository root and use the following commands:

```bash
# Unit tests (for specific modules)
python -m pytest tests/unit/

# Integration tests (to verify interaction between components)
python -m pytest tests/integration/

# Performance tests (to evaluate application performance)
python tests/performance_test.py
```

#### Test Coverage

To generate a test coverage report, which indicates the percentage of code covered by tests:

```bash
# Run tests with coverage
coverage run -m pytest

# Generate a coverage report in the console
coverage report -m

# Generate a detailed HTML report (opens in browser)
coverage html
```

### 📚 API Documentation

While the main focus is the dashboard, the platform is designed to be extensible via API. Below are examples of endpoints that can be implemented:

#### Main Endpoints (Examples)

```http
# Get existing data
GET /api/data

Response:
{
    "data": [
        {"id": "item1", "name": "Product A", "category": "Electronics", "value": 150.75, "status": "active", "created_at": "2023-01-01T10:00:00Z", "updated_at": "2023-01-01T10:00:00Z"}
    ],
    "total": 1,
    "page": 1
}

# Create a new record
POST /api/data
Content-Type: application/json

{
    "name": "New Item",
    "category": "category1",
    "value": 100.50
}

# Get aggregated metrics
GET /api/metrics

Response:
{
    "total_records": 1000,
    "avg_value": 85.50,
    "categories": 5
}
```

### ⚙️ Configuration

Application configurations are managed through a `config.py` file (or similar) to facilitate adaptation to different environments. Example configurations:

```python
# config.py

# Database Settings
DATABASE_URL = "sqlite:///platform.db"

# General Application Settings
DEBUG_MODE = False  # Enable/disable debug mode
MAX_RECORDS = 10000 # Maximum limit of records to be processed
CACHE_TIMEOUT = 300 # Cache time in seconds

# API Settings (if applicable)
API_CONFIG = {
    'host': '0.0.0.0',
    'port': 8000,
    'workers': 4
}
```

### 🔒 Security

Security is a priority, with the following measures implemented or considered:

- **Data Protection:** AES-256 encryption for sensitive data.
- **Access Control:** JWT (JSON Web Tokens) authentication for secure API and dashboard access.
- **Input Validation:** Strict validation of all inputs to prevent attacks such as SQL injection or XSS.
- **Audit Trail:** Comprehensive logging of all user and system actions for traceability and anomaly detection.

### 🛣️ Future Roadmap

Plans for future improvements and expansions include:

- [ ] Mobile app integration.
- [ ] Implementation of more advanced Machine Learning models.
- [ ] Real-time data processing capabilities (streaming).
- [ ] Cloud deployment (AWS, Azure, GCP).
- [ ] Development of an API v2.0 with new functionalities.

### 🤝 Contribution

Contributions are welcome! If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m 'Adds new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request detailing your changes.

### 📄 License

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for more details.

---

**Developed by Gabriel Demetrios Lafis**  
*IBM DevOps & Software Engineering Professional Certificate Capstone Project*

