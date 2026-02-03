"""
Script de configuração automática do Web Scraper
Funciona em Windows, macOS e Linux
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


def print_header(text):
    """Imprimir cabeçalho"""
    print("\n" + "=" * 80)
    print(text)
    print("=" * 80 + "\n")


def print_success(text):
    """Imprimir mensagem de sucesso"""
    print(f"✅ {text}")


def print_error(text):
    """Imprimir mensagem de erro"""
    print(f"❌ {text}")


def print_info(text):
    """Imprimir mensagem de informação"""
    print(f"ℹ️  {text}")


def check_python_version():
    """Verificar versão do Python"""
    print_header("Verificando versão do Python")
    
    version = sys.version_info
    print_info(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error("Python 3.8 ou superior é necessário!")
        return False
    
    print_success("Versão do Python compatível")
    return True


def check_git():
    """Verificar se Git está instalado"""
    print_header("Verificando Git")
    
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        print_success("Git está instalado")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_error("Git não está instalado")
        print_info("Instale Git em: https://git-scm.com/downloads")
        return False


def create_virtual_environment():
    """Criar ambiente virtual"""
    print_header("Criando ambiente virtual")
    
    venv_path = Path("venv")
    
    if venv_path.exists():
        print_info("Ambiente virtual já existe")
        return True
    
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print_success("Ambiente virtual criado")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Erro ao criar ambiente virtual: {e}")
        return False


def get_pip_command():
    """Obter comando pip para o ambiente virtual"""
    if platform.system() == "Windows":
        return Path("venv") / "Scripts" / "pip"
    else:
        return Path("venv") / "bin" / "pip"


def get_python_command():
    """Obter comando python para o ambiente virtual"""
    if platform.system() == "Windows":
        return Path("venv") / "Scripts" / "python"
    else:
        return Path("venv") / "bin" / "python"


def install_dependencies():
    """Instalar dependências"""
    print_header("Instalando dependências")
    
    pip_cmd = get_pip_command()
    
    try:
        # Atualizar pip
        print_info("Atualizando pip...")
        subprocess.run([str(pip_cmd), "install", "--upgrade", "pip"], check=True)
        
        # Instalar dependências
        print_info("Instalando pacotes necessários...")
        subprocess.run([str(pip_cmd), "install", "-r", "requirements.txt"], check=True)
        
        print_success("Dependências instaladas com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Erro ao instalar dependências: {e}")
        return False


def run_tests():
    """Executar testes"""
    print_header("Executando testes")
    
    python_cmd = get_python_command()
    
    try:
        subprocess.run([str(python_cmd), "test_scraper.py"], check=True)
        print_success("Testes executados com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Alguns testes falharam: {e}")
        return False


def create_env_file():
    """Criar arquivo .env a partir do .env.example"""
    print_header("Configurando arquivo .env")
    
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if env_file.exists():
        print_info("Arquivo .env já existe")
        return True
    
    if env_example.exists():
        try:
            env_file.write_text(env_example.read_text())
            print_success("Arquivo .env criado a partir de .env.example")
            return True
        except Exception as e:
            print_error(f"Erro ao criar .env: {e}")
            return False
    else:
        print_info(".env.example não encontrado")
        return True


def create_logs_directory():
    """Criar diretório de logs"""
    print_header("Criando diretório de logs")
    
    logs_dir = Path("logs")
    
    try:
        logs_dir.mkdir(exist_ok=True)
        print_success("Diretório de logs criado")
        return True
    except Exception as e:
        print_error(f"Erro ao criar diretório de logs: {e}")
        return False


def print_next_steps():
    """Imprimir próximos passos"""
    print_header("Próximos passos")
    
    if platform.system() == "Windows":
        activate_cmd = ".\\venv\\Scripts\\activate"
    else:
        activate_cmd = "source venv/bin/activate"
    
    print_info(f"1. Ative o ambiente virtual:")
    print(f"   {activate_cmd}\n")
    
    print_info("2. Execute o scraper:")
    print("   python scraper.py\n")
    
    print_info("3. Ou execute o exemplo com URLs customizadas:")
    print("   python example_urls.py\n")
    
    print_info("4. Para executar os testes novamente:")
    print("   python test_scraper.py\n")


def main():
    """Função principal"""
    print_header("CONFIGURAÇÃO DO WEB SCRAPER")
    print_info(f"Sistema Operacional: {platform.system()}")
    print_info(f"Python: {sys.version}")
    
    # Verificações
    if not check_python_version():
        return False
    
    # Criar ambiente virtual
    if not create_virtual_environment():
        return False
    
    # Instalar dependências
    if not install_dependencies():
        return False
    
    # Criar arquivo .env
    if not create_env_file():
        return False
    
    # Criar diretório de logs
    if not create_logs_directory():
        return False
    
    # Executar testes
    print_info("Executando testes para verificar a instalação...")
    if not run_tests():
        print_error("Alguns testes falharam, mas a instalação pode estar completa")
    
    # Próximos passos
    print_next_steps()
    
    print_header("✅ CONFIGURAÇÃO CONCLUÍDA COM SUCESSO!")
    return True


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Configuração interrompida pelo usuário")
        sys.exit(1)
    except Exception as e:
        print_error(f"Erro inesperado: {e}")
        sys.exit(1)
