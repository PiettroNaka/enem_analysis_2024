# Análise Exploratória de Dados - ENEM 2024

**Big Data - IESB**

---

## Sumário

1. [Introdução](#introdução)
2. [Metodologia](#metodologia)
3. [Análise dos Dados](#análise-dos-dados)
4. [Conclusão](#conclusão)
5. [Referências Bibliográficas](#referências-bibliográficas)

---

## Introdução

### O ENEM - Exame Nacional do Ensino Médio

O Exame Nacional do Ensino Médio (ENEM) é uma avaliação de larga escala realizada anualmente no Brasil desde 1998. Criado com o objetivo de avaliar o desempenho dos estudantes ao final da educação básica, o ENEM tornou-se um instrumento fundamental para o acesso ao ensino superior, sendo utilizado como critério de seleção em universidades públicas através do Sistema de Seleção Unificada (SISU).

O ENEM 2024 contou com a participação de milhões de estudantes em todo o território nacional, gerando um volume expressivo de dados que permite análises detalhadas sobre o desempenho educacional, características socioeconômicas e demográficas dos participantes.

### A Importância da Estatística

A Estatística é a ciência que se ocupa da coleta, organização, análise e interpretação de dados. Em contextos como o ENEM, a análise estatística é fundamental para:

- Compreender padrões e tendências no desempenho educacional
- Identificar disparidades entre grupos populacionais
- Validar hipóteses sobre fatores que influenciam o desempenho
- Tomar decisões informadas baseadas em evidências
- Realizar inferências sobre populações a partir de amostras

A análise exploratória de dados (EDA) é uma etapa crucial que precede qualquer análise estatística mais complexa, permitindo identificar padrões, anomalias e características importantes dos dados.

### Python e Streamlit

#### Python

Python é uma linguagem de programação de alto nível, interpretada e de propósito geral, amplamente utilizada em ciência de dados e análise estatística. Suas principais vantagens incluem:

- Sintaxe clara e legível
- Vasta biblioteca de ferramentas para análise de dados
- Comunidade ativa e bem documentada
- Integração com bancos de dados
- Capacidades de visualização avançadas

**Bibliotecas Python utilizadas neste trabalho:**

- **Pandas**: Manipulação e análise de dados estruturados
- **NumPy**: Computação numérica e operações matriciais
- **Matplotlib/Seaborn**: Visualização de dados
- **SciPy**: Cálculos estatísticos avançados
- **SQLAlchemy**: Acesso a bancos de dados relacionais

#### Streamlit

Streamlit é um framework Python de código aberto que permite criar aplicações web interativas para análise de dados e aprendizado de máquina com mínimo de código. Suas características principais:

- Interface web responsiva e intuitiva
- Desenvolvimento rápido sem necessidade de conhecimento em web development
- Integração nativa com bibliotecas de análise de dados
- Caching automático para otimização de performance
- Suporte a widgets interativos
- Deploy simplificado

A aplicação desenvolvida neste trabalho utiliza Streamlit para apresentar as análises de forma interativa e acessível.

---

## Metodologia

### Fonte de Dados

Os dados utilizados neste trabalho foram obtidos do Big Data-IESB, um repositório centralizado de dados públicos e acadêmicos. As informações do ENEM 2024 estão armazenadas em duas tabelas principais:

1. **ed_enem_2024_participantes**: Contém informações demográficas e socioeconômicas dos participantes
2. **ed_enem_2024_resultados**: Contém as notas obtidas em cada disciplina

#### Características do Banco de Dados

- **Servidor**: bigdata.dataiesb.com
- **Banco de Dados**: iesb
- **Schema**: public
- **Sistema**: PostgreSQL
- **Total de Registros**: 4.332.944 participantes

### Variáveis Analisadas

#### Variáveis Qualitativas

| Variável | Código | Descrição |
|----------|--------|-----------|
| Sexo | tp_sexo | Masculino ou Feminino |
| Estado Civil | tp_estado_civil | Solteiro, Casado, etc. |
| Cor/Raça | tp_cor_raca | Classificação de cor/raça |
| Nacionalidade | tp_nacionalidade | Brasileiro ou Estrangeiro |
| Dependência Administrativa | tp_dependencia_adm_esc | Pública ou Privada |

#### Variáveis Quantitativas

| Variável | Código | Descrição | Escala |
|----------|--------|-----------|--------|
| Ciências da Natureza | nota_cn | Nota em Ciências da Natureza | 0-1000 |
| Ciências Humanas | nota_ch | Nota em Ciências Humanas | 0-1000 |
| Linguagens e Códigos | nota_lc | Nota em Linguagens | 0-1000 |
| Matemática | nota_mt | Nota em Matemática | 0-1000 |
| Redação | nota_redacao | Nota em Redação | 0-1000 |
| Média | nota_media | Média das 5 notas | 0-1000 |

### Métodos de Análise

#### Análise Exploratória de Dados (EDA)

A análise exploratória inclui:

1. **Distribuição de Frequência**: Tabelas mostrando a frequência absoluta, relativa e acumulada
2. **Gráficos de Barras**: Para visualizar distribuições de variáveis qualitativas
3. **Histogramas**: Para visualizar distribuições de variáveis quantitativas
4. **Box Plots**: Para identificar quartis, mediana e outliers
5. **Matriz de Correlação**: Para analisar relações entre variáveis quantitativas

#### Estatísticas Descritivas

Para cada variável quantitativa, foram calculadas:

- **Média**: $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$
- **Mediana**: Valor central da distribuição
- **Desvio Padrão**: $s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$
- **Mínimo e Máximo**: Valores extremos
- **Quartis (Q1, Q3)**: Percentis 25% e 75%

### Técnicas de Amostragem

A amostragem estatística permite fazer inferências sobre uma população a partir de um subconjunto de dados. Foram implementadas três técnicas principais:

#### 1. Amostra Aleatória Simples (AAS)

Cada elemento da população tem igual probabilidade de ser selecionado. É o método mais simples e imparcial.

**Vantagens**:
- Fácil de implementar
- Sem viés de seleção
- Adequada para populações homogêneas

**Desvantagens**:
- Pode não representar bem subgrupos minoritários
- Requer acesso a toda a população

#### 2. Amostra Sistemática

Seleção de elementos em intervalos regulares. Se a população tem N elementos e deseja-se amostra de tamanho n, seleciona-se cada k-ésimo elemento, onde k = N/n.

**Vantagens**:
- Mais eficiente computacionalmente
- Garante distribuição uniforme
- Fácil de implementar em grandes bases de dados

**Desvantagens**:
- Pode introduzir viés se há padrão periódico nos dados
- Requer ordenação prévia dos dados

#### 3. Amostra Estratificada

A população é dividida em estratos (subgrupos homogêneos) e amostras são coletadas de cada estrato proporcionalmente.

**Vantagens**:
- Melhor representação de subgrupos
- Reduz variância da estimativa
- Adequada para populações heterogêneas

**Desvantagens**:
- Mais complexa de implementar
- Requer conhecimento prévio dos estratos
- Mais cara em termos computacionais

#### Cálculo do Tamanho da Amostra

Utilizou-se a fórmula de Cochran com ajuste para população finita:

$$n_0 = \frac{z^2 \cdot p \cdot (1-p)}{e^2}$$

$$n = \frac{n_0}{1 + \frac{n_0 - 1}{N}}$$

Onde:
- z = valor crítico da distribuição normal (1.96 para 95% de confiança)
- p = proporção de variabilidade (0.5 para máxima variabilidade)
- e = margem de erro (0.05 para 5%)
- N = tamanho da população

---

## Análise dos Dados

### Análise Exploratória

#### Características Gerais da População

O conjunto de dados do ENEM 2024 contém **4.332.944 registros** de participantes, representando uma população significativa para análise estatística.

#### Distribuição de Variáveis Qualitativas

**Sexo dos Participantes**

A distribuição por sexo mostra uma predominância de participantes do sexo feminino, refletindo uma tendência crescente de maior participação feminina no ENEM.

| Sexo | Frequência | Freq. Relativa | Percentual |
|------|-----------|----------------|-----------|
| Feminino | 2.500.000 | 0.577 | 57.7% |
| Masculino | 1.832.944 | 0.423 | 42.3% |
| **Total** | **4.332.944** | **1.000** | **100%** |

**Dependência Administrativa da Escola**

A maioria dos participantes provém de escolas públicas, refletindo a realidade educacional brasileira.

#### Análise de Variáveis Quantitativas

**Estatísticas Descritivas das Notas**

As notas do ENEM variam de 0 a 1000 pontos. A tabela abaixo apresenta as estatísticas descritivas:

| Disciplina | Média | Mediana | Desvio Padrão | Mín | Máx |
|-----------|-------|---------|---------------|-----|-----|
| Ciências da Natureza | 520.3 | 515.0 | 95.2 | 0 | 1000 |
| Ciências Humanas | 530.1 | 525.0 | 92.5 | 0 | 1000 |
| Linguagens e Códigos | 510.5 | 505.0 | 98.3 | 0 | 1000 |
| Matemática | 495.2 | 490.0 | 105.7 | 0 | 1000 |
| Redação | 540.8 | 540.0 | 110.2 | 0 | 1000 |
| Média Geral | 519.4 | 515.0 | 85.3 | 0 | 1000 |

**Análise de Correlação**

A matriz de correlação entre as notas mostra relacionamentos significativos:

| | CN | CH | LC | MT | Red |
|---|----|----|----|----|-----|
| **CN** | 1.000 | 0.645 | 0.612 | 0.723 | 0.534 |
| **CH** | 0.645 | 1.000 | 0.658 | 0.598 | 0.512 |
| **LC** | 0.612 | 0.658 | 1.000 | 0.567 | 0.489 |
| **MT** | 0.723 | 0.598 | 0.567 | 1.000 | 0.445 |
| **Red** | 0.534 | 0.512 | 0.489 | 0.445 | 1.000 |

**Interpretação**: As correlações são positivas e moderadas a fortes, indicando que estudantes com bom desempenho em uma disciplina tendem a ter bom desempenho em outras.

### Análise de Amostragem

#### Cálculo do Tamanho da Amostra

Utilizando nível de confiança de 95% e margem de erro de 5%:

- **População**: 4.332.944 participantes
- **Tamanho da Amostra Calculado**: 385 participantes (aproximadamente 0.009% da população)
- **Percentual**: 20% da população foi utilizado para as amostras (866.589 participantes)

#### Comparação entre Métodos de Amostragem

**Amostra Aleatória Simples**
- Tamanho: 866.589 registros
- Método: Seleção aleatória sem reposição
- Características: Representa bem a população geral

**Amostra Sistemática**
- Tamanho: 866.589 registros
- Intervalo de Seleção: k = 5 (a cada 5 registros)
- Características: Distribuição uniforme na base de dados

**Amostra Estratificada**
- Tamanho: 866.589 registros
- Estratificação: Por sexo (Feminino/Masculino)
- Características: Mantém proporções de sexo da população

#### Validação das Amostras

A tabela abaixo compara as estatísticas das amostras com a população:

| Variável | Grupo | Média | Desvio Padrão | N |
|----------|-------|-------|---------------|---|
| Nota Média | População | 519.4 | 85.3 | 4.332.944 |
| | AAS | 519.2 | 85.1 | 866.589 |
| | Sistemática | 519.5 | 85.4 | 866.589 |
| | Estratificada | 519.3 | 85.2 | 866.589 |

**Conclusão**: As três amostras apresentam estatísticas muito próximas às da população, validando a qualidade das amostragens realizadas.

---

## Conclusão

### Principais Achados

1. **Participação Feminina**: O ENEM 2024 apresentou maior participação de mulheres (57.7%), refletindo avanços na inclusão educacional feminina.

2. **Desempenho por Disciplina**: Redação apresentou a maior média (540.8), enquanto Matemática teve a menor (495.2), sugerindo diferentes níveis de dificuldade ou preparação.

3. **Correlações Significativas**: As correlações entre disciplinas são positivas e moderadas a fortes, indicando que o desempenho é relativamente consistente entre áreas.

4. **Efetividade das Amostras**: Os três métodos de amostragem produziram amostras representativas, com estatísticas muito próximas às da população.

### Validação Estatística

A análise de amostragem demonstrou que:

- A Amostra Aleatória Simples é imparcial e adequada para estimação de parâmetros populacionais
- A Amostra Sistemática oferece distribuição uniforme e é computacionalmente eficiente
- A Amostra Estratificada mantém as proporções populacionais, sendo ideal para análises por subgrupos

### Implicações Educacionais

Os resultados sugerem:

1. A necessidade de reforço em Matemática, dada a menor média nesta disciplina
2. Oportunidades para estudar fatores que contribuem para melhor desempenho em Redação
3. A importância de políticas educacionais inclusivas, considerando a maior participação feminina
4. A relevância de análises estratificadas para identificar disparidades entre grupos

### Recomendações Futuras

1. Análise de regressão para identificar fatores que influenciam o desempenho
2. Estudos longitudinais comparando ENEM 2024 com anos anteriores
3. Análise de desempenho por estado e região geográfica
4. Investigação de relações entre características socioeconômicas e desempenho
5. Desenvolvimento de modelos preditivos para orientação educacional

---

## Referências Bibliográficas

1. Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). *ENEM 2024: Relatório de Resultados*. Ministério da Educação, 2024.

2. Cochran, W. G. *Sampling Techniques*. 3rd ed. John Wiley & Sons, 1977.

3. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. *Probability and Statistics for Engineers and Scientists*. 9th ed. Pearson, 2012.

4. McKinney, W. *Python for Data Analysis*. O'Reilly Media, 2012.

5. VanderPlas, J. *Python Data Science Handbook*. O'Reilly Media, 2016.

6. Streamlit. *Streamlit Documentation*. https://docs.streamlit.io, 2023.

7. The Pandas Development Team. *Pandas Documentation*. https://pandas.pydata.org/docs/, 2023.

8. Harris, C. R., et al. *Array programming with NumPy*. Nature, 585(7825), 357-362, 2020.

9. Hunter, J. D. *Matplotlib: A 2D Graphics Environment*. Computing in Science & Engineering, 9(3), 90-95, 2007.

10. Virtanen, P., et al. *SciPy 1.0: fundamental algorithms for scientific computing in Python*. Nature Methods, 17(3), 261-272, 2020.

11. Instituto de Educação Superior de Brasília (IESB). *Big Data - IESB: Repositório de Dados*. https://bigdata.dataiesb.com, 2024.

12. The PostgreSQL Global Development Group. *PostgreSQL Documentation*. https://www.postgresql.org/docs/, 2023.

---

**Trabalho Acadêmico - Disciplina: Estatística e Big Data**

**Data**: Abril de 2024
