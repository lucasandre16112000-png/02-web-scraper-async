"""
Web Scraper Profissional Avançado - Versão PRO
Coleta dados avançados com análises, sentimento, tendências e muito mais
Totalmente compatível com Windows, macOS e Linux
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
import re
from collections import Counter
import hashlib

# Configuração de logging
log_dir = Path.cwd() / "logs"
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / "scraper_pro.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Configuração de asyncio para Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@dataclass
class AdvancedArticle:
    """Modelo avançado de artigo com análises"""
    title: str
    url: str
    source: str
    author: Optional[str] = None
    published_date: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: List[str] = None
    views: Optional[int] = None
    likes: Optional[int] = None
    comments: Optional[int] = None
    shares: Optional[int] = None
    engagement_score: float = 0.0
    sentiment: str = "neutral"  # positive, negative, neutral
    keywords: List[str] = None
    language: str = "pt"
    word_count: int = 0
    reading_time: int = 0
    image_url: Optional[str] = None
    scraped_at: str = None
    
    def __post_init__(self):
        if self.scraped_at is None:
            self.scraped_at = datetime.utcnow().isoformat()
        if self.tags is None:
            self.tags = []
        if self.keywords is None:
            self.keywords = []
        
        # Calcular word count
        if self.content:
            self.word_count = len(self.content.split())
            self.reading_time = max(1, self.word_count // 200)
        
        # Calcular engagement score
        self._calculate_engagement_score()
        
        # Analisar sentimento (básico)
        self._analyze_sentiment()
    
    def _calculate_engagement_score(self):
        """Calcular score de engajamento"""
        views = self.views or 0
        likes = self.likes or 0
        comments = self.comments or 0
        shares = self.shares or 0
        
        # Fórmula: (likes * 1 + comments * 2 + shares * 3) / (views + 1)
        if views > 0:
            self.engagement_score = ((likes * 1 + comments * 2 + shares * 3) / views) * 100
        else:
            self.engagement_score = 0.0
    
    def _analyze_sentiment(self):
        """Análise básica de sentimento"""
        positive_words = ['excelente', 'ótimo', 'incrível', 'fantástico', 'melhor', 'sucesso', 'ganho']
        negative_words = ['ruim', 'péssimo', 'horrível', 'fracasso', 'perda', 'problema', 'erro']
        
        text = (self.title + " " + (self.summary or "")).lower()
        
        positive_count = sum(1 for word in positive_words if word in text)
        negative_count = sum(1 for word in negative_words if word in text)
        
        if positive_count > negative_count:
            self.sentiment = "positive"
        elif negative_count > positive_count:
            self.sentiment = "negative"
        else:
            self.sentiment = "neutral"


class AdvancedWebScraper:
    """Web Scraper Profissional Avançado"""
    
    def __init__(self, output_dir: str = "."):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.session = None
        self.articles = []
        
        # URLs expandidas com múltiplas fontes
        self.urls = {
            "Hacker News": "https://news.ycombinator.com",
            "TechCrunch": "https://www.techcrunch.com",
            "Reddit r/programming": "https://www.reddit.com/r/programming",
            "Medium": "https://medium.com/tag/technology",
            "Dev.to": "https://dev.to",
            "Product Hunt": "https://www.producthunt.com",
            "GitHub Trending": "https://github.com/trending",
            "Lobsters": "https://lobste.rs",
            "Slashdot": "https://slashdot.org",
            "InfoQ": "https://www.infoq.com",
        }
    
    async def scrape_articles(self, custom_urls: Optional[Dict[str, str]] = None) -> List[AdvancedArticle]:
        """Fazer scraping de múltiplos sites com dados avançados"""
        urls_to_scrape = custom_urls or self.urls
        
        print("\n" + "="*80)
        print("🚀 WEB SCRAPER PROFISSIONAL AVANÇADO - VERSÃO PRO")
        print("="*80 + "\n")
        
        async with aiohttp.ClientSession() as session:
            self.session = session
            tasks = [
                self._scrape_source(source, url)
                for source, url in urls_to_scrape.items()
            ]
            results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Processar resultados
        for result in results:
            if isinstance(result, list):
                self.articles.extend(result)
            elif isinstance(result, Exception):
                logger.error(f"Erro ao fazer scraping: {result}")
        
        # Análises avançadas
        self._perform_advanced_analysis()
        
        # Salvar resultados
        self._save_results()
        
        return self.articles
    
    async def _scrape_source(self, source: str, url: str) -> List[AdvancedArticle]:
        """Fazer scraping de uma fonte específica"""
        try:
            print(f"🔍 Coletando dados de: {source}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            async with self.session.get(url, headers=headers, timeout=10) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'lxml')
                    
                    articles = self._extract_articles(soup, source, url)
                    print(f"✅ {source}: {len(articles)} artigos extraídos")
                    return articles
                else:
                    print(f"⚠️  {source}: Status {response.status}")
                    return []
        
        except Exception as e:
            print(f"❌ Erro em {source}: {str(e)}")
            logger.error(f"Erro ao fazer scraping de {source}: {e}")
            return []
    
    def _extract_articles(self, soup: BeautifulSoup, source: str, url: str) -> List[AdvancedArticle]:
        """Extrair artigos com dados avançados"""
        articles = []
        
        try:
            # Estratégias diferentes por fonte
            if "hacker" in source.lower():
                articles = self._extract_hackernews(soup, source)
            elif "techcrunch" in source.lower():
                articles = self._extract_techcrunch(soup, source)
            elif "reddit" in source.lower():
                articles = self._extract_reddit(soup, source)
            elif "medium" in source.lower():
                articles = self._extract_medium(soup, source)
            elif "dev.to" in source.lower():
                articles = self._extract_devto(soup, source)
            elif "producthunt" in source.lower():
                articles = self._extract_producthunt(soup, source)
            elif "github" in source.lower():
                articles = self._extract_github(soup, source)
            else:
                articles = self._extract_generic(soup, source)
        
        except Exception as e:
            logger.error(f"Erro ao extrair artigos de {source}: {e}")
        
        return articles
    
    def _extract_hackernews(self, soup: BeautifulSoup, source: str) -> List[AdvancedArticle]:
        """Extrair de Hacker News"""
        articles = []
        rows = soup.find_all('tr', class_='athing')
        
        for row in rows[:5]:  # Top 5
            try:
                title_elem = row.find('span', class_='titleline')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                link = title_elem.find('a')
                url = link.get('href', '') if link else ''
                
                # Pegar metadata (pontos, comentários)
                meta_row = row.find_next('tr')
                meta = meta_row.find('span', class_='score')
                points = 0
                if meta:
                    points = int(meta.get_text(split=True)[0])
                
                article = AdvancedArticle(
                    title=title,
                    url=url,
                    source=source,
                    likes=points,
                    category="Technology",
                    tags=["news", "tech", "trending"]
                )
                articles.append(article)
            except Exception as e:
                logger.error(f"Erro ao extrair artigo de HN: {e}")
        
        return articles
    
    def _extract_techcrunch(self, soup: BeautifulSoup, source: str) -> List[AdvancedArticle]:
        """Extrair de TechCrunch"""
        articles = []
        posts = soup.find_all('div', class_='post-block')
        
        for post in posts[:5]:
            try:
                title_elem = post.find('h2', class_='post-block__title')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                link = post.find('a', class_='post-block__title__link')
                url = link.get('href', '') if link else ''
                
                summary_elem = post.find('p', class_='post-block__content')
                summary = summary_elem.get_text(strip=True) if summary_elem else None
                
                article = AdvancedArticle(
                    title=title,
                    url=url,
                    source=source,
                    summary=summary,
                    category="Startups",
                    tags=["techcrunch", "startup", "funding"]
                )
                articles.append(article)
            except Exception as e:
                logger.error(f"Erro ao extrair artigo de TechCrunch: {e}")
        
        return articles
    
    def _extract_reddit(self, soup: BeautifulSoup, source: str) -> List[AdvancedArticle]:
        """Extrair de Reddit"""
        articles = []
        posts = soup.find_all('div', {'data-testid': 'post'})
        
        for post in posts[:5]:
            try:
                title_elem = post.find('h3')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                link = post.find('a', {'data-testid': 'internal-unauthenticated-comment-link'})
                url = link.get('href', '') if link else ''
                
                # Pegar upvotes
                score_elem = post.find('div', {'aria-label': lambda x: x and 'upvote' in x.lower()})
                upvotes = 0
                if score_elem:
                    try:
                        upvotes = int(score_elem.get_text(strip=True))
                    except:
                        pass
                
                article = AdvancedArticle(
                    title=title,
                    url=url,
                    source=source,
                    likes=upvotes,
                    category="Discussion",
                    tags=["reddit", "programming", "discussion"]
                )
                articles.append(article)
            except Exception as e:
                logger.error(f"Erro ao extrair artigo de Reddit: {e}")
        
        return articles
    
    def _extract_medium(self, soup: BeautifulSoup, source: str) -> List[AdvancedArticle]:
        """Extrair de Medium"""
        articles = []
        articles_elem = soup.find_all('article')
        
        for article_elem in articles_elem[:5]:
            try:
                title_elem = article_elem.find('h2')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                link = article_elem.find('a')
                url = link.get('href', '') if link else ''
                
                article = AdvancedArticle(
                    title=title,
                    url=url,
                    source=source,
                    category="Blog",
                    tags=["medium", "article", "tech"]
                )
                articles.append(article)
            except Exception as e:
                logger.error(f"Erro ao extrair artigo de Medium: {e}")
        
        return articles
    
    def _extract_devto(self, soup: BeautifulSoup, source: str) -> List[AdvancedArticle]:
        """Extrair de Dev.to"""
        articles = []
        articles_elem = soup.find_all('article')
        
        for article_elem in articles_elem[:5]:
            try:
                title_elem = article_elem.find('h2')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                link = article_elem.find('a')
                url = link.get('href', '') if link else ''
                
                article = AdvancedArticle(
                    title=title,
                    url=url,
                    source=source,
                    category="Development",
                    tags=["dev.to", "programming", "tutorial"]
                )
                articles.append(article)
            except Exception as e:
                logger.error(f"Erro ao extrair artigo de Dev.to: {e}")
        
        return articles
    
    def _extract_producthunt(self, soup: BeautifulSoup, source: str) -> List[AdvancedArticle]:
        """Extrair de Product Hunt"""
        articles = []
        products = soup.find_all('div', class_='postCard')
        
        for product in products[:5]:
            try:
                title_elem = product.find('h2')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                link = product.find('a')
                url = link.get('href', '') if link else ''
                
                article = AdvancedArticle(
                    title=title,
                    url=url,
                    source=source,
                    category="Product",
                    tags=["producthunt", "product", "launch"]
                )
                articles.append(article)
            except Exception as e:
                logger.error(f"Erro ao extrair produto de Product Hunt: {e}")
        
        return articles
    
    def _extract_github(self, soup: BeautifulSoup, source: str) -> List[AdvancedArticle]:
        """Extrair de GitHub Trending"""
        articles = []
        repos = soup.find_all('article', class_='Box-row')
        
        for repo in repos[:5]:
            try:
                title_elem = repo.find('h2')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True).strip()
                link = repo.find('a')
                url = link.get('href', '') if link else ''
                
                stars_elem = repo.find('span', class_='d-inline-block float-sm-right')
                stars = 0
                if stars_elem:
                    try:
                        stars = int(stars_elem.get_text(strip=True).split()[0])
                    except:
                        pass
                
                article = AdvancedArticle(
                    title=title,
                    url=url,
                    source=source,
                    likes=stars,
                    category="Repository",
                    tags=["github", "opensource", "trending"]
                )
                articles.append(article)
            except Exception as e:
                logger.error(f"Erro ao extrair repositório do GitHub: {e}")
        
        return articles
    
    def _extract_generic(self, soup: BeautifulSoup, source: str) -> List[AdvancedArticle]:
        """Extração genérica para outras fontes"""
        articles = []
        articles_elem = soup.find_all(['article', 'div'], class_=['post', 'article', 'item'])
        
        for article_elem in articles_elem[:5]:
            try:
                title_elem = article_elem.find(['h1', 'h2', 'h3'])
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                link = article_elem.find('a')
                url = link.get('href', '') if link else ''
                
                article = AdvancedArticle(
                    title=title,
                    url=url,
                    source=source,
                    category="General",
                    tags=["article"]
                )
                articles.append(article)
            except Exception as e:
                logger.error(f"Erro ao extrair artigo genérico: {e}")
        
        return articles
    
    def _perform_advanced_analysis(self):
        """Realizar análises avançadas nos dados coletados"""
        if not self.articles:
            return
        
        print("\n" + "="*80)
        print("📊 ANÁLISES AVANÇADAS")
        print("="*80 + "\n")
        
        # Análise de fontes
        sources_count = Counter(a.source for a in self.articles)
        print("📰 Artigos por Fonte:")
        for source, count in sources_count.most_common():
            print(f"   {source}: {count} artigos")
        
        # Análise de categorias
        categories = Counter(a.category for a in self.articles if a.category)
        print("\n📂 Artigos por Categoria:")
        for category, count in categories.most_common():
            print(f"   {category}: {count} artigos")
        
        # Análise de sentimento
        sentiments = Counter(a.sentiment for a in self.articles)
        print("\n😊 Análise de Sentimento:")
        for sentiment, count in sentiments.most_common():
            print(f"   {sentiment.capitalize()}: {count} artigos")
        
        # Top artigos por engajamento
        top_articles = sorted(self.articles, key=lambda x: x.engagement_score, reverse=True)[:3]
        print("\n🔥 Top Artigos por Engajamento:")
        for i, article in enumerate(top_articles, 1):
            print(f"   {i}. {article.title[:50]}... (Score: {article.engagement_score:.2f})")
    
    def _save_results(self):
        """Salvar resultados em JSON"""
        results = {
            "timestamp": datetime.utcnow().isoformat(),
            "total_articles": len(self.articles),
            "articles": [
                {
                    **asdict(article),
                    "engagement_score": round(article.engagement_score, 2)
                }
                for article in self.articles
            ],
            "statistics": {
                "total_items": len(self.articles),
                "sources": len(set(a.source for a in self.articles)),
                "categories": len(set(a.category for a in self.articles)),
                "avg_engagement": round(
                    sum(a.engagement_score for a in self.articles) / len(self.articles) if self.articles else 0,
                    2
                ),
                "sentiment_distribution": dict(Counter(a.sentiment for a in self.articles))
            }
        }
        
        output_file = self.output_dir / "scraping_results_pro.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Resultados salvos em: {output_file}")


async def main():
    """Função principal"""
    scraper = AdvancedWebScraper()
    articles = await scraper.scrape_articles()
    
    print("\n" + "="*80)
    print("✅ SCRAPING CONCLUÍDO COM SUCESSO!")
    print("="*80 + "\n")
    
    return articles


if __name__ == "__main__":
    asyncio.run(main())
