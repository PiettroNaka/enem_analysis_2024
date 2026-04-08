import pandas as pd
from sqlalchemy import create_engine
import streamlit as st

# Configurações de conexão
DB_USER = "data_iesb"
DB_PASS = "iesb"
DB_HOST = "bigdata.dataiesb.com"
DB_PORT = "5432"
DB_NAME = "iesb"

@st.cache_resource
def get_engine():
    """Retorna engine de conexão com o banco de dados."""
    db_url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(db_url)

@st.cache_data(ttl=3600)
def load_participantes(limit=None):
    """Carrega dados de participantes do ENEM 2024."""
    engine = get_engine()
    query = "SELECT * FROM ed_enem_2024_participantes"
    if limit:
        query += f" LIMIT {limit}"
    return pd.read_sql(query, engine)

@st.cache_data(ttl=3600)
def load_resultados(limit=None):
    """Carrega dados de resultados do ENEM 2024."""
    engine = get_engine()
    query = "SELECT * FROM ed_enem_2024_resultados"
    if limit:
        query += f" LIMIT {limit}"
    return pd.read_sql(query, engine)

@st.cache_data(ttl=3600)
def load_combined_data(limit=None):
    """Carrega dados combinados de participantes e resultados."""
    engine = get_engine()
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
    LEFT JOIN ed_enem_2024_resultados r ON p.nu_sequencial = r.nu_sequencial
    """
    if limit:
        query += f" LIMIT {limit}"
    return pd.read_sql(query, engine)

def get_table_info(table_name):
    """Retorna informações sobre as colunas de uma tabela."""
    engine = get_engine()
    query = f"""
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = '{table_name}' AND table_schema = 'public'
    """
    return pd.read_sql(query, engine)
