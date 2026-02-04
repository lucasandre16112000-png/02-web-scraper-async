"""
Servidor Web Profissional PRO V4 - COM ROTAÇÃO DE SITES
Integração completa com scraper V4
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
import traceback

PORT = 8000
HOST = "localhost"

scraping_data = {
    "status": "idle",
    "message": "Pronto para iniciar",
    "progress": 0,
    "articles": [],
    "statistics": {},
    "timestamp": datetime.now().isoformat()
}

class ScraperProHandler(http.server.SimpleHTTPRequestHandler):
    """Handler customizado para servidor PRO V4"""
    
    def do_GET(self):
        """Tratar requisições GET"""
        global scraping_data
        
        if self.path == '/api/scraping-data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(scraping_data, ensure_ascii=False).encode('utf-8'))
            return
        
        if self.path == '/api/start-scraping':
            if scraping_data["status"] == "scraping":
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Scraping já em andamento"}).encode())
                return
            
            print("\n🚀 INICIANDO SCRAPER V4...")
            thread = threading.Thread(target=run_scraper_pro_v4, daemon=True)
            thread.start()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "Scraping iniciado"}).encode())
            return
        
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
        pass

def run_scraper_pro_v4():
    """Executar scraper PRO V4"""
    global scraping_data
    
    try:
        scraping_data["status"] = "scraping"
        scraping_data["message"] = "Iniciando scraper PRO V4..."
        scraping_data["progress"] = 10
        scraping_data["articles"] = []
        scraping_data["statistics"] = {}
        
        from scraper_pro_v4 import AdvancedWebScraperV4
        
        print("\n" + "="*80)
        print("🚀 WEB SCRAPER PRO V4 - COM ROTAÇÃO DE SITES")
        print("="*80 + "\n")
        
        scraping_data["progress"] = 20
        scraping_data["message"] = "Selecionando fontes aleatórias..."
        
        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            scraper = AdvancedWebScraperV4(output_dir=".")
            articles = loop.run_until_complete(scraper.scrape_articles())
        finally:
            loop.close()
        
        scraping_data["progress"] = 80
        scraping_data["message"] = "Processando análises avançadas..."
        
        if os.path.exists("scraping_results_pro.json"):
            with open("scraping_results_pro.json", "r", encoding="utf-8") as f:
                results = json.load(f)
                scraping_data["articles"] = results.get("articles", [])
                scraping_data["statistics"] = results.get("statistics", {})
                scraping_data["timestamp"] = results.get("timestamp", datetime.now().isoformat())
        
        scraping_data["progress"] = 100
        scraping_data["status"] = "completed"
        scraping_data["message"] = f"✅ Scraper PRO V4 concluído! {len(scraping_data['articles'])} artigos de fontes diferentes!"
        
        print("\n" + "="*80)
        print(f"✅ SCRAPER PRO V4 CONCLUÍDO! {len(scraping_data['articles'])} ARTIGOS DE FONTES DIFERENTES!")
        print("="*80 + "\n")
        
    except Exception as e:
        scraping_data["status"] = "error"
        scraping_data["message"] = f"❌ Erro: {str(e)}"
        scraping_data["progress"] = 0
        print(f"\n❌ Erro: {e}\n")
        traceback.print_exc()

def start_server_pro():
    """Iniciar servidor PRO V4"""
    
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("\n" + "="*80)
    print("🌐 SERVIDOR WEB PROFISSIONAL PRO V4 - COM ROTAÇÃO DE SITES")
    print("="*80)
    print()
    print(f"✅ Servidor iniciado em: http://{HOST}:{PORT}")
    print()
    print("🌍 Abrindo no navegador...")
    print()
    print("⏹️  Pressione CTRL+C para parar o servidor")
    print()
    print("="*80 + "\n")
    
    with socketserver.TCPServer(("", PORT), ScraperProHandler) as httpd:
        try:
            # Não abrir navegador automaticamente - deixar para o launcher
            pass
        except Exception as e:
            pass
        
        print("\n✅ Servidor rodando! Clique no botão no dashboard para iniciar o scraper!\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n⏹️  Servidor parado pelo usuário")
            sys.exit(0)

if __name__ == "__main__":
    start_server_pro()
