"""
Exemplo de uso do Web Scraper com URLs customizadas
Execute este arquivo para testar o scraper com diferentes URLs
Totalmente compatível com Windows, macOS e Linux
"""

import asyncio
import sys
import platform
from pathlib import Path
from scraper import WebScraper, URLValidator
import json
from datetime import datetime
from dataclasses import asdict

# Configuração de asyncio para Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


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
    print(f"Sistema Operacional: {platform.system()}")
    print("=" * 80)
    
    # Validar URLs
    print("\n🔍 Validando URLs...")
    valid_count = 0
    for url in urls:
        if URLValidator.is_valid_url(url):
            print(f"   ✓ {url}")
            valid_count += 1
        else:
            print(f"   ✗ {url} (inválida)")
    
    if valid_count == 0:
        print("\n❌ Nenhuma URL válida fornecida!")
        sys.exit(1)
    
    # Configurar o scraper com seus próprios parâmetros
    scraper = WebScraper(
        requests_per_second=2.0,  # Máximo de 2 requisições por segundo
        timeout=10,                # Timeout de 10 segundos
        max_retries=3              # Máximo de 3 tentativas por URL
    )
    
    print(f"\n📊 Iniciando scraping de {valid_count} URLs...")
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
    try:
        output_path = scraper.save_results(articles)
        print(f"\n✅ Resultados salvos em '{output_path}'")
        print("\n💡 Dica: Abra o arquivo 'scraping_results.json' para ver os dados em formato JSON")
    except Exception as e:
        print(f"\n❌ Erro ao salvar resultados: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Scraping interrompido pelo usuário")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)
