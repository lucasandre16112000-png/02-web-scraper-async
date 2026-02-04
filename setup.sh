#!/bin/bash

# Script de configuração do Web Scraper para Linux/macOS
# Execute com: bash setup.sh ou chmod +x setup.sh && ./setup.sh

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Funções de output
print_header() {
    echo ""
    echo "================================================================================"
    echo "$1"
    echo "================================================================================"
    echo ""
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Função para tratar erros
handle_error() {
    print_error "$1"
    exit 1
}

# Verificar Python
print_header "Verificando Python"

if ! command -v python3 &> /dev/null; then
    handle_error "Python 3 não encontrado. Instale Python 3.8 ou superior"
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
print_info "Python $PYTHON_VERSION encontrado"

# Verificar versão mínima
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    handle_error "Python 3.8 ou superior é necessário"
fi

print_success "Versão do Python compatível"

# Criar ambiente virtual
print_header "Criando ambiente virtual"

if [ -d "venv" ]; then
    print_info "Ambiente virtual já existe"
else
    python3 -m venv venv || handle_error "Erro ao criar ambiente virtual"
    print_success "Ambiente virtual criado"
fi

# Ativar ambiente virtual
print_header "Ativando ambiente virtual"

source venv/bin/activate || handle_error "Erro ao ativar ambiente virtual"
print_success "Ambiente virtual ativado"

# Instalar dependências
print_header "Instalando dependências"

print_info "Atualizando pip..."
pip install --upgrade pip > /dev/null 2>&1

print_info "Instalando pacotes necessários..."
pip install -r requirements.txt || handle_error "Erro ao instalar dependências"

print_success "Dependências instaladas com sucesso"

# Criar diretório de logs
print_header "Criando diretórios necessários"

mkdir -p logs || handle_error "Erro ao criar diretório de logs"
print_success "Diretórios criados"

# Criar arquivo .env
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        print_success "Arquivo .env criado"
    fi
fi

# Executar testes
print_header "Executando testes"

python test_scraper.py || print_error "Alguns testes falharam, mas a instalação pode estar completa"

# Próximos passos
print_header "PRÓXIMOS PASSOS"

echo -e "${BLUE}1. O ambiente virtual já está ativado${NC}"
echo ""
echo -e "${BLUE}2. Execute o scraper:${NC}"
echo "   python scraper.py"
echo ""
echo -e "${BLUE}3. Ou execute o exemplo com URLs customizadas:${NC}"
echo "   python example_urls.py"
echo ""
echo -e "${BLUE}4. Para executar os testes novamente:${NC}"
echo "   python test_scraper.py"
echo ""
echo -e "${BLUE}5. Para ativar o ambiente virtual em outro terminal:${NC}"
echo "   source venv/bin/activate"
echo ""

print_header "✅ CONFIGURAÇÃO CONCLUÍDA COM SUCESSO!"
