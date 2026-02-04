"""
Web Scraper PRO V2 - VERSÃO SUPER MELHORADA
Coleta dados de 20+ sites com extração robusta e análises avançadas
Totalmente compatível com Windows, macOS e Linux
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
from datetime import datetime
from typing import List, Dict, Optional
import logging
import sys
from pathlib import Path
import platform
import re
from collections import Counter

# Configuração de logging
log_dir = Path.cwd() / "logs"
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / "scraper_pro_v2.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Configuração de asyncio para Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class AdvancedWebScraperV2:
    """Web Scraper Profissional Avançado V2 - SUPER MELHORADO"""
    
    def __init__(self, output_dir: str = "."):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.session = None
        self.articles = []
        
        # 20+ URLs com múltiplas fontes
        self.urls = {
            "Hacker News": "https://news.ycombinator.com",
            "TechCrunch": "https://www.techcrunch.com",
            "Reddit r/programming": "https://www.reddit.com/r/programming",
            "Medium Tech": "https://medium.com/tag/technology",
            "Dev.to": "https://dev.to",
            "Product Hunt": "https://www.producthunt.com",
            "GitHub Trending": "https://github.com/trending",
            "Lobsters": "https://lobste.rs",
            "Slashdot": "https://slashdot.org",
            "InfoQ": "https://www.infoq.com",
            "Dzone": "https://www.dzone.com",
            "CSS Tricks": "https://css-tricks.com",
            "Smashing Magazine": "https://www.smashingmagazine.com",
            "A List Apart": "https://alistapart.com",
            "Web Designer Depot": "https://www.webdesignerdepot.com",
            "SitePoint": "https://www.sitepoint.com",
            "Scotch.io": "https://scotch.io",
            "FreeCodeCamp": "https://www.freecodecamp.org",
            "Codesignal": "https://codesignal.com",
            "Codepen": "https://codepen.io",
        }
    
    async def scrape_articles(self, custom_urls: Optional[Dict[str, str]] = None) -> List[Dict]:
        """Fazer scraping de múltiplos sites com dados avançados"""
        urls_to_scrape = custom_urls or self.urls
        
        print("\n" + "="*80)
        print("🚀 WEB SCRAPER PRO V2 - VERSÃO SUPER MELHORADA")
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
    
    async def _scrape_source(self, source: str, url: str) -> List[Dict]:
        """Fazer scraping de uma fonte específica"""
        try:
            print(f"🔍 Coletando dados de: {source}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            async with self.session.get(url, headers=headers, timeout=15, ssl=False) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    articles = self._extract_articles_generic(soup, source, url)
                    print(f"✅ {source}: {len(articles)} artigos extraídos")
                    return articles
                else:
                    print(f"⚠️  {source}: Status {response.status}")
                    return []
        
        except Exception as e:
            print(f"❌ Erro em {source}: {str(e)[:50]}")
            logger.error(f"Erro ao fazer scraping de {source}: {e}")
            return []
    
    def _extract_articles_generic(self, soup: BeautifulSoup, source: str, url: str) -> List[Dict]:
        """Extração genérica e robusta de artigos"""
        articles = []
        
        try:
            # Estratégia 1: Procurar por tags article
            article_elements = soup.find_all('article')
            if not article_elements:
                # Estratégia 2: Procurar por divs com classe específica
                article_elements = soup.find_all('div', class_=re.compile(r'(post|article|item|card|entry)', re.I))
            
            if not article_elements:
                # Estratégia 3: Procurar por qualquer elemento com h2 ou h3
                article_elements = soup.find_all(['div', 'section', 'li'], limit=20)
            
            for elem in article_elements[:10]:  # Top 10 por fonte
                try:
                    article_data = self._extract_single_article(elem, source)
                    if article_data and article_data.get('title'):
                        articles.append(article_data)
                except Exception as e:
                    logger.debug(f"Erro ao extrair artigo individual: {e}")
                    continue
            
        except Exception as e:
            logger.error(f"Erro ao extrair artigos de {source}: {e}")
        
        return articles
    
    def _extract_single_article(self, elem, source: str) -> Optional[Dict]:
        """Extrair dados de um artigo individual"""
        try:
            # Tentar encontrar título
            title = None
            for tag in ['h1', 'h2', 'h3', 'h4']:
                title_elem = elem.find(tag)
                if title_elem:
                    title = title_elem.get_text(strip=True)
                    if title and len(title) > 5:
                        break
            
            if not title or len(title) < 5:
                return None
            
            # Tentar encontrar URL
            url = None
            link = elem.find('a', href=True)
            if link:
                url = link.get('href', '')
            
            if not url:
                url = source
            
            # Tentar encontrar resumo/descrição
            summary = None
            for tag in ['p', 'span', 'div']:
                summary_elem = elem.find(tag, class_=re.compile(r'(summary|description|excerpt|content)', re.I))
                if summary_elem:
                    summary = summary_elem.get_text(strip=True)
                    if summary and len(summary) > 10:
                        break
            
            if not summary:
                summary_elem = elem.find('p')
                if summary_elem:
                    summary = summary_elem.get_text(strip=True)
            
            # Tentar encontrar autor
            author = None
            for tag in ['span', 'p', 'div']:
                author_elem = elem.find(tag, class_=re.compile(r'(author|by|user)', re.I))
                if author_elem:
                    author = author_elem.get_text(strip=True)
                    if author and len(author) < 50:
                        break
            
            # Tentar encontrar data
            published_date = None
            for tag in ['time', 'span', 'p']:
                date_elem = elem.find(tag, class_=re.compile(r'(date|time|published)', re.I))
                if date_elem:
                    published_date = date_elem.get_text(strip=True)
                    if published_date:
                        break
            
            # Tentar encontrar likes/views
            likes = 0
            views = 0
            for elem_text in elem.find_all(['span', 'div']):
                text = elem_text.get_text(strip=True)
                # Procurar por números
                numbers = re.findall(r'\d+', text)
                if numbers and len(numbers) > 0:
                    try:
                        num = int(numbers[0])
                        if num > 0 and num < 1000000:
                            if 'like' in text.lower() or '👍' in text:
                                likes = num
                            elif 'view' in text.lower() or '👁' in text:
                                views = num
                    except:
                        pass
            
            # Calcular engagement score
            engagement_score = 0.0
            if views > 0:
                engagement_score = ((likes * 1) / views) * 100
            
            # Análise de sentimento básica
            sentiment = self._analyze_sentiment(title + " " + (summary or ""))
            
            # Extrair palavras-chave
            keywords = self._extract_keywords(title + " " + (summary or ""))
            
            return {
                "title": title,
                "url": url,
                "source": source,
                "author": author,
                "published_date": published_date,
                "summary": summary,
                "category": self._categorize(title + " " + (summary or "")),
                "tags": self._extract_tags(title + " " + (summary or "")),
                "views": views,
                "likes": likes,
                "engagement_score": round(engagement_score, 2),
                "sentiment": sentiment,
                "keywords": keywords,
                "scraped_at": datetime.utcnow().isoformat()
            }
        
        except Exception as e:
            logger.debug(f"Erro ao extrair artigo: {e}")
            return None
    
    def _analyze_sentiment(self, text: str) -> str:
        """Análise de sentimento"""
        positive_words = ['excelente', 'ótimo', 'incrível', 'fantástico', 'melhor', 'sucesso', 'ganho', 'novo', 'inovação', 'revolucionário']
        negative_words = ['ruim', 'péssimo', 'horrível', 'fracasso', 'perda', 'problema', 'erro', 'bug', 'falha', 'crítica']
        
        text_lower = text.lower()
        
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extrair palavras-chave"""
        words = text.lower().split()
        stop_words = {'o', 'a', 'de', 'da', 'do', 'e', 'é', 'em', 'para', 'com', 'por', 'um', 'uma', 'os', 'as', 'dos', 'das', 'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        keywords = [w for w in words if len(w) > 3 and w not in stop_words and w.isalpha()]
        return list(set(keywords))[:5]
    
    def _extract_tags(self, text: str) -> List[str]:
        """Extrair tags"""
        tags = []
        if 'python' in text.lower():
            tags.append('python')
        if 'javascript' in text.lower() or 'js' in text.lower():
            tags.append('javascript')
        if 'ai' in text.lower() or 'artificial' in text.lower():
            tags.append('ai')
        if 'web' in text.lower():
            tags.append('web')
        if 'mobile' in text.lower():
            tags.append('mobile')
        if 'startup' in text.lower():
            tags.append('startup')
        if 'tech' in text.lower():
            tags.append('tech')
        return tags if tags else ['general']
    
    def _categorize(self, text: str) -> str:
        """Categorizar artigo"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['startup', 'funding', 'investment', 'venture']):
            return "Startups"
        elif any(word in text_lower for word in ['ai', 'machine learning', 'neural', 'deep learning']):
            return "AI/ML"
        elif any(word in text_lower for word in ['web', 'html', 'css', 'javascript']):
            return "Web"
        elif any(word in text_lower for word in ['mobile', 'app', 'ios', 'android']):
            return "Mobile"
        elif any(word in text_lower for word in ['cloud', 'aws', 'azure', 'kubernetes']):
            return "Cloud"
        elif any(word in text_lower for word in ['security', 'hack', 'cyber']):
            return "Security"
        elif any(word in text_lower for word in ['design', 'ui', 'ux']):
            return "Design"
        else:
            return "Technology"
    
    def _perform_advanced_analysis(self):
        """Realizar análises avançadas"""
        if not self.articles:
            print("⚠️  Nenhum artigo foi coletado!")
            return
        
        print("\n" + "="*80)
        print("📊 ANÁLISES AVANÇADAS")
        print("="*80 + "\n")
        
        # Análise de fontes
        sources_count = Counter(a['source'] for a in self.articles)
        print("📰 Artigos por Fonte:")
        for source, count in sources_count.most_common():
            print(f"   {source}: {count} artigos")
        
        # Análise de categorias
        categories = Counter(a['category'] for a in self.articles)
        print("\n📂 Artigos por Categoria:")
        for category, count in categories.most_common():
            print(f"   {category}: {count} artigos")
        
        # Análise de sentimento
        sentiments = Counter(a['sentiment'] for a in self.articles)
        print("\n😊 Análise de Sentimento:")
        for sentiment, count in sentiments.most_common():
            print(f"   {sentiment.capitalize()}: {count} artigos")
        
        # Top artigos por engajamento
        top_articles = sorted(self.articles, key=lambda x: x['engagement_score'], reverse=True)[:3]
        print("\n🔥 Top Artigos por Engajamento:")
        for i, article in enumerate(top_articles, 1):
            print(f"   {i}. {article['title'][:50]}... (Score: {article['engagement_score']:.2f}%)")
    
    def _save_results(self):
        """Salvar resultados em JSON"""
        results = {
            "timestamp": datetime.utcnow().isoformat(),
            "total_articles": len(self.articles),
            "articles": self.articles,
            "statistics": {
                "total_items": len(self.articles),
                "sources": len(set(a['source'] for a in self.articles)),
                "categories": len(set(a['category'] for a in self.articles)),
                "avg_engagement": round(
                    sum(a['engagement_score'] for a in self.articles) / len(self.articles) if self.articles else 0,
                    2
                ),
                "sentiment_distribution": dict(Counter(a['sentiment'] for a in self.articles))
            }
        }
        
        output_file = self.output_dir / "scraping_results_pro.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Resultados salvos em: {output_file}")


async def main():
    """Função principal"""
    scraper = AdvancedWebScraperV2()
    articles = await scraper.scrape_articles()
    
    print("\n" + "="*80)
    print("✅ SCRAPING CONCLUÍDO COM SUCESSO!")
    print("="*80 + "\n")
    
    return articles


if __name__ == "__main__":
    asyncio.run(main())
