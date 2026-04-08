import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import concurrent.futures
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Análise ENEM 2024", page_icon="📊", layout="wide")

# ── Conexão com timeout real via thread ──────────────────────────────────────
def _connect_and_load():
    from sqlalchemy import create_engine, text
    db_host     = st.secrets.get("db_host",     "bigdata.dataiesb.com")
    db_port     = st.secrets.get("db_port",     5432)
    db_name     = st.secrets.get("db_name",     "iesb")
    db_user     = st.secrets.get("db_user",     "data_iesb")
    db_password = st.secrets.get("db_password", "iesb")

    url = (f"postgresql+psycopg2://{db_user}:{db_password}"
           f"@{db_host}:{db_port}/{db_name}"
           f"?connect_timeout=8&sslmode=prefer")

    engine = create_engine(url, pool_pre_ping=True,
                           connect_args={"connect_timeout": 8,
                                         "options": "-c statement_timeout=20000"})
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

    query = """
        SELECT
            p.nu_sequencial, p.tp_sexo, p.tp_estado_civil,
            p.tp_cor_raca, p.tp_nacionalidade, p.tp_dependencia_adm_esc,
            r.nota_cn_ciencias_da_natureza,
            r.nota_ch_ciencias_humanas,
            r.nota_lc_linguagens_e_codigos,
            r.nota_mt_matematica,
            r.nota_redacao,
            r.nota_media_5_notas
        FROM ed_enem_2024_participantes p
        LEFT JOIN ed_enem_2024_resultados r
               ON p.nu_sequencial::text = r.nu_sequencial::text
        LIMIT 10000
    """
    df = pd.read_sql(query, engine)
    engine.dispose()
    return df

@st.cache_data(ttl=3600, show_spinner=False)
def load_database_data(timeout_sec=20):
    """Tenta carregar do banco com timeout total garantido."""
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
            future = ex.submit(_connect_and_load)
            return future.result(timeout=timeout_sec)
    except concurrent.futures.TimeoutError:
        st.sidebar.error(f"⏱ Banco não respondeu em {timeout_sec}s")
        return None
    except Exception as e:
        st.sidebar.error(f"❌ Erro DB: {e}")
        return None

# ── Dados de exemplo ─────────────────────────────────────────────────────────
def generate_example_data():
    np.random.seed(42)
    n = 10000
    return pd.DataFrame({
        'tp_sexo':         np.random.choice(['M', 'F'], n, p=[0.42, 0.58]),
        'tp_estado_civil': np.random.choice(['Solteiro','Casado','Viúvo','Divorciado'], n),
        'tp_cor_raca':     np.random.choice(['Branca','Preta','Parda','Amarela','Indígena'], n),
        'nota_cn_ciencias_da_natureza': np.random.normal(520, 80, n),
        'nota_ch_ciencias_humanas':     np.random.normal(530, 75, n),
        'nota_lc_linguagens_e_codigos': np.random.normal(510, 85, n),
        'nota_mt_matematica':           np.random.normal(495, 90, n),
        'nota_redacao':                 np.random.normal(540, 100, n),
        'nota_media_5_notas':           np.random.normal(519, 70, n),
    })

# ── Carregamento ─────────────────────────────────────────────────────────────
use_db = st.secrets.get("use_database", True)

with st.spinner("⏳ Conectando ao banco de dados..."):
    if use_db:
        df_data = load_database_data(timeout_sec=20)
        using_example = df_data is None
        if using_example:
            df_data = generate_example_data()
    else:
        df_data = generate_example_data()
        using_example = True

# ── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.title("📊 Análise ENEM 2024")
if using_example:
    st.sidebar.warning("⚠️ Usando dados de exemplo\n\nO banco pode estar inacessível desta rede.")
else:
    st.sidebar.success("✅ Conectado ao Big Data-IESB")

page = st.sidebar.radio("Página:", ["Início","Análise","Amostragem","Comparação","Relatório"])

# ═══════════════════════════════════════════════════════════════════════════════
# INÍCIO
# ═══════════════════════════════════════════════════════════════════════════════
if page == "Início":
    st.title("📊 Análise Exploratória — ENEM 2024")

    if using_example:
        st.warning("⚠️ Exibindo dados de exemplo. O banco `bigdata.dataiesb.com` não foi alcançado.")
    else:
        st.success("✅ Conectado ao Big Data-IESB!")

    st.write("""
    Bem-vindo à análise completa dos dados do ENEM 2024!

    **Funcionalidades:**
    - 📈 Análise exploratória de dados
    - 🎲 Três tipos de amostragem estatística
    - 📋 Comparação de amostras vs população
    - 📄 Relatório técnico
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Registros", f"{len(df_data):,}")
    col2.metric("Variáveis", len(df_data.columns))
    col3.metric("Período", "2024")

    st.subheader("Primeiros Registros")
    st.dataframe(df_data.head(10), use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════════
# ANÁLISE
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Análise":
    st.title("📈 Análise Exploratória")
    st.success(f"✅ Dados carregados: {len(df_data):,} registros")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total", f"{len(df_data):,}")
    col2.metric("Colunas", len(df_data.columns))
    col3.metric("Memória", f"{df_data.memory_usage(deep=True).sum()/1024**2:.1f} MB")

    st.divider()

    # Qualitativas
    st.subheader("📋 Variáveis Qualitativas")
    qual_cols = df_data.select_dtypes(include=['object']).columns.tolist()
    if qual_cols:
        selected_qual = st.selectbox("Selecione:", qual_cols, key="qual")
        c1, c2 = st.columns(2)
        with c1:
            st.write("**Distribuição de frequência:**")
            st.dataframe(df_data[selected_qual].value_counts().rename_axis(selected_qual).reset_index(name='Frequência'))
        with c2:
            fig, ax = plt.subplots(figsize=(8, 5))
            df_data[selected_qual].value_counts().plot(kind='barh', ax=ax, color='steelblue')
            ax.set_title(f"Distribuição de {selected_qual}")
            st.pyplot(fig, use_container_width=True)
            plt.close('all')

    st.divider()

    # Quantitativas
    st.subheader("📊 Variáveis Quantitativas")
    quant_cols = df_data.select_dtypes(include=[np.number]).columns.tolist()
    if quant_cols:
        selected_quant = st.selectbox("Selecione:", quant_cols, key="quant")
        c1, c2 = st.columns(2)
        with c1:
            st.write("**Estatísticas descritivas:**")
            s = df_data[selected_quant].dropna()
            stats = pd.DataFrame({
                'Estatística': ['Média','Mediana','Desvio Padrão','Mínimo','Máximo','Q1','Q3'],
                'Valor': [s.mean(), s.median(), s.std(), s.min(), s.max(),
                          s.quantile(.25), s.quantile(.75)]
            })
            st.dataframe(stats.set_index('Estatística').round(2))
        with c2:
            fig, axes = plt.subplots(1, 2, figsize=(10, 5))
            axes[0].hist(df_data[selected_quant].dropna(), bins=30, color='steelblue', edgecolor='white')
            axes[0].set_title("Histograma")
            axes[1].boxplot(df_data[selected_quant].dropna(), vert=True)
            axes[1].set_title("Box Plot")
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close('all')

    st.divider()

    # Correlação
    st.subheader("🔗 Matriz de Correlação — Notas")
    note_cols = [c for c in quant_cols if 'nota' in c.lower()]
    if len(note_cols) > 1:
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df_data[note_cols].corr(), annot=True, fmt='.2f',
                    cmap='coolwarm', ax=ax, square=True)
        ax.set_title("Correlação entre Notas")
        st.pyplot(fig, use_container_width=True)
        plt.close('all')

# ═══════════════════════════════════════════════════════════════════════════════
# AMOSTRAGEM
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Amostragem":
    st.title("🎲 Amostragem Estatística")
    st.success(f"✅ População: {len(df_data):,} registros")

    c1, c2 = st.columns(2)
    conf   = c1.slider("Nível de Confiança (%)", 90, 99, 95) / 100
    margin = c2.slider("Margem de Erro (%)", 1, 10, 5) / 100

    from scipy import stats as sp_stats
    z  = sp_stats.norm.ppf((1 + conf) / 2)
    n0 = (z**2 * 0.5 * 0.5) / (margin**2)
    n  = int(np.ceil(n0 / (1 + (n0 - 1) / len(df_data))))

    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("População (N)", f"{len(df_data):,}")
    c2.metric("Tamanho da Amostra (n)", f"{n:,}")
    c3.metric("Fração amostral", f"{n/len(df_data)*100:.3f}%")
    st.divider()

    if st.button("🎲 Gerar Amostras", type="primary"):
        with st.spinner("Gerando amostras..."):
            # Aleatória Simples
            s1 = df_data.sample(n=min(n, len(df_data)), random_state=42)

            # Sistemática
            k       = max(1, len(df_data) // n)
            start   = np.random.randint(0, k)
            indices = np.arange(start, len(df_data), k)[:n]
            s2 = df_data.iloc[indices].reset_index(drop=True)

            # Estratificada por sexo
            stratum_col = 'tp_sexo' if 'tp_sexo' in df_data.columns else None
            if stratum_col:
                sizes   = (df_data[stratum_col].value_counts() / len(df_data) * n).astype(int)
                samples = [df_data[df_data[stratum_col]==s].sample(
                               n=min(sz, (df_data[stratum_col]==s).sum()), random_state=42)
                           for s, sz in sizes.items() if sz > 0]
                s3 = pd.concat(samples, ignore_index=True)
            else:
                s3 = s1.copy()

            st.session_state.update(s1=s1, s2=s2, s3=s3, pop=df_data)
        st.success("✅ Amostras geradas!")

    if 's1' in st.session_state:
        tab1, tab2, tab3 = st.tabs(["Aleatória Simples","Sistemática","Estratificada"])
        for tab, key, label in [(tab1,'s1','Aleatória'), (tab2,'s2','Sistemática'), (tab3,'s3','Estratificada')]:
            with tab:
                st.write(f"**Tamanho:** {len(st.session_state[key]):,} registros")
                st.dataframe(st.session_state[key].head(10), use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════════
# COMPARAÇÃO
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Comparação":
    st.title("📋 Comparação de Amostras × População")

    if 's1' not in st.session_state:
        st.warning("⚠️ Gere as amostras primeiro na página **Amostragem**.")
    else:
        quant_cols = df_data.select_dtypes(include=[np.number]).columns.tolist()
        note_cols  = [c for c in quant_cols if 'nota' in c.lower()]

        if note_cols:
            rows = []
            for col in note_cols:
                for label, sample in [("População", st.session_state.pop),
                                       ("Aleatória Simples", st.session_state.s1),
                                       ("Sistemática",       st.session_state.s2),
                                       ("Estratificada",     st.session_state.s3)]:
                    s = sample[col].dropna()
                    rows.append({"Grupo": label, "Variável": col,
                                 "Média": round(s.mean(), 2),
                                 "Desvio Padrão": round(s.std(), 2),
                                 "N": len(s)})
            st.dataframe(pd.DataFrame(rows), use_container_width=True)

            # Gráfico de comparação de médias
            col_sel = st.selectbox("Variável para gráfico:", note_cols)
            df_plot = pd.DataFrame([r for r in rows if r['Variável'] == col_sel])
            fig, ax = plt.subplots(figsize=(8, 4))
            colors = ['#0284c7','#22c55e','#f59e0b','#a855f7']
            ax.bar(df_plot['Grupo'], df_plot['Média'], color=colors, edgecolor='white')
            ax.set_title(f"Comparação de Médias — {col_sel}")
            ax.set_ylabel("Média")
            st.pyplot(fig, use_container_width=True)
            plt.close('all')

# ═══════════════════════════════════════════════════════════════════════════════
# RELATÓRIO
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Relatório":
    st.title("📄 Relatório Técnico")
    st.write("Relatório técnico completo com análise exploratória, amostragem e conclusões.")

    pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports', 'relatorio_tecnico.pdf')
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as f:
            st.download_button("📥 Baixar Relatório em PDF", f,
                               "relatorio_tecnico_enem_2024.pdf", "application/pdf")
    else:
        st.warning("⚠️ Relatório PDF não encontrado em `reports/relatorio_tecnico.pdf`.")
