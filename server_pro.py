"""
Servidor Web Profissional PRO - Dashboard Avançado
Integração completa com scraper avançado
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
from scraper_pro import AdvancedWebScraper

PORT = 8000
HOST = "localhost"

# Variáveis globais
scraping_data = {
    "status": "idle",
    "message": "Pronto para iniciar",
    "progress": 0,
    "articles": [],
    "statistics": {},
    "analysis": {},
    "timestamp": datetime.now().isoformat()
}

class ScraperProHandler(http.server.SimpleHTTPRequestHandler):
    """Handler customizado para servidor PRO"""
    
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
            if scraping_data["status"] == "scraping":
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Scraping já em andamento"}).encode())
                return
            
            thread = threading.Thread(target=run_scraper_pro)
            thread.daemon = True
            thread.start()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "Scraping iniciado"}).encode())
            return
        
        # Servir dashboard por padrão
        if self.path == '/' or self.path == '/dashboard':
            self.path = '/dashboard_pro.html'
        
        return super().do_GET()
    
    def end_headers(self):
        """Adicionar headers"""
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Log customizado"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def run_scraper_pro():
    """Executar scraper PRO"""
    global scraping_data
    
    try:
        scraping_data["status"] = "scraping"
        scraping_data["message"] = "Iniciando scraper PRO..."
        scraping_data["progress"] = 10
        
        # Criar scraper
        scraper = AdvancedWebScraper(output_dir=".")
        
        print("\n" + "="*80)
        print("🚀 SCRAPER PRO - VERSÃO AVANÇADA")
        print("="*80 + "\n")
        
        scraping_data["progress"] = 30
        scraping_data["message"] = "Coletando dados de múltiplas fontes..."
        
        # Rodar asyncio
        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            articles = loop.run_until_complete(scraper.scrape_articles())
        finally:
            loop.close()
        
        scraping_data["progress"] = 80
        scraping_data["message"] = "Processando análises avançadas..."
        
        # Carregar resultados
        if os.path.exists("scraping_results_pro.json"):
            with open("scraping_results_pro.json", "r", encoding="utf-8") as f:
                results = json.load(f)
                scraping_data["articles"] = results.get("articles", [])
                scraping_data["statistics"] = results.get("statistics", {})
                scraping_data["timestamp"] = results.get("timestamp", datetime.now().isoformat())
        
        scraping_data["progress"] = 100
        scraping_data["status"] = "completed"
        scraping_data["message"] = "✅ Scraper PRO concluído com sucesso!"
        
        print("\n" + "="*80)
        print("✅ SCRAPER PRO CONCLUÍDO!")
        print("="*80 + "\n")
        
    except Exception as e:
        scraping_data["status"] = "error"
        scraping_data["message"] = f"❌ Erro: {str(e)}"
        scraping_data["progress"] = 0
        print(f"\n❌ Erro: {e}\n")

def start_server_pro():
    """Iniciar servidor PRO"""
    
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("\n" + "="*80)
    print("🌐 SERVIDOR WEB PROFISSIONAL PRO - PORTFÓLIO AVANÇADO")
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
    
    with socketserver.TCPServer(("", PORT), ScraperProHandler) as httpd:
        try:
            webbrowser.open(f"http://{HOST}:{PORT}/")
        except Exception as e:
            print(f"⚠️  Não foi possível abrir o navegador: {e}")
            print(f"Abra manualmente: http://{HOST}:{PORT}/")
        
        print("\n🕷️  Iniciando scraper PRO automaticamente...\n")
        thread = threading.Thread(target=run_scraper_pro)
        thread.daemon = True
        thread.start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n⏹️  Servidor parado pelo usuário")
            sys.exit(0)

if __name__ == "__main__":
    start_server_pro()
