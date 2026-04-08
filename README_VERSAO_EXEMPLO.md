# 📊 Análise ENEM 2024 - Versão com Dados de Exemplo

## ✅ Versão Funcional e Testada

Esta é a versão **funcional e testada** da aplicação Streamlit para análise do ENEM 2024. Ela usa **dados de exemplo** para demonstração, eliminando dependências de conexão com banco de dados.

---

## 🚀 Como Usar

### Opção 1: Online (Streamlit Cloud)
Acesse diretamente: **https://enem-analysis-2024.streamlit.app**

### Opção 2: Localmente
```bash
# Clone o repositório
git clone https://github.com/PiettroNaka/enem_analysis_2024.git
cd enem_analysis_2024

# Execute o script
chmod +x run.sh
./run.sh

# Ou manualmente
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 📋 Funcionalidades

### 📊 Página Inicial
- Visão geral do projeto
- Dados de exemplo
- Métricas principais

### 📈 Análise Exploratória
- **Variáveis Qualitativas**: Distribuição de frequência e gráficos
- **Variáveis Quantitativas**: Estatísticas descritivas e histogramas
- **Correlação**: Matriz de correlação entre notas

### 🎲 Amostragem Estatística
- Cálculo automático do tamanho da amostra
- Três tipos de amostragem:
  - Amostra Aleatória Simples
  - Amostra Sistemática
  - Amostra Estratificada

### 📋 Comparação de Amostras
- Comparação de estatísticas entre amostras e população
- Validação de representatividade

### 📄 Relatório Técnico
- Download do relatório em PDF
- Análise completa e conclusões

---

## 📊 Dados de Exemplo

A aplicação usa dados simulados com as seguintes características:

| Variável | Tipo | Descrição |
|----------|------|-----------|
| Sexo | Qualitativa | Masculino / Feminino |
| Estado Civil | Qualitativa | Solteiro / Casado / Viúvo / Divorciado |
| Nota_CN | Quantitativa | Ciências da Natureza (μ=520, σ=80) |
| Nota_CH | Quantitativa | Ciências Humanas (μ=530, σ=75) |
| Nota_LC | Quantitativa | Linguagens e Códigos (μ=510, σ=85) |
| Nota_MT | Quantitativa | Matemática (μ=495, σ=90) |
| Nota_Redacao | Quantitativa | Redação (μ=540, σ=100) |

**Tamanho da População**: 100.000 registros

---

## 🔧 Requisitos

- Python 3.9+
- Streamlit >= 1.28.0
- Pandas >= 2.1.0
- NumPy >= 1.26.0
- Matplotlib >= 3.8.0
- Seaborn >= 0.13.0
- SciPy >= 1.11.0

---

## 📦 Instalação de Dependências

```bash
pip install -r requirements.txt
```

---

## 🎯 Como Usar Cada Página

### 1. Início
- Clique em "Início" no menu lateral
- Visualize dados de exemplo
- Veja as métricas principais

### 2. Análise Exploratória
- Selecione uma variável qualitativa para ver distribuição
- Selecione uma variável quantitativa para ver estatísticas
- Visualize a matriz de correlação

### 3. Amostragem
- Ajuste o nível de confiança (90-99%)
- Ajuste a margem de erro (1-10%)
- Clique em "Gerar Amostras"
- Visualize as três amostras geradas

### 4. Comparação
- Primeiro gere as amostras (página anterior)
- Veja a comparação de estatísticas
- Valide a representatividade das amostras

### 5. Relatório
- Clique em "Baixar Relatório em PDF"
- Salve o arquivo localmente

---

## 🔄 Fluxo de Uso Recomendado

1. **Comece pela página "Início"** para entender o projeto
2. **Explore os dados** na página "Análise Exploratória"
3. **Gere amostras** na página "Amostragem"
4. **Compare as amostras** na página "Comparação"
5. **Consulte o relatório** na página "Relatório"

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Erro: "Port 8501 is already in use"
```bash
streamlit run app.py --server.port 8502
```

### Aplicação lenta
- Reduza o número de registros em `app.py`
- Feche outros aplicativos
- Aumente a RAM disponível

---

## 📝 Notas Importantes

- **Dados de Exemplo**: Os dados são gerados aleatoriamente a cada execução
- **Sem Conexão com BD**: Esta versão não se conecta ao Big Data-IESB
- **Funcionalidade Completa**: Todas as análises funcionam normalmente
- **Reprodutível**: Use `random_state=42` para resultados consistentes

---

## 🔗 Links Úteis

- [Documentação Streamlit](https://docs.streamlit.io)
- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [Documentação SciPy](https://docs.scipy.org/)
- [GitHub Repository](https://github.com/PiettroNaka/enem_analysis_2024)

---

## 📄 Licença

MIT License - Veja LICENSE.md para detalhes

---

## ✅ Status

- **Versão**: 1.0.3
- **Status**: ✅ Funcional e Testado
- **Data**: Abril de 2024
- **Python**: 3.9+
- **Streamlit**: 1.28.0+

---

**Última Atualização**: Abril de 2024

A aplicação está pronta para uso! Teste agora e aproveite a análise completa do ENEM 2024.
