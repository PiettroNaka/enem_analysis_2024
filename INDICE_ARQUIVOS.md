# Índice de Arquivos do Projeto

## 📋 Estrutura Completa

### 📄 Arquivos de Documentação

| Arquivo | Descrição |
|---------|-----------|
| `README.md` | Documentação principal do projeto |
| `INSTALACAO.md` | Guia passo a passo de instalação |
| `CONTRIBUINDO.md` | Diretrizes para contribuições |
| `PUBLICACAO_GITHUB.md` | Como publicar no GitHub |
| `RESUMO_PROJETO.md` | Resumo executivo do projeto |
| `LICENSE.md` | Licença MIT |
| `INDICE_ARQUIVOS.md` | Este arquivo |

### 🐍 Arquivos Python

| Arquivo | Descrição | Linhas |
|---------|-----------|--------|
| `app.py` | Aplicação Streamlit principal | ~400 |
| `utils/database.py` | Módulo de conexão com PostgreSQL | ~50 |
| `utils/statistics.py` | Módulo de análise estatística | ~250 |

### 📦 Arquivos de Configuração

| Arquivo | Descrição |
|---------|-----------|
| `requirements.txt` | Dependências Python |
| `run.sh` | Script de execução |
| `.gitignore` | Configuração Git |
| `.streamlit/config.toml` | Configuração Streamlit |
| `.github/workflows/python-app.yml` | Workflow CI/CD |

### 📊 Relatórios

| Arquivo | Descrição | Tamanho |
|---------|-----------|--------|
| `reports/relatorio_tecnico.md` | Relatório em Markdown | ~20 KB |
| `reports/relatorio_tecnico.pdf` | Relatório em PDF | ~128 KB |
| `reports/relatorio_tecnico.tex` | Relatório em LaTeX | ~22 KB |

### 📁 Diretórios

| Diretório | Propósito |
|-----------|----------|
| `utils/` | Módulos Python utilitários |
| `reports/` | Relatórios e documentação técnica |
| `pages/` | Páginas adicionais Streamlit (futuro) |
| `data/` | Dados locais (futuro) |
| `.github/workflows/` | Workflows de CI/CD |
| `.streamlit/` | Configuração Streamlit |

## 📊 Estatísticas do Projeto

### Contagem de Linhas de Código

```
app.py                  ~400 linhas
utils/database.py       ~50 linhas
utils/statistics.py     ~250 linhas
─────────────────────────────────
Total Python            ~700 linhas
```

### Tamanho dos Arquivos

```
app.py                  ~15 KB
utils/database.py       ~2 KB
utils/statistics.py     ~8 KB
reports/relatorio_tecnico.pdf   ~128 KB
─────────────────────────────────
Total                   ~153 KB
```

### Arquivos Criados

- **Total de Arquivos**: 20+
- **Arquivos Python**: 3
- **Arquivos Markdown**: 7
- **Arquivos de Configuração**: 4
- **Relatórios**: 3

## 🔍 Descrição Detalhada dos Arquivos

### app.py
Aplicação Streamlit principal com 5 páginas:
- 📊 Início
- 📈 Análise Exploratória
- 🎲 Amostragem
- 📋 Comparação de Amostras
- 📄 Relatório

### utils/database.py
Módulo para conexão com PostgreSQL:
- `get_engine()`: Cria engine de conexão
- `load_participantes()`: Carrega dados de participantes
- `load_resultados()`: Carrega dados de resultados
- `load_combined_data()`: Carrega dados combinados
- `get_table_info()`: Obtém informações das tabelas

### utils/statistics.py
Módulo de análise estatística:
- `SamplingAnalysis`: Classe para amostragem
- `calculate_frequency_distribution()`: Distribuição de frequência
- `identify_variable_types()`: Identifica tipos de variáveis

### requirements.txt
Dependências do projeto:
- streamlit==1.56.0
- pandas==2.0.3
- numpy==1.24.3
- matplotlib==3.7.1
- seaborn==0.12.2
- scipy==1.11.1
- sqlalchemy==2.0.49
- psycopg2-binary==2.9.11
- plotly==5.14.0

### run.sh
Script de execução que:
1. Cria ambiente virtual
2. Instala dependências
3. Executa aplicação Streamlit

### Relatório Técnico
Documento completo com:
1. Introdução (ENEM, Estatística, Python, Streamlit)
2. Metodologia (Dados, Variáveis, Métodos)
3. Análise (EDA, Amostragem, Validação)
4. Conclusão (Achados, Recomendações)
5. Referências Bibliográficas

## 🎯 Arquivos por Funcionalidade

### Análise Exploratória
- `app.py` (página "Análise Exploratória")
- `utils/statistics.py` (função `calculate_frequency_distribution`)
- `utils/database.py` (funções de carregamento)

### Amostragem
- `app.py` (página "Amostragem")
- `utils/statistics.py` (classe `SamplingAnalysis`)

### Comparação
- `app.py` (página "Comparação de Amostras")
- `utils/statistics.py` (método `compare_samples`)

### Relatório
- `reports/relatorio_tecnico.pdf`
- `reports/relatorio_tecnico.md`
- `reports/relatorio_tecnico.tex`

## 📝 Fluxo de Dados

```
Big Data IESB (PostgreSQL)
        ↓
utils/database.py
        ↓
app.py (Streamlit)
        ↓
utils/statistics.py
        ↓
Visualizações e Relatórios
```

## 🔐 Segurança

- Credenciais em `utils/database.py` (apenas leitura)
- Sem armazenamento local de dados sensíveis
- Acesso apenas a dados públicos do ENEM

## 📦 Distribuição

### Arquivo Compactado
- `enem_analysis_2024.tar.gz` (~267 KB)
- Contém todo o projeto pronto para uso

### Como Usar o Arquivo Compactado
```bash
tar -xzf enem_analysis_2024.tar.gz
cd enem_streamlit
./run.sh
```

## 🚀 Próximas Adições

- [ ] Testes unitários (tests/)
- [ ] Dados de exemplo (data/)
- [ ] Páginas adicionais (pages/)
- [ ] Configuração de ambiente (.env.example)
- [ ] Docker (Dockerfile, docker-compose.yml)
- [ ] Documentação API

---

**Última atualização**: Abril de 2024
**Versão**: 1.0.0
