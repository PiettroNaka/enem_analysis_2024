# Análise Exploratória ENEM 2024 - Big Data IESB

## Descrição

Aplicação Streamlit para análise exploratória completa dos dados do ENEM 2024, armazenados no Big Data-IESB. O projeto inclui:

1. **Análise Exploratória**: Distribuição de frequências, gráficos e correlações
2. **Amostragem Estatística**: Três tipos de amostragem (Aleatória Simples, Sistemática e Estratificada)
3. **Comparação de Amostras**: Validação das amostras contra a população
4. **Relatório Técnico**: Documento completo em LaTeX

## Estrutura do Projeto

```
enem_streamlit/
├── app.py                  # Aplicação principal Streamlit
├── requirements.txt        # Dependências Python
├── README.md              # Este arquivo
├── utils/
│   ├── database.py        # Módulo de conexão com banco de dados
│   └── statistics.py      # Módulo de análise estatística e amostragem
├── pages/                 # Páginas adicionais (futuro)
├── data/                  # Dados locais (futuro)
└── reports/               # Relatórios gerados
```

## Instalação

### Pré-requisitos

- Python 3.8+
- pip ou conda

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/enem_analysis_2024.git
cd enem_analysis_2024
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

Execute a aplicação Streamlit:

```bash
streamlit run app.py
```

A aplicação abrirá no navegador em `http://localhost:8501`

## Funcionalidades

### 📊 Início
- Visão geral do projeto
- Informações sobre as tabelas de dados
- Instruções de uso

### 📈 Análise Exploratória
- Distribuição de frequência para variáveis qualitativas
- Gráficos de barras
- Estatísticas descritivas para variáveis quantitativas
- Histogramas e box plots
- Matriz de correlação entre notas

### 🎲 Amostragem
- Cálculo automático do tamanho da amostra
- Geração de três tipos de amostragem:
  - Amostra Aleatória Simples
  - Amostra Sistemática
  - Amostra Estratificada

### 📋 Comparação de Amostras
- Comparação de estatísticas entre amostras e população
- Visualização gráfica das comparações

### 📄 Relatório
- Acesso ao relatório técnico completo em PDF

## Dados

### Fonte
- **Servidor**: bigdata.dataiesb.com
- **Banco de Dados**: iesb
- **Schema**: public

### Tabelas
1. **ed_enem_2024_participantes**: Informações dos participantes
2. **ed_enem_2024_resultados**: Resultados das provas

## Variáveis Analisadas

### Qualitativas
- Sexo (tp_sexo)
- Estado Civil (tp_estado_civil)
- Cor/Raça (tp_cor_raca)
- Nacionalidade (tp_nacionalidade)
- Dependência Administrativa da Escola (tp_dependencia_adm_esc)

### Quantitativas
- Nota Ciências da Natureza (nota_cn_ciencias_da_natureza)
- Nota Ciências Humanas (nota_ch_ciencias_humanas)
- Nota Linguagens e Códigos (nota_lc_linguagens_e_codigos)
- Nota Matemática (nota_mt_matematica)
- Nota Redação (nota_redacao)
- Nota Média (nota_media_5_notas)

## Métodos Estatísticos

### Amostragem
1. **Amostra Aleatória Simples**: Cada elemento tem igual probabilidade de seleção
2. **Amostra Sistemática**: Seleção a cada k-ésimo elemento
3. **Amostra Estratificada**: Divisão em estratos (por sexo) e amostragem proporcional

### Cálculo do Tamanho da Amostra
- Fórmula de Cochran com ajuste para população finita
- Nível de confiança: 95% (padrão)
- Margem de erro: 5% (padrão)

## Tecnologias Utilizadas

- **Streamlit**: Framework web para aplicações de dados
- **Pandas**: Manipulação e análise de dados
- **NumPy**: Computação numérica
- **Matplotlib/Seaborn**: Visualização de dados
- **SciPy**: Cálculos estatísticos
- **SQLAlchemy**: ORM para banco de dados
- **PostgreSQL**: Banco de dados

## Autor

Desenvolvido como trabalho acadêmico para a disciplina de Estatística - Big Data IESB

## Licença

MIT License

## Contato

Para dúvidas ou sugestões, entre em contato através do GitHub.
