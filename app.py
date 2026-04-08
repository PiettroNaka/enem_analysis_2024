import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Backend não-interativo
import matplotlib.pyplot as plt
import seaborn as sns
from utils.database import load_combined_data
from utils.statistics import SamplingAnalysis, calculate_frequency_distribution, identify_variable_types
import warnings
warnings.filterwarnings('ignore')

# Configuração da página - SIMPLES
st.set_page_config(
    page_title="Análise ENEM 2024",
    page_icon="📊",
    layout="wide"
)

# Configurar matplotlib
matplotlib.rcParams['figure.max_open_warning'] = 0
plt.style.use('default')
sns.set_style("whitegrid")

# Sidebar
st.sidebar.title("Análise ENEM 2024")

page = st.sidebar.radio(
    "Página:",
    ["Início", "Análise Exploratória", "Amostragem", "Comparação", "Relatório"]
)

# Página: Início
if page == "Início":
    st.title("Análise Exploratória - ENEM 2024")
    
    st.write("""
    Análise completa dos dados do ENEM 2024 do Big Data-IESB.
    
    **Funcionalidades:**
    - Análise exploratória de dados
    - Três tipos de amostragem
    - Comparação de amostras
    - Relatório técnico
    """)

# Página: Análise Exploratória
elif page == "Análise Exploratória":
    st.title("Análise Exploratória")
    
    st.info("Carregando dados...")
    
    try:
        @st.cache_data(ttl=3600)
        def load_data():
            return load_combined_data(limit=50000)
        
        df = load_data()
        st.success(f"Dados carregados: {len(df):,} registros")
        
        # Resumo
        col1, col2, col3 = st.columns(3)
        col1.metric("Total", f"{len(df):,}")
        col2.metric("Colunas", len(df.columns))
        col3.metric("Memória", f"{df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
        
        st.divider()
        
        # Variáveis qualitativas
        st.subheader("Variáveis Qualitativas")
        
        qual_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        if qual_cols:
            selected_qual = st.selectbox("Selecione:", qual_cols, key="qual")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("Distribuição:")
                freq = df[selected_qual].value_counts().head(10)
                st.dataframe(freq)
            
            with col2:
                st.write("Gráfico:")
                fig, ax = plt.subplots(figsize=(8, 5))
                df[selected_qual].value_counts().head(10).plot(kind='barh', ax=ax)
                st.pyplot(fig, use_container_width=True)
                plt.close('all')
        
        st.divider()
        
        # Variáveis quantitativas
        st.subheader("Variáveis Quantitativas")
        
        quant_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        if quant_cols:
            selected_quant = st.selectbox("Selecione:", quant_cols, key="quant")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("Estatísticas:")
                stats = {
                    'Média': df[selected_quant].mean(),
                    'Mediana': df[selected_quant].median(),
                    'Desvio': df[selected_quant].std(),
                    'Min': df[selected_quant].min(),
                    'Max': df[selected_quant].max()
                }
                st.dataframe(pd.DataFrame(stats, index=[0]).T)
            
            with col2:
                st.write("Histograma:")
                fig, ax = plt.subplots(figsize=(8, 5))
                ax.hist(df[selected_quant].dropna(), bins=30, edgecolor='black')
                st.pyplot(fig, use_container_width=True)
                plt.close('all')
        
        st.divider()
        
        # Correlação
        st.subheader("Correlação")
        
        note_cols = [c for c in quant_cols if 'nota' in c.lower()]
        
        if len(note_cols) > 1:
            corr = df[note_cols].corr()
            
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax, cbar=True)
            st.pyplot(fig, use_container_width=True)
            plt.close('all')
    
    except Exception as e:
        st.error(f"Erro: {str(e)}")

# Página: Amostragem
elif page == "Amostragem":
    st.title("Amostragem Estatística")
    
    st.info("Carregando população...")
    
    try:
        @st.cache_data(ttl=3600)
        def load_pop():
            return load_combined_data(limit=100000)
        
        df_pop = load_pop()
        st.success(f"População: {len(df_pop):,} registros")
        
        # Parâmetros
        col1, col2 = st.columns(2)
        conf = col1.slider("Confiança (%)", 90, 99, 95) / 100
        margin = col2.slider("Erro (%)", 1, 10, 5) / 100
        
        st.divider()
        
        # Calcular tamanho
        sampling = SamplingAnalysis(df_pop, confidence_level=conf)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("População", f"{len(df_pop):,}")
        col2.metric("Amostra", f"{sampling.sample_size:,}")
        col3.metric("%", f"{(sampling.sample_size/len(df_pop))*100:.2f}%")
        
        st.divider()
        
        if st.button("Gerar Amostras"):
            with st.spinner("Gerando..."):
                s1 = sampling.simple_random_sampling()
                s2 = sampling.systematic_sampling()
                s3 = sampling.stratified_sampling('tp_sexo') if 'tp_sexo' in df_pop.columns else None
                
                st.session_state.s1 = s1
                st.session_state.s2 = s2
                st.session_state.s3 = s3
                st.session_state.pop = df_pop
                
                st.success("Amostras geradas!")
        
        if 's1' in st.session_state:
            tab1, tab2, tab3 = st.tabs(["Aleatória", "Sistemática", "Estratificada"])
            
            with tab1:
                st.write(f"Tamanho: {len(st.session_state.s1):,}")
                st.dataframe(st.session_state.s1.head())
            
            with tab2:
                st.write(f"Tamanho: {len(st.session_state.s2):,}")
                st.dataframe(st.session_state.s2.head())
            
            with tab3:
                if st.session_state.s3 is not None:
                    st.write(f"Tamanho: {len(st.session_state.s3):,}")
                    st.dataframe(st.session_state.s3.head())
    
    except Exception as e:
        st.error(f"Erro: {str(e)}")

# Página: Comparação
elif page == "Comparação":
    st.title("Comparação de Amostras")
    
    if 's1' not in st.session_state:
        st.warning("Gere as amostras primeiro")
    else:
        st.success("Amostras carregadas")
        
        samples = {
            'Aleatória': st.session_state.s1,
            'Sistemática': st.session_state.s2,
        }
        
        if st.session_state.s3 is not None:
            samples['Estratificada'] = st.session_state.s3
        
        quant_cols = st.session_state.pop.select_dtypes(include=[np.number]).columns.tolist()
        note_cols = [c for c in quant_cols if 'nota' in c.lower()]
        
        if note_cols:
            sampling = SamplingAnalysis(st.session_state.pop)
            comp = sampling.compare_samples(samples, note_cols)
            
            st.dataframe(comp)

# Página: Relatório
elif page == "Relatório":
    st.title("Relatório Técnico")
    
    st.write("""
    Relatório técnico completo com análise exploratória, 
    amostragem e conclusões.
    """)
    
    try:
        with open('/home/ubuntu/enem_streamlit/reports/relatorio_tecnico.pdf', 'rb') as f:
            st.download_button(
                "Baixar PDF",
                f,
                "relatorio.pdf",
                "application/pdf"
            )
    except:
        st.warning("Arquivo não encontrado")
