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

# Função para carregar dados do banco de dados
@st.cache_data(ttl=3600)
def load_database_data():
    """Carrega dados do Big Data-IESB"""
    try:
        import streamlit as st
        from sqlalchemy import create_engine
        
        # Obter credenciais dos secrets
        db_host = st.secrets.get("db_host", "bigdata.dataiesb.com")
        db_port = st.secrets.get("db_port", 5432)
        db_name = st.secrets.get("db_name", "iesb")
        db_user = st.secrets.get("db_user", "data_iesb")
        db_password = st.secrets.get("db_password", "iesb")
        db_schema = st.secrets.get("db_schema", "public")
        
        # Criar string de conexão
        db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        
        # Conectar ao banco
        engine = create_engine(db_url)
        
        # Carregar dados
        query = """
        SELECT 
            p.*,
            r.nota_cn_ciencias_da_natureza,
            r.nota_ch_ciencias_humanas,
            r.nota_lc_linguagens_e_codigos,
            r.nota_mt_matematica,
            r.nota_redacao,
            r.nota_media_5_notas
        FROM ed_enem_2024_participantes p
        LEFT JOIN ed_enem_2024_resultados r ON p.nu_sequencial::text = r.nu_sequencial::text
        LIMIT 50000
        """
        
        df = pd.read_sql(query, engine)
        engine.dispose()
        return df
    
    except Exception as e:
        st.warning(f"⚠️ Não foi possível conectar ao banco de dados: {str(e)}")
        st.info("Usando dados de exemplo para demonstração...")
        return None

# Função para gerar dados de exemplo
def generate_example_data():
    """Gera dados de exemplo para demonstração"""
    np.random.seed(42)
    pop_size = 10000
    
    return pd.DataFrame({
        'tp_sexo': np.random.choice(['M', 'F'], pop_size, p=[0.42, 0.58]),
        'tp_estado_civil': np.random.choice(['Solteiro', 'Casado', 'Viúvo', 'Divorciado'], pop_size),
        'nota_cn_ciencias_da_natureza': np.random.normal(520, 80, pop_size),
        'nota_ch_ciencias_humanas': np.random.normal(530, 75, pop_size),
        'nota_lc_linguagens_e_codigos': np.random.normal(510, 85, pop_size),
        'nota_mt_matematica': np.random.normal(495, 90, pop_size),
        'nota_redacao': np.random.normal(540, 100, pop_size),
    })

# Carregar dados
use_db = st.secrets.get("use_database", False)

if use_db:
    df_data = load_database_data()
    if df_data is None:
        df_data = generate_example_data()
        using_example = True
    else:
        using_example = False
else:
    df_data = generate_example_data()
    using_example = True

# Sidebar
st.sidebar.title("📊 Análise ENEM 2024")

if using_example:
    st.sidebar.warning("⚠️ Usando dados de exemplo")
else:
    st.sidebar.success("✅ Conectado ao Big Data-IESB")

page = st.sidebar.radio("Página:", ["Início", "Análise", "Amostragem", "Comparação", "Relatório"])

# Página: Início
if page == "Início":
    st.title("📊 Análise Exploratória - ENEM 2024")
    
    if using_example:
        st.warning("⚠️ Esta é uma versão com dados de exemplo. Para usar dados reais, configure os secrets do Streamlit Cloud.")
    else:
        st.success("✅ Conectado ao Big Data-IESB!")
    
    st.write("""
    Bem-vindo à análise completa dos dados do ENEM 2024!
    
    **Funcionalidades:**
    - Análise exploratória de dados
    - Três tipos de amostragem
    - Comparação de amostras
    - Relatório técnico
    """)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Registros", f"{len(df_data):,}")
    col2.metric("Variáveis", len(df_data.columns))
    col3.metric("Período", "2024")
    
    st.subheader("Primeiros Registros")
    st.dataframe(df_data.head(10), use_container_width=True)

# Página: Análise
elif page == "Análise":
    st.title("📈 Análise Exploratória")
    
    st.success(f"✅ Dados carregados: {len(df_data):,} registros")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total", f"{len(df_data):,}")
    col2.metric("Colunas", len(df_data.columns))
    col3.metric("Memória", f"{df_data.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
    
    st.divider()
    
    # Variáveis Qualitativas
    st.subheader("📋 Variáveis Qualitativas")
    qual_cols = df_data.select_dtypes(include=['object']).columns.tolist()
    
    if qual_cols:
        selected_qual = st.selectbox("Selecione:", qual_cols, key="qual")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Distribuição:**")
            freq = df_data[selected_qual].value_counts()
            st.dataframe(freq)
        
        with col2:
            st.write("**Gráfico:**")
            fig, ax = plt.subplots(figsize=(8, 5))
            df_data[selected_qual].value_counts().plot(kind='barh', ax=ax, color='steelblue')
            ax.set_title(f"Distribuição de {selected_qual}")
            st.pyplot(fig, use_container_width=True)
            plt.close('all')
    
    st.divider()
    
    # Variáveis Quantitativas
    st.subheader("📊 Variáveis Quantitativas")
    quant_cols = df_data.select_dtypes(include=[np.number]).columns.tolist()
    
    if quant_cols:
        selected_quant = st.selectbox("Selecione:", quant_cols, key="quant")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Estatísticas:**")
            stats = {
                'Média': df_data[selected_quant].mean(),
                'Mediana': df_data[selected_quant].median(),
                'Desvio': df_data[selected_quant].std(),
                'Min': df_data[selected_quant].min(),
                'Max': df_data[selected_quant].max()
            }
            st.dataframe(pd.DataFrame(stats, index=[0]).T)
        
        with col2:
            st.write("**Histograma:**")
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.hist(df_data[selected_quant].dropna(), bins=30, edgecolor='black', color='steelblue')
            ax.set_title(f"Distribuição de {selected_quant}")
            st.pyplot(fig, use_container_width=True)
            plt.close('all')
    
    st.divider()
    
    # Correlação
    st.subheader("🔗 Análise de Correlação")
    note_cols = [c for c in quant_cols if 'nota' in c.lower()]
    
    if len(note_cols) > 1:
        corr = df_data[note_cols].corr()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax, cbar=True)
        ax.set_title("Matriz de Correlação entre Notas")
        st.pyplot(fig, use_container_width=True)
        plt.close('all')

# Página: Amostragem
elif page == "Amostragem":
    st.title("🎲 Amostragem Estatística")
    
    st.success(f"✅ População: {len(df_data):,} registros")
    
    # Parâmetros
    col1, col2 = st.columns(2)
    conf = col1.slider("Confiança (%)", 90, 99, 95) / 100
    margin = col2.slider("Erro (%)", 1, 10, 5) / 100
    
    # Calcular tamanho da amostra
    from scipy import stats as sp_stats
    z = sp_stats.norm.ppf((1 + conf) / 2)
    p = 0.5
    n0 = (z**2 * p * (1-p)) / (margin**2)
    n = int(np.ceil(n0 / (1 + (n0-1) / len(df_data))))
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("População", f"{len(df_data):,}")
    col2.metric("Amostra", f"{n:,}")
    col3.metric("%", f"{(n/len(df_data))*100:.3f}%")
    
    st.divider()
    
    if st.button("Gerar Amostras"):
        with st.spinner("Gerando amostras..."):
            # Amostra Aleatória Simples
            s1 = df_data.sample(n=min(n, len(df_data)), random_state=42)
            
            # Amostra Sistemática
            k = len(df_data) // n
            start = np.random.randint(0, max(1, k))
            indices = np.arange(start, len(df_data), max(1, k))[:n]
            s2 = df_data.iloc[indices].reset_index(drop=True)
            
            # Amostra Estratificada
            stratum_col = 'tp_sexo' if 'tp_sexo' in df_data.columns else None
            
            if stratum_col:
                strata = df_data[stratum_col].value_counts()
                strata_prop = strata / len(df_data)
                strata_sizes = (strata_prop * n).astype(int)
                
                samples = []
                for stratum, size in strata_sizes.items():
                    stratum_data = df_data[df_data[stratum_col] == stratum]
                    if len(stratum_data) > 0:
                        sample = stratum_data.sample(n=min(size, len(stratum_data)), random_state=42)
                        samples.append(sample)
                s3 = pd.concat(samples, ignore_index=True) if samples else s1.copy()
            else:
                s3 = s1.copy()
            
            st.session_state.s1 = s1
            st.session_state.s2 = s2
            st.session_state.s3 = s3
            st.session_state.pop = df_data
            
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
        
        quant_cols = df_data.select_dtypes(include=[np.number]).columns.tolist()
        note_cols = [c for c in quant_cols if 'nota' in c.lower()]
        
        if note_cols:
            # Comparar estatísticas
            results = []
            
            for col in note_cols:
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
