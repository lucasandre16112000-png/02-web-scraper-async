"""
Servidor Web Profissional com Scraper Integrado
Executa scraper automaticamente e serve dados via API REST
"""

import http.server
import socketserver
import os
import json
import asyncio
import threading
import webbrowser
import sys
from pathlib import Path
from datetime import datetime
from scraper import WebScraper

PORT = 8000
HOST = "localhost"

# Variáveis globais para armazenar dados
scraping_data = {
    "status": "idle",
    "message": "Pronto para iniciar",
    "progress": 0,
    "articles": [],
    "statistics": {
        "total_items": 0,
        "successful_items": 0,
        "failed_items": 0,
        "total_time": 0,
        "items_per_second": 0,
        "status": "idle"
    },
    "timestamp": datetime.now().isoformat()
}

class ScraperHandler(http.server.SimpleHTTPRequestHandler):
    """Handler customizado para servir arquivos e API"""
    
    def do_GET(self):
        """Tratar requisições GET"""
        global scraping_data
        
        # API: Retornar dados do scraper
        if self.path == '/api/scraping-data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(scraping_data).encode())
            return
        
        # API: Iniciar scraping
        if self.path == '/api/start-scraping':
            # Verificar se já está rodando
            if scraping_data["status"] == "scraping":
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Scraping já em andamento"}).encode())
                return
            
            # Iniciar scraping em thread separada
            thread = threading.Thread(target=run_scraper)
            thread.daemon = True
            thread.start()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "Scraping iniciado"}).encode())
            return
        
        # Servir dashboard.html por padrão
        if self.path == '/' or self.path == '/dashboard':
            self.path = '/dashboard.html'
        
        # Servir arquivo estático
        return super().do_GET()
    
    def end_headers(self):
        """Adicionar headers para evitar cache"""
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Log customizado"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def run_scraper():
    """Executar scraper em thread separada"""
    global scraping_data
    
    try:
        scraping_data["status"] = "scraping"
        scraping_data["message"] = "Iniciando scraper..."
        scraping_data["progress"] = 10
        
        # URLs padrão
        urls = [
            "https://news.ycombinator.com",
            "https://www.reddit.com/r/programming",
            "https://www.techcrunch.com"
        ]
        
        # Criar scraper
        scraper = WebScraper(output_dir=".")
        
        # Executar scraper
        print("\n" + "="*80)
        print("🕷️  INICIANDO SCRAPER AUTOMÁTICO")
        print("="*80 + "\n")
        
        scraping_data["progress"] = 30
        scraping_data["message"] = "Fazendo requisições..."
        
        # Rodar asyncio
        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            loop.run_until_complete(scraper.scrape_articles(urls))
        finally:
            loop.close()
        
        scraping_data["progress"] = 80
        scraping_data["message"] = "Processando resultados..."
        
        # Carregar resultados
        if os.path.exists("scraping_results.json"):
            with open("scraping_results.json", "r", encoding="utf-8") as f:
                results = json.load(f)
                scraping_data["articles"] = results.get("articles", [])
                scraping_data["statistics"] = results.get("statistics", {})
                scraping_data["timestamp"] = results.get("timestamp", datetime.now().isoformat())
        
        scraping_data["progress"] = 100
        scraping_data["status"] = "completed"
        scraping_data["message"] = "✅ Scraping concluído com sucesso!"
        
        print("\n" + "="*80)
        print("✅ SCRAPER CONCLUÍDO COM SUCESSO!")
        print("="*80 + "\n")
        
    except Exception as e:
        scraping_data["status"] = "error"
        scraping_data["message"] = f"❌ Erro: {str(e)}"
        scraping_data["progress"] = 0
        print(f"\n❌ Erro no scraper: {e}\n")

def start_server():
    """Iniciar o servidor web"""
    
    # Mudar para o diretório do script
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("\n" + "="*80)
    print("🌐 SERVIDOR WEB PROFISSIONAL - PORTFÓLIO")
    print("="*80)
    print()
    print(f"✅ Servidor iniciado em: http://{HOST}:{PORT}")
    print()
    print("📂 Arquivos sendo servidos de:", script_dir)
    print()
    print("🌍 Abrindo no navegador...")
    print()
    print("⏹️  Pressione CTRL+C para parar o servidor")
    print()
    print("="*80 + "\n")
    
    # Criar socket server
    with socketserver.TCPServer(("", PORT), ScraperHandler) as httpd:
        # Abrir no navegador
        try:
            webbrowser.open(f"http://{HOST}:{PORT}/")
        except Exception as e:
            print(f"⚠️  Não foi possível abrir o navegador automaticamente: {e}")
            print(f"Abra manualmente: http://{HOST}:{PORT}/")
        
        # Iniciar scraper automaticamente
        print("\n🕷️  Iniciando scraper automaticamente...\n")
        thread = threading.Thread(target=run_scraper)
        thread.daemon = True
        thread.start()
        
        # Servir
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n⏹️  Servidor parado pelo usuário")
            sys.exit(0)

if __name__ == "__main__":
    start_server()
