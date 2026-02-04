# 🕷️ Web Scraper Assíncrono Profissional

Um web scraper de alta performance construído com Python, `asyncio` e `aiohttp`. Projetado para extrair dados de múltiplos sites em paralelo, com rate limiting inteligente, retry automático e tratamento robusto de erros.

**✅ 100% Compatível com Windows, macOS e Linux**

## ✨ Funcionalidades Principais

- **Processamento Assíncrono**: Utiliza `asyncio` e `aiohttp` para fazer múltiplas requisições HTTP em paralelo, aumentando drasticamente a velocidade de coleta de dados.
- **Rate Limiting Inteligente**: Inclui uma classe `RateLimiter` para controlar a frequência das requisições, evitando sobrecarregar o servidor de destino e ser bloqueado.
- **Retry Automático com Exponential Backoff**: Tenta novamente requisições que falharam (ex: por timeout ou erro de rede) com um tempo de espera que aumenta exponencialmente, melhorando a resiliência do scraper.
- **Validação de URLs**: Valida URLs antes de fazer requisições, evitando erros desnecessários.
- **Logging Detalhado**: Fornece feedback em tempo real sobre o progresso do scraping, incluindo sucessos, avisos e erros.
- **Extração Estruturada**: Extrai dados estruturados (título, autor, data, resumo) de páginas HTML usando BeautifulSoup.
- **Estatísticas Completas**: Calcula e exibe estatísticas detalhadas como taxa de sucesso, tempo total e velocidade média.
- **Exportação em JSON**: Salva automaticamente todos os resultados em um arquivo JSON bem formatado.
- **Compatibilidade Multiplataforma**: Funciona perfeitamente em Windows, macOS e Linux com scripts de setup automático.

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|:---|:---|:---|
| **Python** | 3.8+ | Linguagem principal |
| **aiohttp** | 3.9.1 | Cliente/Servidor HTTP assíncrono |
| **BeautifulSoup4** | 4.12.2 | Parsing de HTML e XML |
| **lxml** | 4.9.3 | Parser XML/HTML de alta performance |
| **python-dotenv** | 1.0.0 | Gerenciamento de variáveis de ambiente |

## 📂 Estrutura do Projeto

```
/02-web-scraper-async
├── scraper.py              # Código principal do scraper
├── example_urls.py         # Exemplo de uso com URLs customizadas
├── test_scraper.py         # Testes unitários
├── requirements.txt        # Dependências do projeto
├── setup.py                # Script de setup automático (multiplataforma)
├── setup.bat               # Script de setup para Windows
├── setup.sh                # Script de setup para Linux/macOS
├── .env.example            # Exemplo de arquivo de configuração
├── .gitignore              # Arquivos a ignorar no Git
└── README.md               # Este arquivo
```

## 📋 Guia de Instalação e Execução

### Pré-requisitos

1. **Git**: Ferramenta para baixar (clonar) o código do GitHub.
   - [**Download do Git aqui**](https://git-scm.com/downloads)

2. **Python**: A linguagem de programação usada no projeto (versão 3.8 ou superior).
   - [**Download do Python aqui**](https://www.python.org/downloads/)
   - **Importante (Windows)**: Durante a instalação do Python, marque a caixa que diz **"Add Python to PATH"**.

### Instalação Automática (Recomendado)

#### Windows

1. Abra o **PowerShell** ou **Command Prompt** na pasta do projeto
2. Execute:
```bash
python setup.py
```

Ou simplesmente clique duas vezes em `setup.bat`

#### Linux/macOS

1. Abra o **Terminal** na pasta do projeto
2. Execute:
```bash
bash setup.sh
```

Ou:
```bash
python3 setup.py
```

### Instalação Manual

#### Passo 1: Baixar o Projeto (Clonar)

Abra o seu terminal (ou **Git Bash** no Windows) e use o comando abaixo para baixar o projeto:

```bash
git clone https://github.com/lucasandre16112000-png/02-web-scraper-async.git
cd 02-web-scraper-async
```

#### Passo 2: Criar e Ativar um Ambiente Virtual

Um ambiente virtual isola as dependências do projeto, evitando conflitos com outras aplicações Python.

**No Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**No Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate
```

**No macOS ou Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Você saberá que o ambiente virtual está ativado quando ver `(venv)` no início da linha do seu terminal.

#### Passo 3: Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

#### Passo 4: Executar o Scraper

Execute o script principal para começar o scraping:

```bash
python scraper.py
```

#### Passo 5: Verificar os Resultados

- O terminal mostrará o progresso do scraping em tempo real com emojis e mensagens claras.
- Ao final, um arquivo chamado `scraping_results.json` será criado na mesma pasta, contendo todos os dados extraídos em formato JSON.
- Você pode abrir este arquivo com qualquer editor de texto ou visualizador JSON.

## 🚀 Exemplos de Uso

### Exemplo 1: Usar o Script Padrão

O script padrão (`scraper.py`) já contém um exemplo pronto para usar:

```bash
python scraper.py
```

### Exemplo 2: Customizar URLs

Para scraper URLs diferentes, edite o arquivo `example_urls.py` e modifique a lista `urls`:

```python
urls = [
    "https://seu-site-1.com",
    "https://seu-site-2.com",
    "https://seu-site-3.com",
]
```

Depois execute:

```bash
python example_urls.py
```

### Exemplo 3: Usar o Scraper em Seu Próprio Código

Você pode importar o scraper em seu próprio projeto Python:

```python
import asyncio
from scraper import WebScraper

async def meu_scraper():
    scraper = WebScraper(
        requests_per_second=2.0,  # Máximo de 2 requisições por segundo
        timeout=10,                # Timeout de 10 segundos
        max_retries=3              # Máximo de 3 tentativas
    )
    
    urls = ["https://exemplo.com", "https://outro-site.com"]
    articles = await scraper.scrape_articles(urls)
    
    for article in articles:
        print(f"Título: {article.title}")
        print(f"URL: {article.url}")

asyncio.run(meu_scraper())
```

### Exemplo 4: Especificar Diretório de Saída

```python
import asyncio
from scraper import WebScraper

async def meu_scraper():
    scraper = WebScraper(
        requests_per_second=2.0,
        timeout=10,
        max_retries=3,
        output_dir="./resultados"  # Salvar em outro diretório
    )
    
    urls = ["https://exemplo.com"]
    articles = await scraper.scrape_articles(urls)
    scraper.save_results(articles)

asyncio.run(meu_scraper())
```

## ⚙️ Configuração Avançada

### Parâmetros do WebScraper

Ao criar uma instância do `WebScraper`, você pode customizar os seguintes parâmetros:

```python
scraper = WebScraper(
    requests_per_second=2.0,  # Taxa de requisições (padrão: 2.0)
    timeout=10,                # Timeout em segundos (padrão: 10)
    max_retries=3,             # Máximo de tentativas (padrão: 3)
    output_dir=None            # Diretório de saída (padrão: diretório atual)
)
```

- **requests_per_second**: Controla quantas requisições são feitas por segundo. Valores menores são mais respeitosos com o servidor.
- **timeout**: Tempo máximo de espera para cada requisição em segundos.
- **max_retries**: Número de tentativas antes de desistir de uma URL.
- **output_dir**: Diretório onde os resultados serão salvos.

### Variáveis de Ambiente

Você pode configurar o scraper usando variáveis de ambiente. Copie `.env.example` para `.env` e edite:

```bash
# Configurações do Web Scraper

# Taxa de requisições por segundo (padrão: 2.0)
REQUESTS_PER_SECOND=2.0

# Timeout em segundos para cada requisição (padrão: 10)
TIMEOUT=10

# Máximo de tentativas para cada URL (padrão: 3)
MAX_RETRIES=3

# Nível de log (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL=INFO
```

## 🧪 Executar Testes

O projeto inclui testes unitários abrangentes:

```bash
python test_scraper.py
```

Os testes cobrem:
- Validação de URLs
- Rate limiting
- Criação de artigos
- Inicialização do scraper
- Scraping com URLs vazias/inválidas
- Integração com URLs reais

## 🤔 Solução de Problemas Comuns

### Problema: "ModuleNotFoundError: No module named 'aiohttp'"

**Solução**: Certifique-se de que:
1. O ambiente virtual (venv) está ativado (você deve ver `(venv)` no terminal)
2. Você executou `pip install -r requirements.txt`

### Problema: "Erros de Conexão ou Timeout"

**Solução**: 
- A internet pode estar instável ou o site alvo pode estar bloqueando requisições.
- Tente aumentar o `timeout` ou reduzir `requests_per_second`.
- O script já tenta lidar com isso automaticamente, mas se o erro persistir, pode ser um problema de rede.

### Problema: "SSL: CERTIFICATE_VERIFY_FAILED"

**Solução**: O script já desativa a verificação SSL por padrão. Se o erro persistir, verifique sua conexão de internet.

### Problema: "Arquivo scraping_results.json não foi criado"

**Solução**:
- Verifique se o script executou até o final sem erros.
- Certifique-se de que você tem permissão de escrita na pasta do projeto.
- Verifique o terminal para ver se há mensagens de erro.

### Problema: "Python não reconhecido no Windows"

**Solução**:
1. Reinstale Python marcando **"Add Python to PATH"** durante a instalação
2. Reinicie o computador
3. Abra um novo terminal e tente novamente

## 📊 Entendendo a Saída

Quando você executa o scraper, você verá uma saída como esta:

```
================================================================================
WEB SCRAPER PROFISSIONAL - EXEMPLO DE USO
Sistema Operacional: Windows
================================================================================

📊 Iniciando scraping de 3 URLs...
⏱️  Rate limit: 2 requisições/segundo
🔄 Máximo de tentativas: 3

✓ Fetched: https://news.ycombinator.com
✓ Fetched: https://www.reddit.com/r/programming
✓ Fetched: https://www.techcrunch.com

================================================================================
RESULTADOS
================================================================================

📄 Artigo 1:
   Título: Hacker News
   URL: https://news.ycombinator.com
   Autor: N/A
   Data: N/A
   Resumo: N/A

[... mais artigos ...]

================================================================================
ESTATÍSTICAS
================================================================================

Total de URLs: 3
Sucesso: 3
Falhas: 0
Tempo total: 5.23s
Taxa média: 0.57 itens/segundo
Status: completed

✅ Resultados salvos em 'scraping_results.json'
```

## 📁 Formato do Arquivo JSON de Saída

O arquivo `scraping_results.json` contém todos os dados extraídos em um formato estruturado:

```json
{
  "timestamp": "2025-12-12T18:30:45.123456",
  "articles": [
    {
      "title": "Hacker News",
      "url": "https://news.ycombinator.com",
      "author": null,
      "published_date": null,
      "summary": null,
      "scraped_at": "2025-12-12T18:30:45.123456"
    }
  ],
  "statistics": {
    "total_items": 3,
    "successful_items": 3,
    "failed_items": 0,
    "total_time": 5.23,
    "items_per_second": 0.57,
    "status": "completed"
  }
}
```

## 📋 Logs

Os logs são salvos automaticamente em `logs/scraper.log`. Você pode verificar este arquivo para mais detalhes sobre a execução:

```bash
# Windows
type logs\scraper.log

# Linux/macOS
cat logs/scraper.log
```

## 🔒 Boas Práticas e Ética

- **Respeite o robots.txt**: Sempre verifique o arquivo `robots.txt` do site antes de fazer scraping.
- **Use Rate Limiting**: Não faça requisições muito rápidas para não sobrecarregar os servidores.
- **Verifique os Termos de Serviço**: Certifique-se de que você tem permissão para fazer scraping do site.
- **Identifique-se**: Use um User-Agent apropriado (o script já faz isso automaticamente).
- **Não Armazene Dados Pessoais**: Tenha cuidado ao coletar dados que possam conter informações pessoais.

## 🔄 Melhorias Implementadas (v2.0)

- ✅ Compatibilidade total com Windows (event loop policy)
- ✅ Validação robusta de URLs
- ✅ Scripts de setup automático (Python, Batch, Shell)
- ✅ Suporte a variáveis de ambiente (.env)
- ✅ Diretório de logs automático
- ✅ Tratamento de encoding UTF-8 em Windows
- ✅ Testes unitários expandidos
- ✅ Melhor tratamento de erros
- ✅ Documentação completa
- ✅ Suporte a diretório de saída customizável

## 👨‍💻 Autor

Lucas André S - [GitHub](https://github.com/lucasandre16112000-png)

## 📝 Licença

Este projeto é licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para:
- Reportar bugs
- Sugerir novas funcionalidades
- Fazer pull requests

## 📞 Suporte

Se você encontrar problemas ou tiver dúvidas:
1. Verifique a seção "Solução de Problemas Comuns"
2. Verifique os logs em `logs/scraper.log`
3. Abra uma issue no GitHub
