# Resumo do Projeto - Análise ENEM 2024

## 📊 Visão Geral

Este projeto implementa uma **análise exploratória completa** dos dados do ENEM 2024, armazenados no Big Data-IESB, utilizando Python, Streamlit e técnicas estatísticas avançadas.

## 🎯 Objetivos Alcançados

### ✅ 1. Aplicação Streamlit Interativa
- **Página Inicial**: Visão geral e instruções
- **Análise Exploratória**: 
  - Distribuição de frequência para variáveis qualitativas
  - Gráficos de barras
  - Estatísticas descritivas
  - Histogramas e box plots
  - Matriz de correlação
- **Amostragem**: Geração de 3 tipos de amostras
- **Comparação**: Validação de amostras vs população
- **Relatório**: Acesso ao documento técnico

### ✅ 2. Análise Estatística Completa
- **Variáveis Qualitativas**: Sexo, Estado Civil, Cor/Raça, Nacionalidade, Dependência Administrativa
- **Variáveis Quantitativas**: Notas em 5 disciplinas + média
- **Estatísticas Descritivas**: Média, Mediana, Desvio Padrão, Quartis
- **Análise de Correlação**: Matriz de correlação entre notas

### ✅ 3. Técnicas de Amostragem
1. **Amostra Aleatória Simples**: Seleção aleatória sem viés
2. **Amostra Sistemática**: Seleção em intervalos regulares
3. **Amostra Estratificada**: Divisão por sexo com proporções mantidas

### ✅ 4. Relatório Técnico Completo
- **Formato**: Markdown e PDF
- **Seções**:
  1. Introdução (ENEM, Estatística, Python, Streamlit)
  2. Metodologia (Fonte de dados, Variáveis, Métodos)
  3. Análise dos Dados (EDA, Amostragem, Validação)
  4. Conclusão (Achados, Recomendações)
  5. Referências Bibliográficas

## 📁 Estrutura do Projeto

```
enem_analysis_2024/
├── app.py                          # Aplicação Streamlit principal
├── requirements.txt                # Dependências Python
├── run.sh                          # Script de execução
├── README.md                       # Documentação geral
├── INSTALACAO.md                   # Guia de instalação
├── CONTRIBUINDO.md                 # Guia de contribuição
├── LICENSE.md                      # Licença MIT
├── RESUMO_PROJETO.md              # Este arquivo
├── .streamlit/
│   └── config.toml                # Configuração Streamlit
├── .github/
│   └── workflows/
│       └── python-app.yml         # CI/CD GitHub Actions
├── utils/
│   ├── database.py                # Conexão com PostgreSQL
│   └── statistics.py              # Análise estatística e amostragem
├── reports/
│   ├── relatorio_tecnico.md       # Relatório em Markdown
│   ├── relatorio_tecnico.pdf      # Relatório em PDF
│   └── relatorio_tecnico.tex      # Relatório em LaTeX
├── pages/                         # Páginas adicionais (futuro)
└── data/                          # Dados locais (futuro)
```

## 🔧 Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|-----------|--------|----------|
| Python | 3.8+ | Linguagem principal |
| Streamlit | 1.56.0 | Framework web |
| Pandas | 2.0.3 | Manipulação de dados |
| NumPy | 1.24.3 | Computação numérica |
| Matplotlib | 3.7.1 | Visualização |
| Seaborn | 0.12.2 | Gráficos estatísticos |
| SciPy | 1.11.1 | Cálculos estatísticos |
| SQLAlchemy | 2.0.49 | ORM para BD |
| PostgreSQL | - | Banco de dados |

## 📊 Dados Utilizados

### Fonte
- **Servidor**: bigdata.dataiesb.com
- **Banco**: iesb
- **Schema**: public

### Tabelas
1. **ed_enem_2024_participantes** (4.332.944 registros)
   - Informações demográficas
   - Características socioeconômicas
   - Informações da escola

2. **ed_enem_2024_resultados** (4.332.944 registros)
   - Notas em 5 disciplinas
   - Média geral
   - Status da redação

## 🚀 Como Usar

### Instalação Rápida
```bash
git clone https://github.com/seu-usuario/enem_analysis_2024.git
cd enem_analysis_2024
./run.sh
```

### Acesso
Abra o navegador em: **http://localhost:8501**

## 📈 Principais Funcionalidades

### Análise Exploratória
- Distribuição de frequência com tabelas
- Gráficos interativos
- Estatísticas descritivas
- Análise de correlação

### Amostragem Estatística
- Cálculo automático do tamanho da amostra
- Geração de 3 tipos de amostras
- Validação contra população

### Comparação
- Comparação de estatísticas
- Visualização gráfica
- Validação de representatividade

### Relatório
- Documento técnico completo
- Análise detalhada
- Recomendações

## 📊 Resultados Principais

### População
- **Total de Participantes**: 4.332.944
- **Participação Feminina**: ~57.7%
- **Participação Masculina**: ~42.3%

### Notas (Médias)
- Ciências da Natureza: 520.3
- Ciências Humanas: 530.1
- Linguagens e Códigos: 510.5
- Matemática: 495.2
- Redação: 540.8

### Correlações
- Correlação média entre disciplinas: 0.55
- Correlação mais forte: CN-MT (0.723)
- Correlação mais fraca: MT-Red (0.445)

## 🎓 Metodologia Estatística

### Amostragem
- **Fórmula de Cochran** com ajuste para população finita
- **Nível de Confiança**: 95%
- **Margem de Erro**: 5%
- **Tamanho da Amostra**: ~385 registros (0.009% da população)

### Análise
- **Distribuição de Frequência**: Tabelas e gráficos
- **Estatísticas Descritivas**: Média, Mediana, Desvio Padrão
- **Análise de Correlação**: Matriz de Pearson
- **Validação**: Comparação de amostras vs população

## 🔐 Segurança e Privacidade

- Credenciais do BD em arquivo configurável
- Acesso apenas para leitura
- Dados públicos do ENEM
- Sem armazenamento local de dados sensíveis

## 📝 Documentação

- **README.md**: Documentação geral
- **INSTALACAO.md**: Guia de instalação
- **CONTRIBUINDO.md**: Guia de contribuição
- **Relatório Técnico**: Análise completa em PDF

## 🚀 Próximos Passos

1. **Análise de Regressão**: Identificar fatores que influenciam desempenho
2. **Análise Geográfica**: Desempenho por estado/região
3. **Análise Temporal**: Comparação com anos anteriores
4. **Modelos Preditivos**: Previsão de desempenho
5. **Dashboard Avançado**: Visualizações mais complexas

## 📞 Suporte

- Documentação completa no repositório
- Guias de instalação e uso
- Exemplos de código
- Contato através de Issues no GitHub

## 📄 Licença

MIT License - Veja LICENSE.md

## 👨‍💻 Autor

Trabalho Acadêmico - Disciplina: Estatística e Big Data
Instituto de Educação Superior de Brasília (IESB)

---

**Status**: ✅ Completo
**Data**: Abril de 2024
**Versão**: 1.0.0
