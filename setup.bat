@echo off
REM Script de configuração do Web Scraper para Windows
REM Execute este arquivo para configurar o projeto automaticamente

setlocal enabledelayedexpansion

echo.
echo ================================================================================
echo CONFIGURACAO DO WEB SCRAPER - WINDOWS
echo ================================================================================
echo.

REM Verificar Python
echo [1/5] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ❌ Python nao encontrado!
    echo.
    echo Instale Python em: https://www.python.org/downloads/
    echo Importante: Marque "Add Python to PATH" durante a instalacao
    echo.
    pause
    exit /b 1
)
echo ✅ Python encontrado

REM Criar ambiente virtual
echo.
echo [2/5] Criando ambiente virtual...
if exist venv (
    echo ℹ️  Ambiente virtual ja existe
) else (
    python -m venv venv
    if errorlevel 1 (
        echo ❌ Erro ao criar ambiente virtual
        pause
        exit /b 1
    )
    echo ✅ Ambiente virtual criado
)

REM Ativar ambiente virtual
echo.
echo [3/5] Ativando ambiente virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Erro ao ativar ambiente virtual
    pause
    exit /b 1
)
echo ✅ Ambiente virtual ativado

REM Instalar dependências
echo.
echo [4/5] Instalando dependencias...
pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Erro ao instalar dependencias
    pause
    exit /b 1
)
echo ✅ Dependencias instaladas

REM Criar diretório de logs
echo.
echo [5/5] Criando diretorios necessarios...
if not exist logs mkdir logs
echo ✅ Diretorios criados

REM Criar arquivo .env
if not exist .env (
    if exist .env.example (
        copy .env.example .env >nul
        echo ✅ Arquivo .env criado
    )
)

REM Executar testes
echo.
echo ================================================================================
echo Executando testes...
echo ================================================================================
echo.
python test_scraper.py
if errorlevel 1 (
    echo.
    echo ⚠️  Alguns testes falharam, mas a instalacao pode estar completa
    echo.
)

REM Próximos passos
echo.
echo ================================================================================
echo PROXIMOS PASSOS
echo ================================================================================
echo.
echo 1. O ambiente virtual ja esta ativado
echo.
echo 2. Execute o scraper:
echo    python scraper.py
echo.
echo 3. Ou execute o exemplo com URLs customizadas:
echo    python example_urls.py
echo.
echo 4. Para executar os testes novamente:
echo    python test_scraper.py
echo.
echo 5. Para ativar o ambiente virtual em outro terminal:
echo    venv\Scripts\activate
echo.
echo ================================================================================
echo ✅ CONFIGURACAO CONCLUIDA COM SUCESSO!
echo ================================================================================
echo.
pause
