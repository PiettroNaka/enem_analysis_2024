# 🔐 Configuração de Secrets - Streamlit Cloud

## Como Adicionar Credenciais do Big Data-IESB no Streamlit Cloud

### Passo 1: Acessar o Streamlit Cloud
1. Acesse https://share.streamlit.io
2. Clique em "Manage app" (ícone de engrenagem)
3. Selecione sua aplicação "enem_analysis_2024"

### Passo 2: Ir para Secrets
1. Na barra lateral, clique em **"Secrets"**
2. Você verá um editor de texto com formato TOML

### Passo 3: Adicionar as Credenciais

Copie e cole o seguinte conteúdo no editor de Secrets:

```toml
# Big Data - IESB
db_host = "bigdata.dataiesb.com"
db_port = 5432
db_name = "iesb"
db_user = "data_iesb"
db_password = "iesb"
db_schema = "public"

# Configurações da Aplicação
use_database = true
```

### Passo 4: Salvar
1. Clique em "Save" (ou Ctrl+S)
2. A aplicação será reiniciada automaticamente

### Passo 5: Verificar
- Acesse a aplicação
- Verifique se os dados estão carregando do banco de dados
- Consulte os logs se houver erro

---

## 📋 Formato Correto do TOML

```toml
# Banco de Dados
db_host = "bigdata.dataiesb.com"
db_port = 5432
db_name = "iesb"
db_user = "data_iesb"
db_password = "iesb"
db_schema = "public"

# Aplicação
use_database = true
app_title = "Análise ENEM 2024"
app_icon = "📊"
```

---

## ⚠️ Importante

- **NÃO** compartilhe essas credenciais publicamente
- **NÃO** coloque no arquivo `.gitignore` (já está configurado)
- **NUNCA** faça commit de credenciais no GitHub
- Use apenas em Streamlit Cloud Secrets

---

## 🔍 Verificar se os Secrets Foram Adicionados

1. Acesse a aplicação
2. Abra o console do navegador (F12)
3. Verifique se há mensagens de erro
4. Se não houver erro, os secrets estão funcionando!

---

## 🐛 Troubleshooting

### Erro: "Connection refused"
- Verifique se o host está correto: `bigdata.dataiesb.com`
- Verifique se a porta está correta: `5432`
- Verifique a conexão com a internet

### Erro: "Authentication failed"
- Verifique o usuário: `data_iesb`
- Verifique a senha: `iesb`
- Verifique se o banco de dados está online

### Erro: "Database not found"
- Verifique o nome do banco: `iesb`
- Verifique o schema: `public`

### A aplicação não está usando os secrets
- Verifique se salvou os secrets (clique em Save)
- Aguarde 1-2 minutos para a aplicação reiniciar
- Recarregue a página (Ctrl+F5)

---

## 📝 Próximas Etapas

1. ✅ Adicionar secrets no Streamlit Cloud
2. ✅ Atualizar app.py para usar o banco de dados
3. ✅ Testar a conexão
4. ✅ Verificar se os dados estão carregando

---

## 🔗 Links Úteis

- [Documentação Streamlit Secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)
- [Documentação SQLAlchemy](https://docs.sqlalchemy.org/)
- [PostgreSQL Connection Strings](https://www.postgresql.org/docs/current/libpq-connect-using-params.html)

---

**Última Atualização**: Abril de 2024
**Versão**: 1.0.0
