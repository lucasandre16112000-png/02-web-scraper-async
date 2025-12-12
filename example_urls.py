"""
Exemplo de uso do Web Scraper com URLs customizadas
Execute este arquivo para testar o scraper com diferentes URLs
"""

import asyncio
from scraper import WebScraper
import json
from datetime import datetime
from dataclasses import asdict


async def main():
    """Exemplo com URLs customizadas"""
    
    # Você pode customizar estas URLs com qualquer site público
    urls = [
        "https://news.ycombinator.com",
        "https://www.reddit.com/r/programming",
        "https://www.techcrunch.com",
    ]
    
    print("=" * 80)
    print("WEB SCRAPER ASSÍNCRONO - EXEMPLO CUSTOMIZÁVEL")
    print("=" * 80)
    
    # Configurar o scraper com seus próprios parâmetros
    scraper = WebScraper(
        requests_per_second=2.0,  # Máximo de 2 requisições por segundo
        timeout=10,                # Timeout de 10 segundos
        max_retries=3              # Máximo de 3 tentativas por URL
    )
    
    print(f"\n📊 Iniciando scraping de {len(urls)} URLs...")
    print(f"⏱️  Rate limit: 2 requisições/segundo")
    print(f"🔄 Máximo de tentativas: 3")
    print(f"⏳ Timeout: 10 segundos\n")
    
    # Executar o scraping
    articles = await scraper.scrape_articles(urls)
    
    # Exibir resultados
    print("\n" + "=" * 80)
    print("RESULTADOS DO SCRAPING")
    print("=" * 80)
    
    if articles:
        for i, article in enumerate(articles, 1):
            print(f"\n📄 Artigo {i}:")
            print(f"   Título: {article.title[:70]}...")
            print(f"   URL: {article.url}")
            print(f"   Autor: {article.author or 'Não disponível'}")
            print(f"   Data: {article.published_date or 'Não disponível'}")
            print(f"   Resumo: {(article.summary or 'Não disponível')[:70]}...")
    else:
        print("\n⚠️  Nenhum artigo foi extraído com sucesso.")
    
    # Exibir estatísticas
    stats = scraper.get_stats()
    print("\n" + "=" * 80)
    print("ESTATÍSTICAS")
    print("=" * 80)
    print(f"Total de URLs processadas: {stats['total_items']}")
    print(f"Sucessos: {stats['successful_items']}")
    print(f"Falhas: {stats['failed_items']}")
    print(f"Tempo total: {stats['total_time']:.2f} segundos")
    print(f"Taxa média: {stats['items_per_second']:.2f} itens/segundo")
    print(f"Status: {stats['status'].value}")
    
    # Salvar resultados em JSON
    # Converter stats para dicionário e serializar o status
    stats_dict = dict(stats)
    stats_dict['status'] = stats_dict['status'].value
    
    output = {
        "timestamp": datetime.utcnow().isoformat(),
        "articles": [asdict(a) for a in articles],
        "statistics": stats_dict
    }
    
    with open("scraping_results.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Resultados salvos em 'scraping_results.json'")
    print("\n💡 Dica: Abra o arquivo 'scraping_results.json' para ver os dados em formato JSON")


if __name__ == "__main__":
    asyncio.run(main())
