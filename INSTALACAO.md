# Guia de Instalação e Uso

## Análise Exploratória ENEM 2024 - Big Data IESB

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (para controle de versão)
- Acesso ao banco de dados Big Data-IESB

### Instalação Rápida

#### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/enem_analysis_2024.git
cd enem_analysis_2024
```

#### 2. Execute o script de instalação

```bash
chmod +x run.sh
./run.sh
```

O script irá:
- Criar um ambiente virtual Python
- Instalar todas as dependências
- Iniciar a aplicação Streamlit

#### 3. Acesse a aplicação

Abra seu navegador e acesse: **http://localhost:8501**

### Instalação Manual

#### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/enem_analysis_2024.git
cd enem_analysis_2024
```

#### 2. Crie um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4. Execute a aplicação

```bash
streamlit run app.py
```

### Estrutura do Projeto

```
enem_analysis_2024/
├── app.py                      # Aplicação principal Streamlit
├── requirements.txt            # Dependências Python
├── run.sh                      # Script de execução
├── README.md                   # Documentação geral
├── INSTALACAO.md              # Este arquivo
├── .gitignore                 # Arquivo de configuração Git
├── .streamlit/
│   └── config.toml            # Configuração Streamlit
├── utils/
│   ├── database.py            # Módulo de conexão com BD
│   └── statistics.py          # Módulo de análise estatística
├── pages/                     # Páginas adicionais (futuro)
├── data/                      # Dados locais (futuro)
└── reports/
    ├── relatorio_tecnico.md   # Relatório em Markdown
    ├── relatorio_tecnico.pdf  # Relatório em PDF
    └── relatorio_tecnico.tex  # Relatório em LaTeX
```

### Configuração do Banco de Dados

As credenciais do banco de dados estão configuradas no arquivo `utils/database.py`:

```python
DB_USER = "data_iesb"
DB_PASS = "iesb"
DB_HOST = "bigdata.dataiesb.com"
DB_PORT = "5432"
DB_NAME = "iesb"
```

**Nota**: Essas credenciais são apenas para leitura dos dados públicos.

### Funcionalidades Principais

#### 📊 Página Inicial
- Visão geral do projeto
- Informações sobre as tabelas
- Instruções de uso

#### 📈 Análise Exploratória
- Distribuição de frequência
- Gráficos de barras
- Estatísticas descritivas
- Histogramas e box plots
- Matriz de correlação

#### 🎲 Amostragem
- Cálculo automático do tamanho da amostra
- Geração de três tipos de amostragem:
  - Amostra Aleatória Simples
  - Amostra Sistemática
  - Amostra Estratificada

#### 📋 Comparação de Amostras
- Comparação de estatísticas
- Visualização gráfica

#### 📄 Relatório
- Acesso ao relatório técnico completo

### Troubleshooting

#### Erro: "ModuleNotFoundError: No module named 'streamlit'"

**Solução**: Instale as dependências
```bash
pip install -r requirements.txt
```

#### Erro: "Connection refused" ao conectar ao banco de dados

**Solução**: Verifique:
1. Conexão com a internet
2. Credenciais do banco de dados
3. Se o servidor bigdata.dataiesb.com está acessível

#### Erro: "Permission denied" ao executar run.sh

**Solução**: Torne o script executável
```bash
chmod +x run.sh
```

### Performance

Para melhor performance ao trabalhar com grandes volumes de dados:

1. **Limite de dados**: A aplicação carrega até 500.000 registros por padrão
2. **Cache**: Streamlit utiliza cache automático para otimizar requisições
3. **Índices**: O banco de dados possui índices otimizados

### Requisitos de Sistema

- **RAM**: Mínimo 4GB (recomendado 8GB)
- **Armazenamento**: 500MB para o projeto
- **Processador**: Dual-core (recomendado quad-core)
- **Conexão**: Internet de banda larga

### Desenvolvimento

Para contribuir com melhorias:

1. Crie uma branch para sua feature
```bash
git checkout -b feature/nova-funcionalidade
```

2. Faça suas alterações e commits
```bash
git add .
git commit -m "Descrição da alteração"
```

3. Push para a branch
```bash
git push origin feature/nova-funcionalidade
```

4. Abra um Pull Request

### Suporte

Para dúvidas ou problemas, consulte:
- [Documentação Streamlit](https://docs.streamlit.io)
- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [Big Data IESB](https://bigdata.dataiesb.com)

### Licença

MIT License - Veja LICENSE.md para detalhes

---

**Última atualização**: Abril de 2024
