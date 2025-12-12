"""
Testes unitários para o Web Scraper
Verifica se todas as funcionalidades estão funcionando corretamente
"""

import asyncio
import unittest
from scraper import WebScraper, RateLimiter, Article, ScraperStatus
from dataclasses import asdict
import time


class TestRateLimiter(unittest.TestCase):
    """Testes para a classe RateLimiter"""
    
    def test_rate_limiter_initialization(self):
        """Testa se o RateLimiter é inicializado corretamente"""
        limiter = RateLimiter(requests_per_second=2.0)
        self.assertEqual(limiter.requests_per_second, 2.0)
        self.assertEqual(limiter.min_interval, 0.5)
    
    def test_rate_limiter_wait(self):
        """Testa se o RateLimiter aguarda corretamente"""
        async def test():
            limiter = RateLimiter(requests_per_second=2.0)
            start = time.time()
            await limiter.wait()
            await limiter.wait()
            elapsed = time.time() - start
            # Deve ter esperado pelo menos 0.5 segundos
            self.assertGreaterEqual(elapsed, 0.4)
        
        asyncio.run(test())


class TestArticle(unittest.TestCase):
    """Testes para a classe Article"""
    
    def test_article_creation(self):
        """Testa se um Article é criado corretamente"""
        article = Article(
            title="Test Title",
            url="https://example.com",
            author="Test Author"
        )
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.url, "https://example.com")
        self.assertEqual(article.author, "Test Author")
        self.assertIsNotNone(article.scraped_at)
    
    def test_article_to_dict(self):
        """Testa se um Article pode ser convertido para dicionário"""
        article = Article(
            title="Test Title",
            url="https://example.com"
        )
        article_dict = asdict(article)
        self.assertIsInstance(article_dict, dict)
        self.assertEqual(article_dict['title'], "Test Title")
        self.assertEqual(article_dict['url'], "https://example.com")


class TestWebScraper(unittest.TestCase):
    """Testes para a classe WebScraper"""
    
    def test_scraper_initialization(self):
        """Testa se o WebScraper é inicializado corretamente"""
        scraper = WebScraper(
            requests_per_second=2.0,
            timeout=10,
            max_retries=3
        )
        self.assertEqual(scraper.rate_limiter.requests_per_second, 2.0)
        self.assertEqual(scraper.timeout.total, 10)
        self.assertEqual(scraper.max_retries, 3)
    
    def test_scraper_stats_initialization(self):
        """Testa se as estatísticas são inicializadas corretamente"""
        scraper = WebScraper()
        stats = scraper.get_stats()
        self.assertEqual(stats['total_items'], 0)
        self.assertEqual(stats['successful_items'], 0)
        self.assertEqual(stats['failed_items'], 0)
        self.assertEqual(stats['status'].value, 'pending')
    
    def test_scraper_with_empty_urls(self):
        """Testa o scraper com uma lista vazia de URLs"""
        async def test():
            scraper = WebScraper()
            articles = await scraper.scrape_articles([])
            self.assertEqual(len(articles), 0)
            stats = scraper.get_stats()
            self.assertEqual(stats['total_items'], 0)
        
        asyncio.run(test())


class TestIntegration(unittest.TestCase):
    """Testes de integração"""
    
    def test_scraper_with_valid_url(self):
        """Testa o scraper com uma URL válida"""
        async def test():
            scraper = WebScraper(
                requests_per_second=1.0,
                timeout=10,
                max_retries=2
            )
            # Usar uma URL que é conhecida por ser estável
            urls = ["https://example.com"]
            articles = await scraper.scrape_articles(urls)
            
            stats = scraper.get_stats()
            self.assertEqual(stats['total_items'], 1)
            self.assertGreaterEqual(stats['successful_items'] + stats['failed_items'], 1)
        
        asyncio.run(test())


def run_tests():
    """Executa todos os testes"""
    print("=" * 80)
    print("EXECUTANDO TESTES DO WEB SCRAPER")
    print("=" * 80)
    
    # Criar suite de testes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Adicionar testes
    suite.addTests(loader.loadTestsFromTestCase(TestRateLimiter))
    suite.addTests(loader.loadTestsFromTestCase(TestArticle))
    suite.addTests(loader.loadTestsFromTestCase(TestWebScraper))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Executar testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 80)
    if result.wasSuccessful():
        print("✅ TODOS OS TESTES PASSARAM COM SUCESSO!")
    else:
        print("❌ ALGUNS TESTES FALHARAM")
        print(f"Falhas: {len(result.failures)}")
        print(f"Erros: {len(result.errors)}")
    print("=" * 80)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
