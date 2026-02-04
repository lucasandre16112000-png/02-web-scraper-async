"""
Web Scraper PRO V4 - VERSÃO FINAL COM ROTAÇÃO DE SITES
Seleciona diferentes sites a cada execução para variedade
30+ fontes disponíveis, sempre diferentes!
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
import random

# Configuração de logging
log_dir = Path.cwd() / "logs"
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / "scraper_pro_v4.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Configuração de asyncio para Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class AdvancedWebScraperV4:
    """Web Scraper Profissional Avançado V4 - COM ROTAÇÃO DE SITES"""
    
    def __init__(self, output_dir: str = "."):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.session = None
        self.articles = []
        
        # 30+ URLs - BANCO COMPLETO DE FONTES
        self.all_urls = {
            # Tech News
            "Hacker News": "https://news.ycombinator.com",
            "TechCrunch": "https://www.techcrunch.com",
            "The Verge": "https://www.theverge.com",
            "Wired": "https://www.wired.com",
            "Ars Technica": "https://arstechnica.com",
            "AnandTech": "https://www.anandtech.com",
            
            # Programming & Development
            "Reddit r/programming": "https://www.reddit.com/r/programming",
            "Dev.to": "https://dev.to",
            "Medium Tech": "https://medium.com/tag/technology",
            "CSS Tricks": "https://css-tricks.com",
            "Smashing Magazine": "https://www.smashingmagazine.com",
            "A List Apart": "https://alistapart.com",
            
            # Product & Startup
            "Product Hunt": "https://www.producthunt.com",
            "Indie Hackers": "https://www.indiehackers.com",
            "Y Combinator": "https://news.ycombinator.com/newest",
            
            # Open Source & Community
            "GitHub Trending": "https://github.com/trending",
            "Lobsters": "https://lobste.rs",
            "Hacker News New": "https://news.ycombinator.com/newest",
            
            # Tech Analysis & Opinion
            "Slashdot": "https://slashdot.org",
            "InfoQ": "https://www.infoq.com",
            "Dzone": "https://www.dzone.com",
            "SitePoint": "https://www.sitepoint.com",
            
            # Design & UX
            "Web Designer Depot": "https://www.webdesignerdepot.com",
            "Dribbble": "https://dribbble.com",
            "Designer Hangout": "https://www.designerhangout.co",
            
            # Learning & Tutorials
            "FreeCodeCamp": "https://www.freecodecamp.org",
            "Scotch.io": "https://scotch.io",
            "Egghead": "https://egghead.io",
            
            # Code Showcase
            "Codepen": "https://codepen.io",
            "Codesignal": "https://codesignal.com",
        }
    
    def get_random_urls(self, num_sources: int = 12) -> Dict[str, str]:
        """Selecionar URLs aleatórias do banco de fontes"""
        available_sources = list(self.all_urls.items())
        selected = random.sample(available_sources, min(num_sources, len(available_sources)))
        return dict(selected)
    
    async def scrape_articles(self, custom_urls: Optional[Dict[str, str]] = None) -> List[Dict]:
        """Fazer scraping de múltiplos sites"""
        
        # Se não forneceu URLs, selecionar aleatoriamente
        if custom_urls is None:
            urls_to_scrape = self.get_random_urls(num_sources=12)
        else:
            urls_to_scrape = custom_urls
        
        print("\n" + "="*80)
        print("🚀 WEB SCRAPER PRO V4 - VERSÃO FINAL COM ROTAÇÃO DE SITES")
        print("="*80)
        print(f"\n📡 Selecionadas {len(urls_to_scrape)} fontes diferentes para esta execução:\n")
        for source in urls_to_scrape.keys():
            print(f"   • {source}")
        print("\n" + "="*80 + "\n")
        
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
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            
            async with self.session.get(url, headers=headers, timeout=15, ssl=False) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    articles = self._extract_articles_advanced(soup, source, url)
                    print(f"✅ {source}: {len(articles)} artigos extraídos")
                    return articles
                else:
                    print(f"⚠️  {source}: Status {response.status}")
                    return []
        
        except Exception as e:
            print(f"❌ Erro em {source}: {str(e)[:50]}")
            logger.error(f"Erro ao fazer scraping de {source}: {e}")
            return []
    
    def _extract_articles_advanced(self, soup: BeautifulSoup, source: str, url: str) -> List[Dict]:
        """Extração avançada de artigos"""
        articles = []
        
        try:
            # Procurar por diferentes tipos de elementos
            article_selectors = [
                soup.find_all('article'),
                soup.find_all('div', class_=re.compile(r'(post|article|item|card|entry|story)', re.I)),
                soup.find_all('li', class_=re.compile(r'(post|article|item|card)', re.I)),
                soup.find_all('div', class_=re.compile(r'(content|main|feed)', re.I)),
            ]
            
            article_elements = []
            for selector in article_selectors:
                if selector:
                    article_elements.extend(selector)
                    if len(article_elements) >= 15:
                        break
            
            # Remover duplicatas
            article_elements = list(set(article_elements))[:15]
            
            for elem in article_elements:
                try:
                    article_data = self._extract_single_article_v4(elem, source)
                    if article_data and article_data.get('title') and len(article_data.get('title', '')) > 5:
                        articles.append(article_data)
                except Exception as e:
                    logger.debug(f"Erro ao extrair artigo: {e}")
                    continue
        
        except Exception as e:
            logger.error(f"Erro ao extrair artigos de {source}: {e}")
        
        return articles[:10]  # Top 10 por fonte
    
    def _extract_single_article_v4(self, elem, source: str) -> Optional[Dict]:
        """Extração avançada de artigo individual"""
        try:
            # Extrair título
            title = self._extract_title(elem)
            if not title or len(title) < 5:
                return None
            
            # Extrair URL
            url = self._extract_url(elem)
            
            # Extrair resumo
            summary = self._extract_summary(elem)
            
            # Extrair autor
            author = self._extract_author(elem)
            
            # Extrair data
            published_date = self._extract_date(elem)
            
            # Extrair conteúdo
            content = self._extract_content(elem)
            
            # Extrair métricas
            views, likes, comments, shares = self._extract_metrics(elem)
            
            # Calcular engagement
            engagement_score = self._calculate_engagement(views, likes, comments, shares)
            
            # Análise de sentimento
            sentiment = self._analyze_sentiment(title + " " + (summary or ""))
            
            # Categorização inteligente
            category = self._categorize_smart(title, summary, content, source)
            
            # Extrair tags
            tags = self._extract_tags(title, summary, source)
            
            # Extrair palavras-chave
            keywords = self._extract_keywords(title + " " + (summary or ""))
            
            # Extrair imagem
            image_url = self._extract_image(elem)
            
            return {
                "title": title,
                "url": url or source,
                "source": source,
                "author": author,
                "published_date": published_date,
                "summary": summary,
                "content": content,
                "category": category,
                "tags": tags,
                "views": views,
                "likes": likes,
                "comments": comments,
                "shares": shares,
                "engagement_score": round(engagement_score, 2),
                "sentiment": sentiment,
                "keywords": keywords,
                "image_url": image_url,
                "word_count": len((content or "").split()),
                "reading_time": max(1, len((content or "").split()) // 200),
                "scraped_at": datetime.utcnow().isoformat()
            }
        
        except Exception as e:
            logger.debug(f"Erro ao extrair artigo: {e}")
            return None
    
    def _extract_title(self, elem) -> Optional[str]:
        """Extrair título"""
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5']:
            title_elem = elem.find(tag)
            if title_elem:
                title = title_elem.get_text(strip=True)
                if title and len(title) > 5 and len(title) < 500:
                    return title
        return None
    
    def _extract_url(self, elem) -> Optional[str]:
        """Extrair URL"""
        link = elem.find('a', href=True)
        if link:
            url = link.get('href', '')
            if url and (url.startswith('http') or url.startswith('/')):
                return url
        return None
    
    def _extract_summary(self, elem) -> Optional[str]:
        """Extrair resumo/descrição"""
        for class_name in ['summary', 'description', 'excerpt', 'content', 'lead', 'intro']:
            summary_elem = elem.find(class_=re.compile(class_name, re.I))
            if summary_elem:
                summary = summary_elem.get_text(strip=True)
                if summary and len(summary) > 10 and len(summary) < 1000:
                    return summary
        
        p_elem = elem.find('p')
        if p_elem:
            summary = p_elem.get_text(strip=True)
            if summary and len(summary) > 10 and len(summary) < 1000:
                return summary
        
        return None
    
    def _extract_author(self, elem) -> Optional[str]:
        """Extrair autor"""
        for class_name in ['author', 'by', 'user', 'writer', 'creator']:
            author_elem = elem.find(class_=re.compile(class_name, re.I))
            if author_elem:
                author = author_elem.get_text(strip=True)
                if author and len(author) < 100 and len(author) > 2:
                    return author
        return None
    
    def _extract_date(self, elem) -> Optional[str]:
        """Extrair data"""
        time_elem = elem.find('time')
        if time_elem:
            date = time_elem.get_text(strip=True)
            if date:
                return date
        
        for class_name in ['date', 'time', 'published', 'posted']:
            date_elem = elem.find(class_=re.compile(class_name, re.I))
            if date_elem:
                date = date_elem.get_text(strip=True)
                if date and len(date) < 100:
                    return date
        
        return None
    
    def _extract_content(self, elem) -> Optional[str]:
        """Extrair conteúdo completo"""
        for script in elem(["script", "style"]):
            script.decompose()
        
        for class_name in ['content', 'body', 'article-body', 'post-content', 'entry-content']:
            content_elem = elem.find(class_=re.compile(class_name, re.I))
            if content_elem:
                content = content_elem.get_text(strip=True)
                if content and len(content) > 50:
                    return content[:2000]
        
        return None
    
    def _extract_metrics(self, elem) -> tuple:
        """Extrair métricas"""
        views = likes = comments = shares = 0
        
        text_content = elem.get_text().lower()
        numbers = re.findall(r'(\d+)\s*(views?|likes?|comments?|shares?|upvotes?|points?)', text_content)
        
        for num, metric_type in numbers:
            try:
                num = int(num)
                if num > 0 and num < 10000000:
                    if 'view' in metric_type:
                        views = max(views, num)
                    elif 'like' in metric_type or 'upvote' in metric_type:
                        likes = max(likes, num)
                    elif 'comment' in metric_type:
                        comments = max(comments, num)
                    elif 'share' in metric_type:
                        shares = max(shares, num)
                    elif 'point' in metric_type:
                        likes = max(likes, num)
            except:
                pass
        
        return views, likes, comments, shares
    
    def _calculate_engagement(self, views: int, likes: int, comments: int, shares: int) -> float:
        """Calcular score de engajamento"""
        if views > 0:
            return ((likes * 1 + comments * 2 + shares * 3) / views) * 100
        elif likes > 0 or comments > 0 or shares > 0:
            return float(likes + comments * 2 + shares * 3)
        return 0.0
    
    def _analyze_sentiment(self, text: str) -> str:
        """Análise de sentimento"""
        positive_words = ['excelente', 'ótimo', 'incrível', 'fantástico', 'melhor', 'sucesso', 'ganho', 'novo', 'inovação', 'revolucionário', 'amazing', 'awesome', 'great', 'excellent', 'best']
        negative_words = ['ruim', 'péssimo', 'horrível', 'fracasso', 'perda', 'problema', 'erro', 'bug', 'falha', 'crítica', 'bad', 'terrible', 'worst', 'fail', 'issue']
        
        text_lower = text.lower()
        
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"
    
    def _categorize_smart(self, title: str, summary: str, content: str, source: str) -> str:
        """Categorização inteligente"""
        text = (title + " " + (summary or "") + " " + (content or "") + " " + source).lower()
        
        categories = {
            "AI/ML": ['ai', 'machine learning', 'neural', 'deep learning', 'nlp', 'gpt', 'transformer', 'model', 'algorithm', 'data science'],
            "Web Development": ['web', 'html', 'css', 'javascript', 'react', 'vue', 'angular', 'frontend', 'backend', 'nodejs', 'typescript'],
            "Mobile": ['mobile', 'app', 'ios', 'android', 'flutter', 'react native', 'swift', 'kotlin'],
            "Cloud": ['cloud', 'aws', 'azure', 'gcp', 'kubernetes', 'docker', 'devops', 'infrastructure'],
            "Security": ['security', 'hack', 'cyber', 'encryption', 'vulnerability', 'exploit', 'breach', 'ssl'],
            "Database": ['database', 'sql', 'nosql', 'mongodb', 'postgresql', 'mysql', 'redis', 'elasticsearch'],
            "DevOps": ['devops', 'ci/cd', 'jenkins', 'gitlab', 'github actions', 'terraform', 'ansible'],
            "Startups": ['startup', 'funding', 'investment', 'venture', 'series a', 'ipo', 'acquisition'],
            "Design": ['design', 'ui', 'ux', 'figma', 'adobe', 'css', 'animation', 'responsive'],
            "Performance": ['performance', 'optimization', 'speed', 'benchmark', 'profiling', 'caching'],
            "Testing": ['testing', 'test', 'qa', 'selenium', 'jest', 'pytest', 'unit test'],
            "Programming": ['programming', 'code', 'coding', 'python', 'java', 'c++', 'rust', 'golang'],
        }
        
        for category, keywords in categories.items():
            if any(keyword in text for keyword in keywords):
                return category
        
        return "Technology"
    
    def _extract_tags(self, title: str, summary: str, source: str) -> List[str]:
        """Extrair tags"""
        tags = []
        text = (title + " " + (summary or "") + " " + source).lower()
        
        tag_keywords = {
            'python': ['python'],
            'javascript': ['javascript', 'js', 'typescript'],
            'ai': ['ai', 'artificial intelligence', 'machine learning'],
            'web': ['web', 'html', 'css'],
            'mobile': ['mobile', 'app'],
            'startup': ['startup', 'funding'],
            'tech': ['tech', 'technology'],
            'news': ['news', 'announcement'],
            'tutorial': ['tutorial', 'guide', 'how to'],
            'review': ['review', 'analysis'],
        }
        
        for tag, keywords in tag_keywords.items():
            if any(keyword in text for keyword in keywords):
                tags.append(tag)
        
        return tags if tags else ['general']
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extrair palavras-chave"""
        words = text.lower().split()
        stop_words = {'o', 'a', 'de', 'da', 'do', 'e', 'é', 'em', 'para', 'com', 'por', 'um', 'uma', 'os', 'as', 'dos', 'das', 'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'is', 'are', 'was', 'be'}
        keywords = [w for w in words if len(w) > 3 and w not in stop_words and w.isalpha()]
        return list(set(keywords))[:8]
    
    def _extract_image(self, elem) -> Optional[str]:
        """Extrair URL de imagem"""
        img = elem.find('img')
        if img:
            src = img.get('src', '')
            if src and (src.startswith('http') or src.startswith('/')):
                return src
        return None
    
    def _perform_advanced_analysis(self):
        """Realizar análises avançadas"""
        if not self.articles:
            print("⚠️  Nenhum artigo foi coletado!")
            return
        
        print("\n" + "="*80)
        print("📊 ANÁLISES AVANÇADAS")
        print("="*80 + "\n")
        
        sources_count = Counter(a['source'] for a in self.articles)
        print("📰 Artigos por Fonte:")
        for source, count in sources_count.most_common():
            print(f"   {source}: {count} artigos")
        
        categories = Counter(a['category'] for a in self.articles)
        print("\n📂 Artigos por Categoria:")
        for category, count in categories.most_common():
            print(f"   {category}: {count} artigos")
        
        sentiments = Counter(a['sentiment'] for a in self.articles)
        print("\n😊 Análise de Sentimento:")
        for sentiment, count in sentiments.most_common():
            print(f"   {sentiment.capitalize()}: {count} artigos")
        
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
    scraper = AdvancedWebScraperV4()
    articles = await scraper.scrape_articles()
    
    print("\n" + "="*80)
    print(f"✅ SCRAPING CONCLUÍDO! {len(articles)} ARTIGOS COLETADOS!")
    print("="*80 + "\n")
    
    return articles


if __name__ == "__main__":
    asyncio.run(main())
