"""
Servidor Web Simples para o Dashboard
Execute este arquivo para abrir o dashboard em http://localhost:8000
"""

import http.server
import socketserver
import os
import webbrowser
import sys
from pathlib import Path

PORT = 8000
HOST = "localhost"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handler customizado para servir arquivos"""
    
    def end_headers(self):
        """Adicionar headers para evitar cache"""
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Log customizado"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def start_server():
    """Iniciar o servidor web"""
    
    # Mudar para o diretório do script
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("=" * 80)
    print("🌐 SERVIDOR WEB - DASHBOARD")
    print("=" * 80)
    print()
    print(f"✅ Servidor iniciado em: http://{HOST}:{PORT}")
    print()
    print("📂 Arquivos sendo servidos de:", script_dir)
    print()
    print("🌍 Abrindo no navegador...")
    print()
    print("⏹️  Pressione CTRL+C para parar o servidor")
    print()
    print("=" * 80)
    print()
    
    # Criar socket server
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        # Abrir no navegador
        try:
            webbrowser.open(f"http://{HOST}:{PORT}/dashboard.html")
        except Exception as e:
            print(f"⚠️  Não foi possível abrir o navegador automaticamente: {e}")
            print(f"Abra manualmente: http://{HOST}:{PORT}/dashboard.html")
        
        # Servir
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n⏹️  Servidor parado pelo usuário")
            sys.exit(0)

if __name__ == "__main__":
    start_server()
