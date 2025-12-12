# 🕷️ App 2: Web Scraper Assíncrono e Profissional

Este projeto demonstra a construção de um **web scraper de alta performance** utilizando Python com as bibliotecas `asyncio` e `aiohttp`. Ele é projetado para ser eficiente, robusto e respeitoso com os servidores de destino, incorporando funcionalidades essenciais para automação de dados em escala.

## ✨ Funcionalidades Principais

- **Processamento Assíncrono**: Utiliza `asyncio` e `aiohttp` para fazer múltiplas requisições HTTP em paralelo, aumentando drasticamente a velocidade de coleta de dados.
- **Rate Limiting Inteligente**: Inclui uma classe `RateLimiter` para controlar a frequência das requisições, evitando sobrecarregar o servidor de destino e ser bloqueado.
- **Retry Automático com Exponential Backoff**: Tenta novamente requisições que falharam (ex: por timeout ou erro de rede) com um tempo de espera que aumenta exponencialmente, melhorando a resiliência do scraper.
- **Logging Detalhado**: Fornece feedback em tempo real sobre o progresso do scraping, incluindo sucessos, avisos e erros.

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
| :--- | :--- | :--- |
| **Python** | 3.11+ | Linguagem principal |
| **aiohttp** | 3.9.1 | Cliente/Servidor HTTP assíncrono |
| **BeautifulSoup4** | 4.12.2 | Biblioteca para parsing de HTML e XML |

## 📋 Guia de Instalação e Execução (Para Qualquer Pessoa)

Este guia foi feito para que qualquer pessoa, mesmo sem conhecimento técnico, possa executar este projeto.

### Pré-requisitos

1.  **Git**: Ferramenta para baixar (clonar) o código do GitHub.
    - [**Download do Git aqui**](https://git-scm.com/downloads)
2.  **Python**: A linguagem de programação usada no projeto (versão 3.8 ou superior).
    - [**Download do Python aqui**](https://www.python.org/downloads/)
    - **Importante**: Durante a instalação do Python no Windows, marque a caixa que diz **"Add Python to PATH"**.

### Passo 1: Baixar o Projeto (Clonar)

Abra o seu terminal (ou **Git Bash** no Windows) e use o comando abaixo para baixar o projeto:

```bash
git clone https://github.com/lucasandre16112000-png/02-web-scraper-async.git
```

### Passo 2: Entrar na Pasta do Projeto

```bash
cd 02-web-scraper-async
```

### Passo 3: Criar e Ativar um Ambiente Virtual

```bash
# No Windows
python -m venv venv
.\venv\Scripts\activate

# No macOS ou Linux
python3 -m venv venv
source venv/bin/activate
```

### Passo 4: Instalar as Bibliotecas do Projeto

```bash
pip install -r requirements.txt
```

### Passo 5: Executar o Scraper

```bash
python scraper.py
```

### Passo 6: Verificar os Resultados

- O terminal mostrará o progresso do scraping em tempo real.
- Ao final, um arquivo chamado `scraping_results.json` será criado na mesma pasta, contendo todos os dados extraídos.

## 🤔 Solução de Problemas Comuns

- **`ModuleNotFoundError: No module named 'aiohttp'`**: Certifique-se de que o ambiente virtual (venv) está ativado (Passo 3) e que você instalou as dependências (Passo 4).
- **Erros de Conexão ou Timeout**: A internet pode estar instável ou o site alvo pode estar bloqueando requisições. O script já tenta lidar com isso, mas se o erro persistir, pode ser um problema de rede.

## 👨‍💻 Autor

Lucas André S - [GitHub](https://github.com/lucasandre16112000-png)
