# Guia de Deploy no Streamlit Cloud

## Como Publicar a Aplicação no Streamlit Cloud

O Streamlit Cloud permite hospedar sua aplicação gratuitamente com deploy automático a partir do GitHub.

### Passo 1: Criar Conta no Streamlit Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Clique em "Sign up"
3. Selecione "Sign up with GitHub"
4. Autorize a integração com GitHub
5. Complete seu perfil

### Passo 2: Conectar Repositório GitHub

1. Clique em "New app"
2. Selecione:
   - **Repository**: PiettroNaka/enem_analysis_2024
   - **Branch**: main
   - **Main file path**: app.py
3. Clique em "Deploy"

### Passo 3: Configurar Variáveis de Ambiente

Se necessário, configure variáveis de ambiente:

1. Vá para "Settings" → "Secrets"
2. Adicione variáveis conforme necessário:
   ```
   DB_USER=data_iesb
   DB_PASS=iesb
   DB_HOST=bigdata.dataiesb.com
   DB_PORT=5432
   DB_NAME=iesb
   ```

### Passo 4: Acompanhar Deploy

1. A aplicação será construída automaticamente
2. Você verá o progresso em tempo real
3. Após conclusão, receberá um link público

### URL da Aplicação

Após o deploy bem-sucedido, sua aplicação estará disponível em:
```
https://enem-analysis-2024.streamlit.app
```

### Configurações Recomendadas

#### 1. Auto-reload
- Ativado por padrão
- Redeploy automático ao fazer push no GitHub

#### 2. Timeout
- Padrão: 60 segundos
- Para operações longas, pode aumentar em Settings

#### 3. Memory
- Padrão: 512 MB
- Suficiente para análise de dados

### Troubleshooting

#### Erro: "ModuleNotFoundError"
**Solução**: Verifique se `requirements.txt` está no root do repositório

#### Erro: "Connection refused" ao banco de dados
**Solução**: Verifique credenciais em `utils/database.py`

#### Aplicação lenta
**Solução**: Use cache do Streamlit:
```python
@st.cache_data(ttl=3600)
def load_data():
    # seu código
```

### Monitoramento

1. **Logs**: Acesse "Manage app" → "Logs"
2. **Métricas**: Veja uso de CPU, memória e tempo de execução
3. **Alertas**: Configure notificações de erro

### Atualizar Aplicação

Após fazer alterações:

```bash
git add .
git commit -m "Descrição da alteração"
git push origin main
```

A aplicação será redeploy automaticamente em poucos minutos.

### Limpar Cache

Se precisar limpar cache da aplicação:

1. Vá para "Manage app"
2. Clique em "Reboot app"
3. Ou faça um novo push para GitHub

### Compartilhar Aplicação

Após deploy, compartilhe o link:
```
https://enem-analysis-2024.streamlit.app
```

Você pode:
- Compartilhar em redes sociais
- Adicionar ao README.md
- Incluir em portfólio

### Recursos Adicionais

- [Documentação Streamlit Cloud](https://docs.streamlit.io/streamlit-cloud)
- [Guia de Deploy](https://docs.streamlit.io/streamlit-cloud/get-started)
- [Troubleshooting](https://docs.streamlit.io/streamlit-cloud/troubleshooting)

### Próximas Melhorias

- [ ] Adicionar autenticação
- [ ] Implementar banco de dados local
- [ ] Adicionar temas customizados
- [ ] Criar páginas adicionais
- [ ] Implementar cache de dados

---

**Nota**: O Streamlit Cloud oferece 1 GB de armazenamento e execução ilimitada para repositórios públicos.

Para mais informações, consulte a [documentação oficial](https://docs.streamlit.io/streamlit-cloud).
