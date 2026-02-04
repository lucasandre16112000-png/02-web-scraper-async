# 📊 DASHBOARD - VISUALIZE OS DADOS

Criei um **Dashboard Web Interativo** para você visualizar os dados do scraper de forma muito mais legal!

---

## 🚀 Como Usar

### Opção 1: Abrir Diretamente (Mais Fácil)

1. Vá para a pasta do projeto: `C:\Users\Pc\02-web-scraper-async`
2. Clique duplo em `dashboard.html`
3. O navegador vai abrir automaticamente
4. Clique em "Escolher arquivo" e selecione `scraping_results.json`

### Opção 2: Usar o Servidor Web

Se preferir acessar via servidor local:

```powershell
# Ativar ambiente virtual (se não estiver)
.\venv\Scripts\activate

# Rodar o servidor
python server.py
```

Isso vai:
- ✅ Iniciar um servidor em `http://localhost:8000`
- ✅ Abrir o navegador automaticamente
- ✅ Servir o dashboard

---

## 📋 O Que Você Verá

### 1. **Estatísticas Principais**
- ✅ Total de sucessos
- ❌ Total de falhas
- ⏱️ Tempo total de processamento
- 📊 Taxa média de itens por segundo

### 2. **Gráficos Interativos**
- 📈 Gráfico de pizza: Taxa de sucesso vs falhas
- ⏱️ Gráfico de barras: Tempo de processamento

### 3. **Lista de Artigos**
- 📄 Todos os artigos extraídos
- 🔗 Links clicáveis para acessar as URLs
- 👤 Autor (se disponível)
- 📅 Data de publicação (se disponível)
- 📝 Resumo (se disponível)
- ⏰ Timestamp de quando foi coletado

---

## 🎯 Passo a Passo Completo

### 1. Rodar o Scraper

```powershell
# Ativar ambiente virtual
.\venv\Scripts\activate

# Rodar o scraper
python scraper.py
```

Isso vai criar um arquivo `scraping_results.json`

### 2. Abrir o Dashboard

**Opção A: Clique Duplo (Mais Fácil)**
- Vá para a pasta do projeto
- Clique duplo em `dashboard.html`

**Opção B: Servidor Web**
```powershell
python server.py
```

### 3. Carregar os Dados

- Clique em "Escolher arquivo"
- Selecione `scraping_results.json`
- Os dados aparecem automaticamente!

---

## 📊 Recursos do Dashboard

### ✨ Recursos Principais

- **Responsivo**: Funciona em desktop, tablet e mobile
- **Gráficos Interativos**: Feitos com Chart.js
- **Design Moderno**: Interface limpa e intuitiva
- **Sem Dependências**: Funciona offline (exceto Chart.js)
- **Carregamento de Arquivo**: Selecione qualquer arquivo JSON

### 🎨 Design

- **Cores Vibrantes**: Gradiente roxo e azul
- **Cards Interativos**: Efeitos hover
- **Badges de Status**: Indicadores visuais
- **Tipografia Clara**: Fácil de ler

---

## 🔧 Troubleshooting

### Problema: "O arquivo não carrega"

**Solução:**
1. Certifique-se de que `scraping_results.json` existe na pasta do projeto
2. Verifique se o arquivo não está corrompido
3. Tente rodar o scraper novamente: `python scraper.py`

### Problema: "O navegador não abre automaticamente"

**Solução:**
1. Abra manualmente: `http://localhost:8000/dashboard.html`
2. Ou clique duplo em `dashboard.html`

### Problema: "Erro ao carregar o arquivo"

**Solução:**
1. Verifique se o arquivo é um JSON válido
2. Abra o arquivo com um editor de texto para verificar
3. Se estiver corrompido, rodar o scraper novamente

---

## 📁 Arquivos Necessários

Para usar o dashboard, você precisa de:

- `dashboard.html` - O dashboard (já criado)
- `server.py` - Servidor web (opcional)
- `scraping_results.json` - Dados do scraper (criado ao rodar `python scraper.py`)

---

## 🌐 Acessar de Outro Computador

Se você quer acessar o dashboard de outro computador na mesma rede:

1. Descubra o IP do seu computador:
```powershell
ipconfig
```

Procure por "IPv4 Address" (algo como `192.168.1.100`)

2. No outro computador, acesse:
```
http://192.168.1.100:8000/dashboard.html
```

---

## 💾 Exportar Dados

O dashboard não exporta dados, mas você pode:

1. **Ver o JSON**: Abra `scraping_results.json` com um editor de texto
2. **Copiar Dados**: Use o navegador para copiar os dados
3. **Salvar HTML**: Use o navegador para salvar a página como HTML

---

## 🎯 Próximos Passos

1. **Rodar o scraper**: `python scraper.py`
2. **Abrir o dashboard**: Clique duplo em `dashboard.html`
3. **Carregar dados**: Selecione `scraping_results.json`
4. **Explorar**: Veja os gráficos e dados!

---

## 📞 Precisa de Ajuda?

1. Verifique se o arquivo `scraping_results.json` existe
2. Verifique se o arquivo é um JSON válido
3. Tente rodar o scraper novamente
4. Verifique os logs: `type logs\scraper.log`

---

**Pronto para visualizar seus dados? Abra o dashboard agora!** 🚀
