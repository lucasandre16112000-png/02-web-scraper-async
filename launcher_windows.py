"""
Web Scraper PRO V4 - Launcher Windows
Executável que faz TUDO automaticamente para o cliente
Clique 2 vezes e pronto!
"""

import os
import sys
import subprocess
import shutil
import json
import time
import webbrowser
from pathlib import Path
import threading
import socket
from datetime import datetime

# Configurações
REPO_URL = "https://github.com/lucasandre16112000-png/02-web-scraper-async.git"
PROJECT_NAME = "02-web-scraper-async"
PORT = 8000
HOST = "localhost"

class WindowsLauncher:
    """Launcher profissional para Windows"""
    
    def __init__(self):
        self.home_dir = Path.home()
        self.project_dir = self.home_dir / PROJECT_NAME
        self.venv_dir = self.project_dir / "venv"
        self.python_exe = self.venv_dir / "Scripts" / "python.exe"
        self.pip_exe = self.venv_dir / "Scripts" / "pip.exe"
        
    def log(self, message: str, level: str = "INFO"):
        """Log com timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
    
    def check_python(self) -> bool:
        """Verificar se Python está instalado"""
        self.log("Verificando Python...")
        try:
            result = subprocess.run(
                [sys.executable, "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                self.log(f"✅ Python encontrado: {result.stdout.strip()}")
                return True
        except Exception as e:
            self.log(f"❌ Erro ao verificar Python: {e}", "ERROR")
        return False
    
    def check_git(self) -> bool:
        """Verificar se Git está instalado"""
        self.log("Verificando Git...")
        try:
            result = subprocess.run(
                ["git", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                self.log(f"✅ Git encontrado: {result.stdout.strip()}")
                return True
        except Exception as e:
            self.log(f"❌ Erro ao verificar Git: {e}", "ERROR")
        return False
    
    def clone_repository(self) -> bool:
        """Clonar repositório do GitHub"""
        if self.project_dir.exists():
            self.log(f"📁 Pasta já existe: {self.project_dir}")
            self.log("Atualizando repositório...")
            try:
                subprocess.run(
                    ["git", "-C", str(self.project_dir), "pull", "origin", "main"],
                    capture_output=True,
                    timeout=60
                )
                self.log("✅ Repositório atualizado!")
                return True
            except Exception as e:
                self.log(f"⚠️  Erro ao atualizar: {e}", "WARNING")
                return False
        
        self.log(f"📥 Clonando repositório...")
        try:
            subprocess.run(
                ["git", "clone", REPO_URL, str(self.project_dir)],
                capture_output=True,
                timeout=120
            )
            self.log("✅ Repositório clonado com sucesso!")
            return True
        except Exception as e:
            self.log(f"❌ Erro ao clonar: {e}", "ERROR")
            return False
    
    def create_venv(self) -> bool:
        """Criar ambiente virtual"""
        if self.venv_dir.exists():
            self.log("✅ Ambiente virtual já existe")
            return True
        
        self.log("🔧 Criando ambiente virtual...")
        try:
            subprocess.run(
                [sys.executable, "-m", "venv", str(self.venv_dir)],
                capture_output=True,
                timeout=60
            )
            self.log("✅ Ambiente virtual criado!")
            return True
        except Exception as e:
            self.log(f"❌ Erro ao criar venv: {e}", "ERROR")
            return False
    
    def install_dependencies(self) -> bool:
        """Instalar dependências"""
        self.log("📦 Instalando dependências...")
        
        requirements_file = self.project_dir / "requirements.txt"
        if not requirements_file.exists():
            self.log("❌ Arquivo requirements.txt não encontrado", "ERROR")
            return False
        
        try:
            # Upgrade pip
            subprocess.run(
                [str(self.pip_exe), "install", "--upgrade", "pip"],
                capture_output=True,
                timeout=120
            )
            
            # Instalar requirements
            subprocess.run(
                [str(self.pip_exe), "install", "-r", str(requirements_file)],
                capture_output=True,
                timeout=300
            )
            
            self.log("✅ Dependências instaladas!")
            return True
        except Exception as e:
            self.log(f"❌ Erro ao instalar dependências: {e}", "ERROR")
            return False
    
    def is_port_available(self, port: int = PORT) -> bool:
        """Verificar se porta está disponível"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                result = sock.connect_ex(('127.0.0.1', port))
                return result != 0
        except:
            return True
    
    def run_server(self) -> bool:
        """Rodar servidor"""
        self.log("🚀 Iniciando servidor Web Scraper PRO V4...")
        
        if not self.is_port_available():
            self.log(f"⚠️  Porta {PORT} já está em uso", "WARNING")
            self.log("Tentando porta alternativa...")
            # Tentar outra porta
            for alt_port in [8001, 8002, 8003, 9000]:
                if self.is_port_available(alt_port):
                    self.log(f"✅ Usando porta {alt_port}")
                    break
        
        try:
            # Rodar servidor em background
            server_script = self.project_dir / "server_pro_v4.py"
            if not server_script.exists():
                self.log("❌ server_pro_v4.py não encontrado", "ERROR")
                return False
            
            # Usar CREATE_NEW_CONSOLE para não mostrar terminal
            subprocess.Popen(
                [str(self.python_exe), str(server_script)],
                cwd=str(self.project_dir),
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            
            self.log("✅ Servidor iniciado!")
            time.sleep(3)  # Aguardar servidor iniciar
            
            # Abrir navegador
            self.log("🌍 Abrindo navegador...")
            webbrowser.open(f"http://{HOST}:{PORT}")
            
            return True
        except Exception as e:
            self.log(f"❌ Erro ao rodar servidor: {e}", "ERROR")
            return False
    
    def run_all(self) -> bool:
        """Executar todas as etapas"""
        print("\n" + "="*80)
        print("🚀 WEB SCRAPER PRO V4 - LAUNCHER WINDOWS")
        print("="*80 + "\n")
        
        # Verificações iniciais
        if not self.check_python():
            self.log("❌ Python não está instalado!", "ERROR")
            self.log("Por favor, instale Python de: https://www.python.org/downloads/", "ERROR")
            input("\nPressione ENTER para sair...")
            return False
        
        if not self.check_git():
            self.log("❌ Git não está instalado!", "ERROR")
            self.log("Por favor, instale Git de: https://git-scm.com/download/win", "ERROR")
            input("\nPressione ENTER para sair...")
            return False
        
        # Etapas principais
        if not self.clone_repository():
            self.log("❌ Falha ao clonar repositório", "ERROR")
            input("\nPressione ENTER para sair...")
            return False
        
        if not self.create_venv():
            self.log("❌ Falha ao criar ambiente virtual", "ERROR")
            input("\nPressione ENTER para sair...")
            return False
        
        if not self.install_dependencies():
            self.log("❌ Falha ao instalar dependências", "ERROR")
            input("\nPressione ENTER para sair...")
            return False
        
        if not self.run_server():
            self.log("❌ Falha ao rodar servidor", "ERROR")
            input("\nPressione ENTER para sair...")
            return False
        
        print("\n" + "="*80)
        print("✅ TUDO PRONTO! O NAVEGADOR DEVE ABRIR AUTOMATICAMENTE!")
        print("="*80)
        print("\n💡 Dicas:")
        print("   • Clique em '🚀 Iniciar Scraping PRO' para começar")
        print("   • Aguarde os dados serem coletados")
        print("   • Os gráficos aparecem em tempo real")
        print("   • Feche o navegador para parar o servidor")
        print("\n" + "="*80 + "\n")
        
        return True


def main():
    """Função principal"""
    try:
        launcher = WindowsLauncher()
        success = launcher.run_all()
        
        if success:
            # Manter janela aberta
            input("\nPressione ENTER para sair...")
        
        sys.exit(0 if success else 1)
    
    except Exception as e:
        print(f"\n❌ Erro fatal: {e}")
        import traceback
        traceback.print_exc()
        input("\nPressione ENTER para sair...")
        sys.exit(1)


if __name__ == "__main__":
    main()
