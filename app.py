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

# ── Conexão real ao banco ─────────────────────────────────────────────────────
def _connect_and_load():
    from sqlalchemy import create_engine, text
    db_host     = st.secrets.get("db_host",     "bigdata.dataiesb.com")
    db_port     = st.secrets.get("db_port",     5432)
    db_name     = st.secrets.get("db_name",     "iesb")
    db_user     = st.secrets.get("db_user",     "data_iesb")
    db_password = st.secrets.get("db_password", "iesb")

    url = (f"postgresql+psycopg2://{db_user}:{db_password}"
           f"@{db_host}:{db_port}/{db_name}"
           f"?connect_timeout=8&sslmode=disable")

    engine = create_engine(url, pool_pre_ping=False,
                           connect_args={"connect_timeout": 8})
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
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
            df = ex.submit(_connect_and_load).result(timeout=timeout_sec)
            return df, None
    except concurrent.futures.TimeoutError:
        return None, "timeout"
    except Exception as e:
        return None, str(e)


def _safe_int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _normalize_timeout_seconds(value, default=20):
    timeout = _safe_int(value, default)
    return max(1, timeout)

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
db_timeout = _normalize_timeout_seconds(st.secrets.get("db_timeout_seconds", 20), 20)
using_example = False
db_error = None
db_status_msg = ""

with st.spinner("⏳ Conectando ao banco de dados..."):
    if use_db:
        df_data, db_error = load_database_data(timeout_sec=db_timeout)
        if df_data is None:
            df_data = generate_example_data()
            using_example = True
            if db_error == "timeout":
                db_status_msg = f"Banco não respondeu em {db_timeout}s."
            elif db_error:
                db_status_msg = "Falha ao conectar no banco."
            else:
                db_status_msg = "Banco indisponível nesta rede."
    else:
        df_data = generate_example_data()
        using_example = True
        db_status_msg = "Conexão com banco desativada (use_database=false)."

# ── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.title("📊 Análise ENEM 2024")
if using_example:
    st.sidebar.warning(
        "⚠️ Usando dados de exemplo\n\n"
        f"{db_status_msg}\n"
        "O host bigdata.dataiesb.com pode não estar acessível desta rede."
    )
else:
    st.sidebar.success("✅ Big Data-IESB conectado")

page = st.sidebar.radio("Página:", ["Início","Análise","Amostragem","Comparação","Relatório"])

# helpers
def WIDTH(): return "stretch"

# ═════════════════════════════════════════════════════════════════════════════
# INÍCIO
# ═════════════════════════════════════════════════════════════════════════════
if page == "Início":
    st.title("📊 Análise Exploratória — ENEM 2024")

    if using_example:
        detail = ""
        if db_error and db_error not in {"timeout"}:
            detail = f"  \nDetalhe técnico: `{db_error}`."
        st.info(
            "ℹ️ **Exibindo dados simulados.**  \n"
            f"{db_status_msg}  \n"
            "Para usar dados reais, o banco precisa liberar conexões externas ou usar um túnel."
            f"{detail}"
        )
    else:
        st.success("✅ Conectado ao Big Data-IESB — dados reais carregados!")

    st.write("""
    Bem-vindo à análise completa dos dados do ENEM 2024!

    **Funcionalidades:**
    - 📈 Análise exploratória com gráficos interativos
    - 🎲 Três tipos de amostragem estatística
    - 📋 Comparação de amostras × população
    - 📄 Relatório técnico em PDF
    """)

    c1, c2, c3 = st.columns(3)
    c1.metric("Total de Registros", f"{len(df_data):,}")
    c2.metric("Variáveis", len(df_data.columns))
    c3.metric("Período", "2024")

    st.subheader("Primeiros Registros")
    st.dataframe(df_data.head(10), width=WIDTH())

# ═════════════════════════════════════════════════════════════════════════════
# ANÁLISE
# ═════════════════════════════════════════════════════════════════════════════
elif page == "Análise":
    st.title("📈 Análise Exploratória")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total", f"{len(df_data):,}")
    c2.metric("Colunas", len(df_data.columns))
    c3.metric("Memória", f"{df_data.memory_usage(deep=True).sum()/1024**2:.1f} MB")

    st.divider()

    # Qualitativas
    st.subheader("📋 Variáveis Qualitativas")
    qual_cols = df_data.select_dtypes(include=['object']).columns.tolist()
    if qual_cols:
        sel_q = st.selectbox("Selecione a variável:", qual_cols, key="qual")
        c1, c2 = st.columns(2)
        with c1:
            freq = (df_data[sel_q].value_counts()
                    .rename_axis(sel_q).reset_index(name='Frequência'))
            freq['%'] = (freq['Frequência'] / freq['Frequência'].sum() * 100).round(2)
            st.dataframe(freq, width=WIDTH())
        with c2:
            fig, ax = plt.subplots(figsize=(7, 4))
            df_data[sel_q].value_counts().plot(kind='barh', ax=ax, color='steelblue')
            ax.set_xlabel("Frequência")
            ax.set_title(f"Distribuição — {sel_q}")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close('all')

    st.divider()

    # Quantitativas
    st.subheader("📊 Variáveis Quantitativas")
    quant_cols = df_data.select_dtypes(include=[np.number]).columns.tolist()
    if quant_cols:
        sel_n = st.selectbox("Selecione a variável:", quant_cols, key="quant")
        s = df_data[sel_n].dropna()
        c1, c2 = st.columns(2)
        with c1:
            stats = pd.DataFrame({
                'Estatística': ['N','Média','Mediana','Desvio Padrão','Mínimo','Q1','Q3','Máximo'],
                'Valor':       [len(s), s.mean(), s.median(), s.std(),
                                s.min(), s.quantile(.25), s.quantile(.75), s.max()]
            }).set_index('Estatística').round(2)
            st.dataframe(stats, width=WIDTH())
        with c2:
            fig, axes = plt.subplots(1, 2, figsize=(9, 4))
            axes[0].hist(s, bins=30, color='steelblue', edgecolor='white')
            axes[0].set_title("Histograma"); axes[0].set_xlabel(sel_n)
            axes[1].boxplot(s, vert=True, patch_artist=True,
                            boxprops=dict(facecolor='steelblue', color='white'),
                            medianprops=dict(color='yellow'))
            axes[1].set_title("Box Plot")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close('all')

    st.divider()

    # Correlação
    st.subheader("🔗 Matriz de Correlação — Notas")
    note_cols = [c for c in quant_cols if 'nota' in c.lower()]
    if len(note_cols) > 1:
        fig, ax = plt.subplots(figsize=(10, 7))
        sns.heatmap(df_data[note_cols].corr(), annot=True, fmt='.2f',
                    cmap='coolwarm', ax=ax, square=True, linewidths=.5)
        ax.set_title("Correlação entre Notas", pad=12)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close('all')

# ═════════════════════════════════════════════════════════════════════════════
# AMOSTRAGEM
# ═════════════════════════════════════════════════════════════════════════════
elif page == "Amostragem":
    st.title("🎲 Amostragem Estatística")
    st.success(f"✅ População: {len(df_data):,} registros")

    c1, c2 = st.columns(2)
    conf   = c1.slider("Nível de Confiança (%)", 90, 99, 95) / 100
    margin = c2.slider("Margem de Erro (%)", 1, 10, 5) / 100

    from scipy import stats as sp_stats
    z  = sp_stats.norm.ppf((1 + conf) / 2)
    n0 = (z**2 * 0.5 * 0.5) / (margin**2)
    n  = int(np.ceil(n0 / (1 + (n0-1) / len(df_data))))

    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("População (N)", f"{len(df_data):,}")
    c2.metric("Tamanho da Amostra (n)", f"{n:,}")
    c3.metric("Fração amostral", f"{n/len(df_data)*100:.3f}%")
    st.divider()

    if st.button("🎲 Gerar Amostras", type="primary"):
        with st.spinner("Gerando amostras..."):
            s1 = df_data.sample(n=min(n, len(df_data)), random_state=42)

            k = max(1, len(df_data) // n)
            start = np.random.randint(0, k)
            s2 = df_data.iloc[np.arange(start, len(df_data), k)[:n]].reset_index(drop=True)

            if 'tp_sexo' in df_data.columns:
                sizes   = (df_data['tp_sexo'].value_counts() / len(df_data) * n).astype(int)
                samples = [df_data[df_data['tp_sexo']==s].sample(
                               n=min(sz, (df_data['tp_sexo']==s).sum()), random_state=42)
                           for s, sz in sizes.items() if sz > 0]
                s3 = pd.concat(samples, ignore_index=True)
            else:
                s3 = s1.copy()

            st.session_state.update(
                s1=s1,
                s2=s2,
                s3=s3,
                population_df=df_data,
            )
        st.success("✅ Amostras geradas com sucesso!")

    if 's1' in st.session_state:
        tab1, tab2, tab3 = st.tabs(["Aleatória Simples","Sistemática","Estratificada"])
        for tab, key in [(tab1,'s1'),(tab2,'s2'),(tab3,'s3')]:
            with tab:
                st.write(f"**Tamanho:** {len(st.session_state[key]):,} registros")
                st.dataframe(st.session_state[key].head(10), width=WIDTH())

# ═════════════════════════════════════════════════════════════════════════════
# COMPARAÇÃO
# ═════════════════════════════════════════════════════════════════════════════
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
                population = st.session_state.get("population_df", df_data)
                for label, sample in [("População",        population),
                                       ("Aleat. Simples",  st.session_state["s1"]),
                                       ("Sistemática",     st.session_state["s2"]),
                                       ("Estratificada",   st.session_state["s3"])]:
                    s = sample[col].dropna()
                    rows.append({"Grupo":label, "Variável":col,
                                 "Média":round(s.mean(),2),
                                 "Desvio Padrão":round(s.std(),2), "N":len(s)})
            st.dataframe(pd.DataFrame(rows), width=WIDTH())

            col_sel = st.selectbox("Variável para gráfico:", note_cols)
            df_plot = pd.DataFrame([r for r in rows if r['Variável']==col_sel])
            fig, ax = plt.subplots(figsize=(8, 4))
            colors = ['#0284c7','#22c55e','#f59e0b','#a855f7']
            bars = ax.bar(df_plot['Grupo'], df_plot['Média'], color=colors, edgecolor='white', width=0.6)
            ax.bar_label(bars, fmt='%.1f', padding=3)
            ax.set_title(f"Comparação de Médias — {col_sel}")
            ax.set_ylabel("Média")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close('all')

# ═════════════════════════════════════════════════════════════════════════════
# RELATÓRIO
# ═════════════════════════════════════════════════════════════════════════════
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
