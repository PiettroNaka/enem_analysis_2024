import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Configuração
st.set_page_config(page_title="Análise ENEM 2024", page_icon="📊", layout="wide")

# Sidebar
st.sidebar.title("📊 Análise ENEM 2024")
page = st.sidebar.radio("Página:", ["Início", "Análise", "Amostragem", "Comparação", "Relatório"])

# Página: Início
if page == "Início":
    st.title("📊 Análise Exploratória - ENEM 2024")
    st.write("""
    Bem-vindo à análise completa dos dados do ENEM 2024!
    
    **Funcionalidades:**
    - Análise exploratória de dados
    - Três tipos de amostragem
    - Comparação de amostras
    - Relatório técnico
    """)
    
    # Dados de exemplo
    st.subheader("Dados de Exemplo")
    np.random.seed(42)
    df_exemplo = pd.DataFrame({
        'Sexo': np.random.choice(['M', 'F'], 1000),
        'Nota_CN': np.random.normal(520, 80, 1000),
        'Nota_CH': np.random.normal(530, 75, 1000),
        'Nota_LC': np.random.normal(510, 85, 1000),
        'Nota_MT': np.random.normal(495, 90, 1000),
        'Nota_Redacao': np.random.normal(540, 100, 1000),
    })
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Registros", "1.000")
    col2.metric("Variáveis", "6")
    col3.metric("Período", "2024")
    
    st.dataframe(df_exemplo.head(10), use_container_width=True)

# Página: Análise
elif page == "Análise":
    st.title("📈 Análise Exploratória")
    
    # Gerar dados de exemplo
    np.random.seed(42)
    df = pd.DataFrame({
        'Sexo': np.random.choice(['Masculino', 'Feminino'], 1000),
        'Estado_Civil': np.random.choice(['Solteiro', 'Casado', 'Viúvo', 'Divorciado'], 1000),
        'Nota_CN': np.random.normal(520, 80, 1000),
        'Nota_CH': np.random.normal(530, 75, 1000),
        'Nota_LC': np.random.normal(510, 85, 1000),
        'Nota_MT': np.random.normal(495, 90, 1000),
        'Nota_Redacao': np.random.normal(540, 100, 1000),
    })
    
    st.success(f"✅ Dados carregados: {len(df):,} registros")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total", f"{len(df):,}")
    col2.metric("Colunas", len(df.columns))
    col3.metric("Memória", f"{df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
    
    st.divider()
    
    # Variáveis Qualitativas
    st.subheader("📋 Variáveis Qualitativas")
    qual_cols = ['Sexo', 'Estado_Civil']
    selected_qual = st.selectbox("Selecione:", qual_cols, key="qual")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Distribuição:**")
        freq = df[selected_qual].value_counts()
        st.dataframe(freq)
    
    with col2:
        st.write("**Gráfico:**")
        fig, ax = plt.subplots(figsize=(8, 5))
        df[selected_qual].value_counts().plot(kind='barh', ax=ax, color='steelblue')
        ax.set_title(f"Distribuição de {selected_qual}")
        st.pyplot(fig, use_container_width=True)
        plt.close('all')
    
    st.divider()
    
    # Variáveis Quantitativas
    st.subheader("📊 Variáveis Quantitativas")
    quant_cols = ['Nota_CN', 'Nota_CH', 'Nota_LC', 'Nota_MT', 'Nota_Redacao']
    selected_quant = st.selectbox("Selecione:", quant_cols, key="quant")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Estatísticas:**")
        stats = {
            'Média': df[selected_quant].mean(),
            'Mediana': df[selected_quant].median(),
            'Desvio': df[selected_quant].std(),
            'Min': df[selected_quant].min(),
            'Max': df[selected_quant].max()
        }
        st.dataframe(pd.DataFrame(stats, index=[0]).T)
    
    with col2:
        st.write("**Histograma:**")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(df[selected_quant], bins=30, edgecolor='black', color='steelblue')
        ax.set_title(f"Distribuição de {selected_quant}")
        st.pyplot(fig, use_container_width=True)
        plt.close('all')
    
    st.divider()
    
    # Correlação
    st.subheader("🔗 Análise de Correlação")
    corr = df[quant_cols].corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax, cbar=True)
    ax.set_title("Matriz de Correlação entre Notas")
    st.pyplot(fig, use_container_width=True)
    plt.close('all')

# Página: Amostragem
elif page == "Amostragem":
    st.title("🎲 Amostragem Estatística")
    
    # Gerar população
    np.random.seed(42)
    pop_size = 100000
    df_pop = pd.DataFrame({
        'Sexo': np.random.choice(['Masculino', 'Feminino'], pop_size, p=[0.42, 0.58]),
        'Nota_CN': np.random.normal(520, 80, pop_size),
        'Nota_CH': np.random.normal(530, 75, pop_size),
        'Nota_LC': np.random.normal(510, 85, pop_size),
        'Nota_MT': np.random.normal(495, 90, pop_size),
        'Nota_Redacao': np.random.normal(540, 100, pop_size),
    })
    
    st.success(f"✅ População: {len(df_pop):,} registros")
    
    # Parâmetros
    col1, col2 = st.columns(2)
    conf = col1.slider("Confiança (%)", 90, 99, 95) / 100
    margin = col2.slider("Erro (%)", 1, 10, 5) / 100
    
    # Calcular tamanho da amostra
    from scipy import stats as sp_stats
    z = sp_stats.norm.ppf((1 + conf) / 2)
    p = 0.5
    n0 = (z**2 * p * (1-p)) / (margin**2)
    n = int(np.ceil(n0 / (1 + (n0-1) / len(df_pop))))
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("População", f"{len(df_pop):,}")
    col2.metric("Amostra", f"{n:,}")
    col3.metric("%", f"{(n/len(df_pop))*100:.3f}%")
    
    st.divider()
    
    if st.button("Gerar Amostras"):
        with st.spinner("Gerando amostras..."):
            # Amostra Aleatória Simples
            s1 = df_pop.sample(n=n, random_state=42)
            
            # Amostra Sistemática
            k = len(df_pop) // n
            start = np.random.randint(0, k)
            indices = np.arange(start, len(df_pop), k)[:n]
            s2 = df_pop.iloc[indices].reset_index(drop=True)
            
            # Amostra Estratificada
            strata = df_pop['Sexo'].value_counts()
            strata_prop = strata / len(df_pop)
            strata_sizes = (strata_prop * n).astype(int)
            
            samples = []
            for stratum, size in strata_sizes.items():
                stratum_data = df_pop[df_pop['Sexo'] == stratum]
                sample = stratum_data.sample(n=min(size, len(stratum_data)), random_state=42)
                samples.append(sample)
            s3 = pd.concat(samples, ignore_index=True)
            
            st.session_state.s1 = s1
            st.session_state.s2 = s2
            st.session_state.s3 = s3
            st.session_state.pop = df_pop
            
            st.success("✅ Amostras geradas!")
    
    if 's1' in st.session_state:
        tab1, tab2, tab3 = st.tabs(["Aleatória Simples", "Sistemática", "Estratificada"])
        
        with tab1:
            st.write(f"**Tamanho:** {len(st.session_state.s1):,} registros")
            st.dataframe(st.session_state.s1.head(10), use_container_width=True)
        
        with tab2:
            st.write(f"**Tamanho:** {len(st.session_state.s2):,} registros")
            st.dataframe(st.session_state.s2.head(10), use_container_width=True)
        
        with tab3:
            st.write(f"**Tamanho:** {len(st.session_state.s3):,} registros")
            st.dataframe(st.session_state.s3.head(10), use_container_width=True)

# Página: Comparação
elif page == "Comparação":
    st.title("📋 Comparação de Amostras")
    
    if 's1' not in st.session_state:
        st.warning("⚠️ Gere as amostras primeiro na página 'Amostragem'")
    else:
        st.success("✅ Amostras carregadas")
        
        quant_cols = ['Nota_CN', 'Nota_CH', 'Nota_LC', 'Nota_MT', 'Nota_Redacao']
        
        # Comparar estatísticas
        results = []
        
        for col in quant_cols:
            # População
            results.append({
                'Grupo': 'População',
                'Variável': col,
                'Média': st.session_state.pop[col].mean(),
                'Desvio': st.session_state.pop[col].std(),
                'N': len(st.session_state.pop)
            })
            
            # Amostra 1
            results.append({
                'Grupo': 'Aleatória Simples',
                'Variável': col,
                'Média': st.session_state.s1[col].mean(),
                'Desvio': st.session_state.s1[col].std(),
                'N': len(st.session_state.s1)
            })
            
            # Amostra 2
            results.append({
                'Grupo': 'Sistemática',
                'Variável': col,
                'Média': st.session_state.s2[col].mean(),
                'Desvio': st.session_state.s2[col].std(),
                'N': len(st.session_state.s2)
            })
            
            # Amostra 3
            results.append({
                'Grupo': 'Estratificada',
                'Variável': col,
                'Média': st.session_state.s3[col].mean(),
                'Desvio': st.session_state.s3[col].std(),
                'N': len(st.session_state.s3)
            })
        
        comp_df = pd.DataFrame(results)
        st.dataframe(comp_df, use_container_width=True)

# Página: Relatório
elif page == "Relatório":
    st.title("📄 Relatório Técnico")
    
    st.write("""
    Relatório técnico completo com análise exploratória, 
    amostragem e conclusões.
    """)
    
    try:
        with open('/home/ubuntu/enem_streamlit/reports/relatorio_tecnico.pdf', 'rb') as f:
            st.download_button(
                "📥 Baixar Relatório em PDF",
                f,
                "relatorio_tecnico_enem_2024.pdf",
                "application/pdf"
            )
    except:
        st.warning("⚠️ Arquivo do relatório não encontrado")
