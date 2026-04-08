# 🔧 Troubleshooting - Guia de Resolução de Problemas

## Erros Comuns e Soluções

### 1. Erro: "Falha ao executar 'removeChild' em 'Node'"

**Sintoma**: Aplicação carrega mas exibe erro de DOM no console do navegador

**Causa**: Problema de renderização de gráficos ou componentes Streamlit

**Solução**:
```bash
# Limpe o cache do navegador
# Pressione Ctrl+Shift+Delete (Windows/Linux) ou Cmd+Shift+Delete (Mac)

# Ou recarregue a página
# Pressione Ctrl+F5 (Windows/Linux) ou Cmd+Shift+R (Mac)
```

**Alternativa**: Reinicie a aplicação Streamlit
```bash
# Interrompa a execução (Ctrl+C)
# Execute novamente
streamlit run app.py
```

---

### 2. Erro: "ModuleNotFoundError: No module named 'streamlit'"

**Sintoma**: Erro ao executar `streamlit run app.py`

**Causa**: Dependências não instaladas

**Solução**:
```bash
# Instale as dependências
pip install -r requirements.txt

# Ou use o script de execução
./run.sh
```

---

### 3. Erro: "Connection refused" ao conectar ao banco de dados

**Sintoma**: Erro ao carregar dados: "Connection refused"

**Causa**: Problema de conexão com o servidor Big Data-IESB

**Solução**:
```bash
# Verifique a conexão com a internet
ping bigdata.dataiesb.com

# Verifique as credenciais em utils/database.py
# DB_USER = "data_iesb"
# DB_PASS = "iesb"
# DB_HOST = "bigdata.dataiesb.com"
# DB_PORT = "5432"
# DB_NAME = "iesb"
```

**Se o servidor estiver indisponível**:
- Tente novamente mais tarde
- Verifique se o servidor está online
- Contate o administrador do Big Data-IESB

---

### 4. Erro: "MemoryError" ao carregar dados

**Sintoma**: Erro de memória ao carregar muitos registros

**Causa**: Limite de memória da máquina

**Solução**:
```python
# Reduza o limite de registros em app.py
df = load_combined_data(limit=50000)  # Ao invés de 100000
```

**Ou aumente a memória disponível**:
- Feche outros aplicativos
- Aumente a RAM da máquina
- Use um servidor com mais recursos

---

### 5. Erro: "No module named 'psycopg2'"

**Sintoma**: Erro ao conectar ao PostgreSQL

**Causa**: Driver PostgreSQL não instalado

**Solução**:
```bash
# Instale o driver
pip install psycopg2-binary

# Ou reinstale todas as dependências
pip install -r requirements.txt
```

---

### 6. Erro: "Port 8501 is already in use"

**Sintoma**: Erro ao iniciar Streamlit

**Causa**: Outra instância de Streamlit já está usando a porta

**Solução**:
```bash
# Use uma porta diferente
streamlit run app.py --server.port 8502

# Ou mate o processo anterior
# Windows
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :8501
kill -9 <PID>
```

---

### 7. Erro: "Timeout" ao carregar dados

**Sintoma**: Aplicação fica carregando indefinidamente

**Causa**: Conexão lenta ou servidor lento

**Solução**:
```bash
# Aumente o timeout em utils/database.py
from sqlalchemy import create_engine

engine = create_engine(
    db_url,
    connect_args={'connect_timeout': 30}  # Aumentar timeout
)
```

---

### 8. Erro: "No such file or directory: 'relatorio_tecnico.pdf'"

**Sintoma**: Erro ao tentar baixar o relatório

**Causa**: Arquivo do relatório não encontrado

**Solução**:
```bash
# Verifique se o arquivo existe
ls -la reports/

# Se não existir, regenere o relatório
cd reports/
manus-md-to-pdf relatorio_tecnico.md relatorio_tecnico.pdf
```

---

### 9. Erro: "KeyError" ao acessar coluna

**Sintoma**: Erro ao tentar acessar uma coluna do dataframe

**Causa**: Coluna não existe ou tem nome diferente

**Solução**:
```python
# Verifique os nomes das colunas
print(df.columns)

# Atualize o nome da coluna em app.py
# Exemplo: 'tp_sexo' pode ser 'sexo' ou 'genero'
```

---

### 10. Erro: "ValueError: No objects to concatenate"

**Sintoma**: Erro ao gerar amostras estratificadas

**Causa**: Nenhum dado disponível para estratificação

**Solução**:
```python
# Verifique se a coluna de estratificação existe
if 'tp_sexo' in df.columns:
    # Prossiga com estratificação
else:
    # Use outra coluna
    sample = sampling.stratified_sampling('outra_coluna')
```

---

## Problemas no Streamlit Cloud

### 11. Erro: "Secrets not found"

**Sintoma**: Erro ao acessar variáveis de ambiente

**Causa**: Secrets não configurados no Streamlit Cloud

**Solução**:
1. Acesse https://share.streamlit.io
2. Clique em "Manage app"
3. Vá para "Settings" → "Secrets"
4. Adicione as variáveis:
```toml
db_user = "data_iesb"
db_password = "iesb"
db_host = "bigdata.dataiesb.com"
db_port = 5432
db_name = "iesb"
```

---

### 12. Erro: "App crashed"

**Sintoma**: Aplicação para de funcionar no Streamlit Cloud

**Causa**: Erro não tratado ou recurso indisponível

**Solução**:
1. Verifique os logs:
   - Clique em "Manage app"
   - Vá para "Logs"
2. Procure pela mensagem de erro
3. Corrija o problema localmente
4. Faça push para GitHub
5. A aplicação será redeploy automaticamente

---

## Performance

### 13. Aplicação lenta

**Sintoma**: Aplicação demora para carregar ou responder

**Causa**: Muitos dados ou operações pesadas

**Solução**:
```python
# Use cache do Streamlit
@st.cache_data(ttl=3600)
def load_data():
    return load_combined_data(limit=50000)

# Reduza o número de registros
df = load_combined_data(limit=50000)

# Otimize gráficos
plt.rcParams['figure.figsize'] = (10, 6)  # Tamanho menor
```

---

### 14. Gráficos não aparecem

**Sintoma**: Área de gráfico vazia

**Causa**: Problema de renderização do matplotlib

**Solução**:
```python
# Use plt.close() após cada gráfico
fig, ax = plt.subplots()
ax.plot(data)
st.pyplot(fig)
plt.close(fig)  # Importante!

# Ou use use_container_width=True
st.pyplot(fig, use_container_width=True)
```

---

## Dicas de Debugging

### Ativar modo debug
```bash
# Execute com logs detalhados
streamlit run app.py --logger.level=debug
```

### Verificar variáveis
```python
# Adicione prints para debug
st.write("Debug:", df.columns)
st.write("Shape:", df.shape)
st.dataframe(df.head())
```

### Usar st.write para debug
```python
# Exiba variáveis facilmente
st.write(variable)  # Funciona com qualquer tipo
```

---

## Recursos Adicionais

- [Documentação Streamlit](https://docs.streamlit.io)
- [Stack Overflow - Streamlit](https://stackoverflow.com/questions/tagged/streamlit)
- [GitHub Issues - Streamlit](https://github.com/streamlit/streamlit/issues)
- [Comunidade Streamlit](https://discuss.streamlit.io)

---

## Suporte

Se o problema persistir:

1. **Verifique a documentação**: Leia os guias do projeto
2. **Procure online**: Google, Stack Overflow, GitHub Issues
3. **Abra uma issue**: No repositório GitHub
4. **Contate o suporte**: Streamlit Community

---

**Última atualização**: Abril de 2024
**Versão**: 1.0.0
