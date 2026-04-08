import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils.database import load_combined_data
from utils.statistics import SamplingAnalysis, calculate_frequency_distribution, identify_variable_types
import warnings
warnings.filterwarnings('ignore')

# Configuração da página
st.set_page_config(
    page_title="Análise ENEM 2024 - Big Data IESB",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configurar matplotlib para evitar problemas de renderização
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Sidebar
st.sidebar.title("🎯 Análise ENEM 2024")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Selecione a página:",
    ["📊 Início", "📈 Análise Exploratória", "🎲 Amostragem", "📋 Comparação de Amostras", "📄 Relatório"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Dados:** ENEM 2024 - Big Data IESB
    
    **Tabelas:**
    - ed_enem_2024_participantes
    - ed_enem_2024_resultados
    
    **Análises:**
    - Exploratória
    - Amostragem
    - Comparação
    """
)

# Página: Início
if page == "📊 Início":
    st.title("📊 Análise Exploratória - ENEM 2024")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📚 Tabela de Participantes", "ed_enem_2024_participantes")
    
    with col2:
        st.metric("📊 Tabela de Resultados", "ed_enem_2024_resultados")
    
    with col3:
        st.metric("🎯 Ano", "2024")
    
    st.markdown("---")
    
    st.subheader("📋 Sobre o Projeto")
    st.write("""
    Este projeto realiza uma análise exploratória completa dos dados do ENEM 2024, 
    armazenados no Big Data-IESB. A análise inclui:
    
    1. **Análise Exploratória**: Distribuição de frequências, gráficos e correlações
    2. **Amostragem Estatística**: Três tipos de amostragem com 20% da população
    3. **Comparação de Amostras**: Validação das amostras contra a população
    4. **Relatório Técnico**: Documento completo em LaTeX
    
    **Variáveis Analisadas:**
    - Qualitativas: Sexo, Estado Civil, Cor/Raça, Nacionalidade, Dependência Administrativa da Escola
    - Quantitativas: Notas (Ciências da Natureza, Ciências Humanas, Linguagens, Matemática, Redação)
    """)
    
    st.markdown("---")
    
    st.subheader("🚀 Como Usar")
    st.write("""
    1. Acesse a página **Análise Exploratória** para visualizar gráficos e tabelas
    2. Vá para **Amostragem** para gerar as três amostras
    3. Compare as amostras com a população em **Comparação de Amostras**
    4. Consulte o **Relatório** para análise detalhada
    """)

# Página: Análise Exploratória
elif page == "📈 Análise Exploratória":
    st.title("📈 Análise Exploratória dos Dados")
    
    st.info("⏳ Carregando dados... (primeira vez pode levar alguns minutos)")
    
    try:
        # Carrega dados com cache
        @st.cache_data(ttl=3600)
        def load_data():
            return load_combined_data(limit=100000)
        
        df = load_data()
        st.success(f"✅ Dados carregados: {len(df):,} registros")
        
        # Identifica tipos de variáveis
        var_types = identify_variable_types(df)
        
        st.subheader("📊 Resumo dos Dados")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Registros", f"{len(df):,}")
        with col2:
            st.metric("Variáveis Qualitativas", len(var_types['qualitative']))
        with col3:
            st.metric("Variáveis Quantitativas", len(var_types['quantitative']))
        
        st.markdown("---")
        
        # Análise de Variáveis Qualitativas
        st.subheader("📋 Variáveis Qualitativas")
        
        qualitative_cols = [col for col in var_types['qualitative'] if col in df.columns and df[col].notna().sum() > 0]
        
        if qualitative_cols:
            selected_qual = st.selectbox("Selecione uma variável qualitativa:", qualitative_cols, key="qual_select")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Distribuição de Frequência:**")
                freq_dist = calculate_frequency_distribution(df[selected_qual])
                st.dataframe(freq_dist, use_container_width=True)
            
            with col2:
                st.write("**Gráfico de Barras:**")
                fig, ax = plt.subplots(figsize=(10, 6))
                counts = df[selected_qual].value_counts().head(10)
                counts.plot(kind='bar', ax=ax, color='steelblue')
                ax.set_title(f"Distribuição de {selected_qual}")
                ax.set_xlabel(selected_qual)
                ax.set_ylabel("Frequência")
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                st.pyplot(fig, use_container_width=True)
                plt.close(fig)
        
        st.markdown("---")
        
        # Análise de Variáveis Quantitativas
        st.subheader("📊 Variáveis Quantitativas")
        
        quantitative_cols = [col for col in var_types['quantitative'] if col in df.columns and df[col].notna().sum() > 0]
        
        if quantitative_cols:
            selected_quant = st.selectbox("Selecione uma variável quantitativa:", quantitative_cols, key="quant_select")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Estatísticas Descritivas:**")
                stats_data = {
                    'Média': df[selected_quant].mean(),
                    'Mediana': df[selected_quant].median(),
                    'Desvio Padrão': df[selected_quant].std(),
                    'Mínimo': df[selected_quant].min(),
                    'Máximo': df[selected_quant].max(),
                    'Q1': df[selected_quant].quantile(0.25),
                    'Q3': df[selected_quant].quantile(0.75)
                }
                st.dataframe(pd.DataFrame(stats_data, index=[0]).T, use_container_width=True)
            
            with col2:
                st.write("**Histograma:**")
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.hist(df[selected_quant].dropna(), bins=50, color='steelblue', edgecolor='black')
                ax.set_title(f"Distribuição de {selected_quant}")
                ax.set_xlabel(selected_quant)
                ax.set_ylabel("Frequência")
                plt.tight_layout()
                st.pyplot(fig, use_container_width=True)
                plt.close(fig)
            
            st.write("**Box Plot:**")
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.boxplot(df[selected_quant].dropna(), vert=True)
            ax.set_ylabel(selected_quant)
            ax.set_title(f"Box Plot de {selected_quant}")
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
        
        st.markdown("---")
        
        # Análise de Correlação
        st.subheader("🔗 Análise de Correlação")
        
        if quantitative_cols:
            note_cols = [col for col in quantitative_cols if 'nota' in col.lower()]
            
            if len(note_cols) > 1:
                st.write("**Matriz de Correlação (Notas):**")
                corr_matrix = df[note_cols].corr()
                
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax)
                ax.set_title("Matriz de Correlação entre Notas")
                plt.tight_layout()
                st.pyplot(fig, use_container_width=True)
                plt.close(fig)
    
    except Exception as e:
        st.error(f"❌ Erro ao carregar dados: {str(e)}")
        st.info("Verifique a conexão com o banco de dados Big Data-IESB")

# Página: Amostragem
elif page == "🎲 Amostragem":
    st.title("🎲 Análise de Amostragem Estatística")
    
    st.info("⏳ Carregando dados da população...")
    
    try:
        @st.cache_data(ttl=3600)
        def load_pop_data():
            return load_combined_data(limit=500000)
        
        df_pop = load_pop_data()
        st.success(f"✅ População carregada: {len(df_pop):,} registros")
        
        # Parâmetros de amostragem
        col1, col2 = st.columns(2)
        
        with col1:
            confidence_level = st.slider("Nível de Confiança (%)", 90, 99, 95) / 100
        
        with col2:
            margin_of_error = st.slider("Margem de Erro (%)", 1, 10, 5) / 100
        
        # Inicializa análise de amostragem
        sampling = SamplingAnalysis(df_pop, confidence_level=confidence_level)
        
        st.markdown("---")
        
        st.subheader("📊 Tamanho da Amostra Calculado")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Tamanho da População", f"{len(df_pop):,}")
        
        with col2:
            st.metric("Tamanho da Amostra", f"{sampling.sample_size:,}")
        
        with col3:
            percentage = (sampling.sample_size / len(df_pop)) * 100
            st.metric("Percentual (%)", f"{percentage:.2f}%")
        
        st.markdown("---")
        
        st.subheader("🎯 Gerando Amostras")
        
        if st.button("Gerar Amostras", key="generate_samples"):
            with st.spinner("Gerando amostras..."):
                # Amostra Aleatória Simples
                sample_simple = sampling.simple_random_sampling()
                st.success("✅ Amostra Aleatória Simples gerada")
                
                # Amostra Sistemática
                sample_systematic = sampling.systematic_sampling()
                st.success("✅ Amostra Sistemática gerada")
                
                # Amostra Estratificada
                if 'tp_sexo' in df_pop.columns:
                    sample_stratified = sampling.stratified_sampling('tp_sexo')
                    st.success("✅ Amostra Estratificada gerada")
                else:
                    sample_stratified = None
                    st.warning("⚠️ Coluna 'tp_sexo' não encontrada para estratificação")
                
                # Armazena em session_state
                st.session_state.sample_simple = sample_simple
                st.session_state.sample_systematic = sample_systematic
                st.session_state.sample_stratified = sample_stratified
                st.session_state.population = df_pop
                st.session_state.sampling_info = {
                    'population_size': len(df_pop),
                    'sample_size': sampling.sample_size,
                    'confidence_level': confidence_level
                }
        
        st.markdown("---")
        
        st.subheader("📋 Visualizar Amostras")
        
        if 'sample_simple' in st.session_state:
            tab1, tab2, tab3 = st.tabs(["Aleatória Simples", "Sistemática", "Estratificada"])
            
            with tab1:
                st.write(f"**Tamanho:** {len(st.session_state.sample_simple):,} registros")
                st.dataframe(st.session_state.sample_simple.head(10), use_container_width=True)
            
            with tab2:
                st.write(f"**Tamanho:** {len(st.session_state.sample_systematic):,} registros")
                st.dataframe(st.session_state.sample_systematic.head(10), use_container_width=True)
            
            with tab3:
                if st.session_state.sample_stratified is not None:
                    st.write(f"**Tamanho:** {len(st.session_state.sample_stratified):,} registros")
                    st.dataframe(st.session_state.sample_stratified.head(10), use_container_width=True)
    
    except Exception as e:
        st.error(f"❌ Erro ao carregar dados: {str(e)}")
        st.info("Verifique a conexão com o banco de dados Big Data-IESB")

# Página: Comparação de Amostras
elif page == "📋 Comparação de Amostras":
    st.title("📋 Comparação de Amostras com População")
    
    if 'sample_simple' not in st.session_state:
        st.warning("⚠️ Gere as amostras primeiro na página 'Amostragem'")
    else:
        st.success("✅ Amostras carregadas")
        
        # Prepara dados para comparação
        samples_dict = {
            'Aleatória Simples': st.session_state.sample_simple,
            'Sistemática': st.session_state.sample_systematic,
        }
        
        if st.session_state.sample_stratified is not None:
            samples_dict['Estratificada'] = st.session_state.sample_stratified
        
        # Seleciona variáveis quantitativas para comparação
        var_types = identify_variable_types(st.session_state.population)
        quantitative_cols = [col for col in var_types['quantitative'] 
                            if col in st.session_state.population.columns 
                            and 'nota' in col.lower()]
        
        if quantitative_cols:
            st.subheader("📊 Comparação de Estatísticas")
            
            # Cria análise de comparação
            sampling = SamplingAnalysis(st.session_state.population)
            comparison_df = sampling.compare_samples(samples_dict, quantitative_cols)
            
            st.dataframe(comparison_df, use_container_width=True)
            
            st.markdown("---")
            
            st.subheader("📈 Visualização de Comparação")
            
            selected_var = st.selectbox("Selecione uma variável para visualizar:", quantitative_cols)
            
            # Gráfico de comparação de médias
            fig, ax = plt.subplots(figsize=(12, 6))
            
            comparison_subset = comparison_df[comparison_df['Variável'] == selected_var]
            
            ax.bar(comparison_subset['Grupo'], comparison_subset['Média'], color='steelblue', alpha=0.7)
            ax.set_title(f"Comparação de Médias - {selected_var}")
            ax.set_ylabel("Média")
            ax.set_xlabel("Grupo")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

# Página: Relatório
elif page == "📄 Relatório":
    st.title("📄 Relatório Técnico")
    
    st.info("📋 Relatório técnico completo em PDF")
    
    st.subheader("📋 Estrutura do Relatório")
    
    st.write("""
    1. **Introdução**
       - Sobre o ENEM
       - Importância da Estatística
       - Python e Streamlit
    
    2. **Metodologia**
       - Fonte de Dados
       - Métodos de Análise
       - Técnicas de Amostragem
    
    3. **Análise dos Dados**
       - Análise Exploratória
       - Distribuições de Frequência
       - Análise de Correlação
       - Amostragem Estatística
    
    4. **Conclusão**
       - Principais Achados
       - Recomendações
    
    5. **Referências Bibliográficas**
    """)
    
    st.markdown("---")
    
    st.subheader("📥 Download do Relatório")
    
    try:
        with open('/home/ubuntu/enem_streamlit/reports/relatorio_tecnico.pdf', 'rb') as pdf_file:
            st.download_button(
                label="📥 Baixar Relatório em PDF",
                data=pdf_file,
                file_name="relatorio_tecnico_enem_2024.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("⚠️ Arquivo do relatório não encontrado")

if __name__ == "__main__":
    pass
