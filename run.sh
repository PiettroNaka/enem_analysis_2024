#!/bin/bash

# Script para executar a aplicação Streamlit

echo "🚀 Iniciando Análise ENEM 2024 - Streamlit"
echo "==========================================="
echo ""

# Verifica se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativa o ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Instala dependências
echo "📚 Instalando dependências..."
pip install -q -r requirements.txt

# Executa a aplicação
echo ""
echo "✅ Iniciando aplicação Streamlit..."
echo "📍 Acesse: http://localhost:8501"
echo ""

streamlit run app.py
