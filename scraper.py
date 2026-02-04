"""
Web Scraper Profissional com Rate Limiting e Tratamento de Erros
Exemplo de automação de dados com boas práticas de performance e respeito a recursos.
Totalmente compatível com Windows, macOS e Linux.
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
from datetime import datetime
from typing import List, Dict, Optional
import logging
import logging.handlers
from dataclasses import dataclass, asdict
from enum import Enum
import time
import os
import sys
from pathlib import Path
import platform

# Configuração de logging com suporte a Windows
log_dir = Path.cwd() / "logs"
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / "scraper.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Configuração de asyncio para Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class ScraperStatus(Enum):
    """Status de scraping"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Article:
    """Modelo de artigo extraído"""
    title: str
    url: str
    author: Optional[str] = None
    published_date: Optional[str] = None
    summary: Optional[str] = None
    scraped_at: str = None
    
    def __post_init__(self):
        if self.scraped_at is None:
            self.scraped_at = datetime.utcnow().isoformat()


@dataclass
class ScraperStats:
    """Estatísticas de scraping"""
    total_items: int = 0
    successful_items: int = 0
    failed_items: int = 0
    total_time: float = 0.0
    items_per_second: float = 0.0
    status: ScraperStatus = ScraperStatus.PENDING


class URLValidator:
    """Validador de URLs"""
    
    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Validar se uma URL é válida"""
        if not isinstance(url, str):
            return False
        
        url = url.strip()
        if not url:
            return False
        
        # Verificar se começa com http:// ou https://
        if not (url.startswith("http://") or url.startswith("https://")):
            return False
        
        # Verificar se tem pelo menos um ponto no domínio
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            if not parsed.netloc or "." not in parsed.netloc:
                return False
            return True
        except Exception:
            return False


class RateLimiter:
    """Limitador de taxa de requisições"""
    
    def __init__(self, requests_per_second: float = 1.0):
        self.requests_per_second = requests_per_second
        self.min_interval = 1.0 / requests_per_second
        self.last_request_time = 0.0
    
    async def wait(self):
        """Aguardar antes de fazer próxima requisição"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.min_interval:
            await asyncio.sleep(self.min_interval - elapsed)
        self.last_request_time = time.time()


class WebScraper:
    """Scraper profissional com rate limiting e tratamento de erros"""
    
    def __init__(
        self,
        requests_per_second: float = 2.0,
        timeout: int = 10,
        max_retries: int = 3,
        output_dir: Optional[str] = None
    ):
        self.rate_limiter = RateLimiter(requests_per_second)
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.max_retries = max_retries
        self.stats = ScraperStats()
        self.user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
        
        # Configurar diretório de saída
        if output_dir is None:
            self.output_dir = Path.cwd()
        else:
            self.output_dir = Path(output_dir)
            self.output_dir.mkdir(parents=True, exist_ok=True)
    
    async def fetch_url(self, session: aiohttp.ClientSession, url: str) -> Optional[str]:
        """Fazer requisição HTTP com retry"""
        # Validar URL
        if not URLValidator.is_valid_url(url):
            logger.error(f"URL inválida: {url}")
            return None
        
        headers = {"User-Agent": self.user_agent}
        
        for attempt in range(self.max_retries):
            try:
                await self.rate_limiter.wait()
                
                async with session.get(
                    url,
                    headers=headers,
                    timeout=self.timeout,
                    ssl=False
                ) as response:
                    if response.status == 200:
                        logger.info(f"✓ Fetched: {url}")
                        return await response.text()
                    else:
                        logger.warning(f"Status {response.status}: {url}")
                        
            except asyncio.TimeoutError:
                logger.warning(f"Timeout (attempt {attempt + 1}/{self.max_retries}): {url}")
            except aiohttp.ClientError as e:
                logger.warning(f"Error (attempt {attempt + 1}/{self.max_retries}): {url} - {str(e)}")
            except Exception as e:
                logger.warning(f"Unexpected error (attempt {attempt + 1}/{self.max_retries}): {url} - {str(e)}")
            
            if attempt < self.max_retries - 1:
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
        
        logger.error(f"✗ Failed after {self.max_retries} attempts: {url}")
        return None
    
    async def scrape_articles(self, urls: List[str]) -> List[Article]:
        """Scraper múltiplas URLs em paralelo"""
        self.stats.status = ScraperStatus.RUNNING
        
        # Filtrar URLs válidas
        valid_urls = [url for url in urls if URLValidator.is_valid_url(url)]
        
        if not valid_urls:
            logger.error("Nenhuma URL válida fornecida")
            self.stats.status = ScraperStatus.FAILED
            return []
        
        self.stats.total_items = len(valid_urls)
        start_time = time.time()
        
        articles = []
        
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                tasks = [self._scrape_single_url(session, url) for url in valid_urls]
                results = await asyncio.gather(*tasks, return_exceptions=True)
                
                for result in results:
                    if isinstance(result, Article):
                        articles.append(result)
                        self.stats.successful_items += 1
                    elif isinstance(result, Exception):
                        self.stats.failed_items += 1
                        logger.error(f"Exception during scraping: {result}")
                    else:
                        self.stats.failed_items += 1
        
        except Exception as e:
            logger.error(f"Erro crítico durante scraping: {e}")
            self.stats.failed_items += len(valid_urls) - len(articles)
            self.stats.status = ScraperStatus.FAILED
            return articles
        
        # Calcular estatísticas
        elapsed_time = time.time() - start_time
        self.stats.total_time = elapsed_time
        self.stats.items_per_second = self.stats.successful_items / elapsed_time if elapsed_time > 0 else 0
        self.stats.status = ScraperStatus.COMPLETED
        
        return articles
    
    async def _scrape_single_url(self, session: aiohttp.ClientSession, url: str) -> Optional[Article]:
        """Scraper uma URL individual"""
        try:
            html = await self.fetch_url(session, url)
            if not html:
                return None
            
            soup = BeautifulSoup(html, 'html.parser')
            
            # Extrair título
            title_tag = soup.find('h1') or soup.find('title')
            title = title_tag.get_text(strip=True) if title_tag else "N/A"
            
            # Limpar título
            title = title[:200] if len(title) > 200 else title
            
            # Extrair autor (exemplo genérico)
            author_tag = soup.find('meta', {'name': 'author'})
            author = author_tag.get('content') if author_tag else None
            
            # Extrair data de publicação
            date_tag = soup.find('meta', {'property': 'article:published_time'})
            published_date = date_tag.get('content') if date_tag else None
            
            # Extrair resumo/descrição
            summary_tag = soup.find('meta', {'name': 'description'})
            summary = summary_tag.get('content') if summary_tag else None
            
            # Limpar resumo
            summary = summary[:500] if summary and len(summary) > 500 else summary
            
            article = Article(
                title=title,
                url=url,
                author=author,
                published_date=published_date,
                summary=summary
            )
            
            return article
            
        except Exception as e:
            logger.error(f"Error scraping {url}: {str(e)}")
            return None
    
    def get_stats(self) -> Dict:
        """Obter estatísticas de scraping"""
        return asdict(self.stats)
    
    def save_results(self, articles: List[Article], filename: str = "scraping_results.json") -> Path:
        """Salvar resultados em JSON com suporte a Windows"""
        try:
            stats = self.get_stats()
            stats_dict = dict(stats)
            stats_dict['status'] = stats_dict['status'].value
            
            output = {
                "timestamp": datetime.utcnow().isoformat(),
                "articles": [asdict(a) for a in articles],
                "statistics": stats_dict
            }
            
            output_path = self.output_dir / filename
            
            # Usar encoding utf-8 explicitamente para Windows
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Resultados salvos em '{output_path}'")
            return output_path
            
        except Exception as e:
            logger.error(f"Erro ao salvar resultados: {e}")
            raise


# ============================================================================
# EXEMPLO DE USO
# ============================================================================

async def main():
    """Exemplo de uso do scraper"""
    
    # URLs de exemplo (sites públicos)
    urls = [
        "https://news.ycombinator.com",
        "https://www.reddit.com/r/programming",
        "https://www.techcrunch.com",
    ]
    
    print("=" * 80)
    print("WEB SCRAPER PROFISSIONAL - EXEMPLO DE USO")
    print(f"Sistema Operacional: {platform.system()}")
    print("=" * 80)
    
    # Criar scraper
    scraper = WebScraper(requests_per_second=2.0, timeout=10, max_retries=3)
    
    print(f"\n📊 Iniciando scraping de {len(urls)} URLs...")
    print(f"⏱️  Rate limit: 2 requisições/segundo")
    print(f"🔄 Máximo de tentativas: 3\n")
    
    # Executar scraping
    articles = await scraper.scrape_articles(urls)
    
    # Exibir resultados
    print("\n" + "=" * 80)
    print("RESULTADOS")
    print("=" * 80)
    
    for i, article in enumerate(articles, 1):
        print(f"\n📄 Artigo {i}:")
        print(f"   Título: {article.title[:60]}...")
        print(f"   URL: {article.url}")
        print(f"   Autor: {article.author or 'N/A'}")
        print(f"   Data: {article.published_date or 'N/A'}")
        print(f"   Resumo: {(article.summary or 'N/A')[:60]}...")
    
    # Exibir estatísticas
    stats = scraper.get_stats()
    print("\n" + "=" * 80)
    print("ESTATÍSTICAS")
    print("=" * 80)
    print(f"Total de URLs: {stats['total_items']}")
    print(f"Sucesso: {stats['successful_items']}")
    print(f"Falhas: {stats['failed_items']}")
    print(f"Tempo total: {stats['total_time']:.2f}s")
    print(f"Taxa média: {stats['items_per_second']:.2f} itens/segundo")
    print(f"Status: {stats['status'].value}")
    
    # Salvar resultados em JSON
    try:
        output_path = scraper.save_results(articles)
        print(f"\n✅ Resultados salvos em '{output_path}'")
    except Exception as e:
        print(f"\n❌ Erro ao salvar resultados: {e}")


if __name__ == "__main__":
    # Suporte melhorado para Windows
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Scraping interrompido pelo usuário")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Erro fatal: {e}")
        sys.exit(1)
