# 🕷️ Web Scraper PRO - Dashboard Profissional

Um web scraper assíncrono profissional com dashboard interativo, rotação de 30+ fontes, análises avançadas e interface visual moderna. Construído com Python, `asyncio` e `aiohttp`.

**✅ 100% Compatível com Windows, macOS e Linux**

---

## ✨ Funcionalidades Principais

- **🚀 Processamento Assíncrono**: Múltiplas requisições HTTP em paralelo com `asyncio` e `aiohttp`
- **🔄 Rotação de 30+ Fontes**: Sempre coleta dados de diferentes sites
- **📊 Dashboard Interativo**: Interface visual profissional com gráficos em tempo real
- **🎯 Análises Avançadas**: Sentimento, engajamento, categorização inteligente
- **⚡ Rate Limiting Inteligente**: Controla requisições sem sobrecarregar servidores
- **🔁 Retry Automático**: Exponential backoff para requisições que falham
- **✅ Validação de URLs**: Valida antes de fazer requisições
- **📝 Logging Detalhado**: Feedback em tempo real do progresso
- **📁 Exportação JSON**: Salva dados estruturados automaticamente
- **🖥️ Compatibilidade Multiplataforma**: Windows, macOS e Linux

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|:---|:---|:---|
| **Python** | 3.8+ | Linguagem principal |
| **aiohttp** | 3.9.1 | Cliente/Servidor HTTP assíncrono |
| **BeautifulSoup4** | 4.12.2 | Parsing de HTML e XML |
| **lxml** | 4.9.3 | Parser XML/HTML de alta performance |
| **python-dotenv** | 1.0.0 | Gerenciamento de variáveis de ambiente |

---

## 📂 Estrutura do Projeto

```
/02-web-scraper-async
├── scraper_pro_v4.py           # Scraper principal (versão final)
├── server_pro_v4.py            # Servidor web com dashboard
├── dashboard_pro.html          # Interface visual profissional
├── RODAR_WEB_SCRAPER.vbs       # Launcher Windows (recomendado)
├── RODAR_WEB_SCRAPER.bat       # Launcher Windows (backup)
├── requirements.txt            # Dependências do projeto
├── README.md                   # Este arquivo
├── DASHBOARD.md                # Guia do dashboard
└── LEIA-ME-CLIENTE.txt         # Instruções para clientes
```

---

## 📋 Guia de Instalação e Execução

### Pré-requisitos

1. **Git**: Ferramenta para clonar o repositório
   - [**Download do Git aqui**](https://git-scm.com/downloads)

2. **Python**: Versão 3.8 ou superior
   - [**Download do Python aqui**](https://www.python.org/downloads/)
   - **Importante (Windows)**: Marque **"Add Python to PATH"** durante instalação

---

## 🚀 Instalação e Execução Rápida (RECOMENDADO)

### Windows - Clique 2 Vezes (Mais Fácil)

1. Clique 2 vezes em `RODAR_WEB_SCRAPER.vbs`
2. Aguarde o navegador abrir
3. Clique em "🚀 Iniciar Scraping PRO"
4. Pronto! Dashboard mostra dados em tempo real

### Windows - PowerShell

```powershell
git clone https://github.com/lucasandre16112000-png/02-web-scraper-async.git
cd 02-web-scraper-async
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python server_pro_v4.py
```

### Linux/macOS - Terminal

```bash
git clone https://github.com/lucasandre16112000-png/02-web-scraper-async.git
cd 02-web-scraper-async
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 server_pro_v4.py
```

---

## 📊 Como Usar o Dashboard

### Passo 1: Iniciar o Servidor
```powershell
python server_pro_v4.py
```

### Passo 2: Abrir Dashboard
- Navegador abre automaticamente em `http://localhost:8000`
- Ou acesse manualmente: `http://localhost:8000`

### Passo 3: Iniciar Scraping
- Clique no botão **"🚀 Iniciar Scraping PRO"**
- Dashboard mostra progresso em tempo real
- Gráficos e estatísticas atualizam automaticamente

### Passo 4: Visualizar Dados
- **Estatísticas**: Total de artigos, fontes, categorias
- **Gráficos**: Distribuição de sentimento, artigos por fonte
- **Análises**: Score de engajamento, top artigos
- **Lista**: Todos os artigos com detalhes completos

---

## 🎯 Exemplos de Uso

### Exemplo 1: Rodar Scraper Diretamente (Python)

```python
import asyncio
from scraper_pro_v4 import WebScraperPro

async def main():
    scraper = WebScraperPro()
    results = await scraper.scrape()
    print(f"✅ {len(results)} artigos coletados!")

asyncio.run(main())
```

### Exemplo 2: Usar com URLs Customizadas

```python
import asyncio
from scraper_pro_v4 import WebScraperPro

async def main():
    scraper = WebScraperPro()
    # Customizar fontes
    scraper.sources = [
        "https://seu-site-1.com",
        "https://seu-site-2.com"
    ]
    results = await scraper.scrape()

asyncio.run(main())
```

---

## ⚙️ Configuração Avançada

### Parâmetros do WebScraperPro

```python
scraper = WebScraperPro(
    requests_per_second=2.0,  # Taxa de requisições
    timeout=10,                # Timeout em segundos
    max_retries=3              # Máximo de tentativas
)
```

### Variáveis de Ambiente

Crie um arquivo `.env`:

```
REQUESTS_PER_SECOND=2.0
TIMEOUT=10
MAX_RETRIES=3
LOG_LEVEL=INFO
```

---

## 📊 Dados Coletados

Cada artigo contém:
- ✅ Título
- ✅ URL
- ✅ Autor
- ✅ Data de publicação
- ✅ Resumo
- ✅ Conteúdo completo
- ✅ Categoria (12 tipos)
- ✅ Tags
- ✅ Views, Likes, Comentários
- ✅ Score de engajamento
- ✅ Análise de sentimento
- ✅ Palavras-chave

---

## 📡 30+ Fontes Disponíveis

**Tech News:**
Hacker News, TechCrunch, The Verge, Wired, Ars Technica, AnandTech

**Programming:**
Reddit r/programming, Dev.to, Medium, CSS Tricks, Smashing Magazine

**Product & Startup:**
Product Hunt, Indie Hackers, Y Combinator

**Community:**
GitHub Trending, Lobsters, Hacker News New

**Analysis:**
Slashdot, InfoQ, Dzone, SitePoint

**Design:**
Web Designer Depot, Dribbble, Designer Hangout

**Learning:**
FreeCodeCamp, Scotch.io, Egghead

**Showcase:**
Codepen, Codesignal

---

## 🤔 Solução de Problemas Comuns

### Problema: "ModuleNotFoundError: No module named 'aiohttp'"

**Solução**: 
1. Certifique-se que o ambiente virtual está ativado: `(venv)` deve aparecer no terminal
2. Execute: `pip install -r requirements.txt`

### Problema: "Erros de Conexão ou Timeout"

**Solução**: 
- Verifique sua conexão de internet
- Tente aumentar o `timeout` em `server_pro_v4.py`
- Reduza `requests_per_second`

### Problema: "Dashboard não abre no navegador"

**Solução**:
- Verifique se o servidor está rodando (deve mostrar "Servidor rodando em http://localhost:8000")
- Acesse manualmente: `http://localhost:8000`
- Verifique se a porta 8000 não está em uso

### Problema: "Python não reconhecido no Windows"

**Solução**:
1. Reinstale Python marcando **"Add Python to PATH"**
2. Reinicie o computador
3. Abra um novo terminal e tente novamente

---

## 📊 Formato do Arquivo JSON de Saída

```json
{
  "timestamp": "2026-02-03T20:00:00.000000",
  "articles": [
    {
      "title": "Exemplo de Artigo",
      "url": "https://exemplo.com",
      "author": "John Doe",
      "published_date": "2026-02-03",
      "summary": "Resumo do artigo...",
      "content": "Conteúdo completo...",
      "category": "AI/ML",
      "tags": ["ai", "machine-learning"],
      "views": 1000,
      "likes": 250,
      "comments": 50,
      "shares": 100,
      "engagement_score": 85.5,
      "sentiment": "positive",
      "keywords": ["ai", "ml", "learning"]
    }
  ],
  "statistics": {
    "total_items": 56,
    "successful_items": 56,
    "failed_items": 0,
    "total_time": 12.45,
    "items_per_second": 4.5,
    "status": "completed"
  }
}
```

---

## 🔒 Boas Práticas e Ética

- **Respeite o robots.txt**: Verifique antes de fazer scraping
- **Use Rate Limiting**: Não sobrecarregue os servidores
- **Verifique Termos de Serviço**: Tenha permissão para fazer scraping
- **Identifique-se**: Use User-Agent apropriado (automático)
- **Não Armazene Dados Pessoais**: Tenha cuidado com informações sensíveis

---

## 🔄 Versão Atual (v4.0)

- ✅ Rotação de 30+ fontes
- ✅ Dashboard profissional interativo
- ✅ Análises avançadas (sentimento, engajamento)
- ✅ Categorização inteligente (12 categorias)
- ✅ Extração completa de dados
- ✅ Compatibilidade 100% Windows
- ✅ Launcher automático (.vbs)
- ✅ Interface visual moderna

---

## 👨‍💻 Autor

Lucas André S - [GitHub](https://github.com/lucasandre16112000-png)

---

## 📝 Licença

MIT License - Veja LICENSE para detalhes

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para:
- Reportar bugs
- Sugerir novas funcionalidades
- Fazer pull requests

---

## 📞 Suporte

Se encontrar problemas:
1. Verifique a seção "Solução de Problemas Comuns"
2. Verifique os logs em `logs/scraper.log`
3. Abra uma issue no GitHub

---

**Pronto para começar? Execute `python RODAR_WEB_SCRAPER.vbs` no Windows ou `python server_pro_v4.py` em Linux/macOS!** 🚀
