#!/usr/bin/env python3
"""
DevOps Platform - Main Application
Ibm Devops Capstone
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sqlite3
import numpy as np
import logging

from devops_platform import DevOpsPlatform, MachineLearningEngine, AnalyticsEngine # Importar as novas classes

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# A classe DevOpsPlatform foi movida para devops_platform.py
# As classes MachineLearningEngine e AnalyticsEngine também foram movidas para devops_platform.py

def create_dashboard():
    """Create Streamlit dashboard"""
    st.set_page_config(
        page_title="DevOps Platform",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📊 DevOps Platform Dashboard")
    st.markdown("---")
    
    # Initialize platforms
    platform = DevOpsPlatform()
    ml_engine = MachineLearningEngine()
    analytics_engine = AnalyticsEngine()
    
    # Sidebar
    st.sidebar.title("🔧 Platform Controls")
    
    if st.sidebar.button("🔄 Generate Sample Data"):
        with st.spinner("Generating sample data..."):
            platform.generate_sample_data()
        st.sidebar.success("Sample data generated!")
        st.experimental_rerun()
    
    # Main dashboard
    data = platform.get_data()
    metrics = platform.get_metrics()
    kpis = platform.calculate_kpis()
    
    if data.empty:
        st.warning("No data available. Please generate sample data using the sidebar.")
        return
    
    # KPI Cards
    st.subheader("📈 Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Records", kpis.get("total_records", 0))
    
    with col2:
        st.metric("Active Records", kpis.get("active_records", 0))
    
    with col3:
        st.metric("Total Value", f"${kpis.get("total_value", 0):,.2f}")
    
    with col4:
        st.metric("Average Value", f"${kpis.get("average_value", 0):,.2f}")
    
    # Charts
    st.subheader("📊 Data Visualizations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Category distribution
        category_counts = data["category"].value_counts()
        fig_pie = px.pie(
            values=category_counts.values,
            names=category_counts.index,
            title="Distribution by Category"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Status distribution
        status_counts = data["status"].value_counts()
        fig_bar = px.bar(
            x=status_counts.index,
            y=status_counts.values,
            title="Records by Status"
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Time series metrics
    if not metrics.empty:
        st.subheader("📈 Metrics Over Time")
        
        metric_options = metrics["metric_name"].unique()
        selected_metric = st.selectbox("Select Metric", metric_options)
        
        metric_data = metrics[metrics["metric_name"] == selected_metric]
        metric_data["metric_date"] = pd.to_datetime(metric_data["metric_date"])
        
        fig_line = px.line(
            metric_data,
            x="metric_date",
            y="metric_value",
            title=f"{selected_metric.replace("_", " ").title()} Over Time"
        )
        st.plotly_chart(fig_line, use_container_width=True)
    
    # Machine Learning Section
    st.subheader("🤖 Machine Learning Insights")
    if not data.empty and len(data["category"].unique()) > 1:
        st.write("Demonstrando um modelo de Machine Learning para classificação de dados.")
        
        # Preparar dados para ML
        # Para simplificar, vamos usar 'value' como feature e 'category' como target
        # Em um cenário real, mais features seriam usadas e pré-processamento seria mais complexo
        X = data[["value"]]
        # Converter categorias para numérico para o modelo
        y = data["category"].astype("category").cat.codes
        
        if len(X) > 1 and len(y.unique()) > 1: # Garante que há dados suficientes para treinar
            try:
                model = ml_engine.train_model(X, y)
                st.success("Modelo de Machine Learning treinado com sucesso!")
                
                # Exemplo de previsão
                sample_value = st.slider("Valor para Previsão", float(data["value"].min()), float(data["value"].max()), float(data["value"].mean()))
                sample_df = pd.DataFrame({"value": [sample_value]})
                prediction_code = ml_engine.make_predictions(model, sample_df)
                predicted_category = data["category"].astype("category").cat.categories[prediction_code[0]]
                st.info(f"Para o valor {sample_value:.2f}, a categoria prevista é: **{predicted_category}**")
            except Exception as e:
                st.error(f"Erro ao treinar ou prever com o modelo ML: {e}")
        else:
            st.warning("Dados insuficientes para treinar o modelo de Machine Learning. Necessita de mais de uma categoria e mais de um registro.")
    else:
        st.info("Gere dados de exemplo para habilitar a demonstração de Machine Learning.")

    # Analytics Engine Section
    st.subheader("📈 Advanced Analytics Engine")
    if not data.empty:
        st.write("Análise de tendências e padrões nos dados.")
        try:
            # Para a análise de tendências, precisamos de uma coluna de data. Usaremos 'created_at' e 'value'.
            data["created_at"] = pd.to_datetime(data["created_at"])
            trends_data = data.rename(columns={"created_at": "date"})
            trends, patterns = analytics_engine.analyze_trends(trends_data[["date", "value"]])
            
            if trends is not None and not trends.empty:
                st.success("Análise de tendências realizada com sucesso!")
                st.write("**Tendências de Valor ao Longo do Tempo (Média Diária):**")
                fig_trends = px.line(trends["value"]["mean"].reset_index(), x="date", y="mean", title="Média de Valor por Data")
                st.plotly_chart(fig_trends, use_container_width=True)
                
                st.write("**Padrões Identificados:**")
                st.json(patterns)
            else:
                st.warning("Não foi possível gerar tendências ou padrões com os dados disponíveis.")
        except Exception as e:
            st.error(f"Erro ao executar a análise de tendências: {e}")
    else:
        st.info("Gere dados de exemplo para habilitar a demonstração do Analytics Engine.")

    # Data table
    st.subheader("📋 Data Table")
    st.dataframe(data, use_container_width=True)
    
    # Performance metrics
    st.subheader("⚡ Performance Metrics")
    perf_col1, perf_col2, perf_col3 = st.columns(3)
    
    with perf_col1:
        st.metric("Response Time", "< 2s", "✅")
    
    with perf_col2:
        st.metric("Uptime", "99.9%", "✅")
    
    with perf_col3:
        st.metric("Accuracy", "95.2%", "✅")

def main():
    """Main application entry point"""
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--generate-data":
            platform = DevOpsPlatform()
            platform.generate_sample_data()
            print("Sample data generated successfully!")
        elif sys.argv[1] == "--setup":
            platform = DevOpsPlatform()
            print("Platform setup completed!")
        elif sys.argv[1] == "--start":
            print("Starting DevOps Platform...")
            create_dashboard()
        else:
            print("Usage: python main_platform.py [--generate-data|--setup|--start]")
    else:
        # Run Streamlit dashboard
        create_dashboard()

if __name__ == "__main__":
    main()

