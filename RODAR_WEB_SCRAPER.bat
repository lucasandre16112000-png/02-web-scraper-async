@echo off
REM ============================================================================
REM Web Scraper PRO V4 - Launcher Windows Batch
REM Clique 2 vezes e tudo funciona automaticamente!
REM ============================================================================

setlocal enabledelayedexpansion

REM Cores e formatação
cls
echo.
echo ============================================================================
echo.
echo   ^^!^^! WEB SCRAPER PRO V4 - LAUNCHER WINDOWS ^^!^^!
echo.
echo   Clique 2 vezes e deixe a magia acontecer...
echo.
echo ============================================================================
echo.

REM Configurações
set REPO_URL=https://github.com/lucasandre16112000-png/02-web-scraper-async.git
set PROJECT_NAME=02-web-scraper-async
set HOME_DIR=%USERPROFILE%
set PROJECT_DIR=%HOME_DIR%\%PROJECT_NAME%
set VENV_DIR=%PROJECT_DIR%\venv
set PYTHON_EXE=%VENV_DIR%\Scripts\python.exe
set PIP_EXE=%VENV_DIR%\Scripts\pip.exe

REM ============================================================================
REM 1. VERIFICAR PYTHON
REM ============================================================================
echo [*] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Python nao esta instalado!
    echo.
    echo Por favor, instale Python de:
    echo https://www.python.org/downloads/
    echo.
    echo Certifique-se de marcar "Add Python to PATH" durante a instalacao!
    echo.
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo [OK] %PYTHON_VERSION% encontrado!
echo.

REM ============================================================================
REM 2. VERIFICAR GIT
REM ============================================================================
echo [*] Verificando Git...
git --version >nul 2>&1
if errorlevel 1 (
    echo [X] Git nao esta instalado!
    echo.
    echo Por favor, instale Git de:
    echo https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('git --version') do set GIT_VERSION=%%i
echo [OK] %GIT_VERSION% encontrado!
echo.

REM ============================================================================
REM 3. CLONAR/ATUALIZAR REPOSITÓRIO
REM ============================================================================
echo [*] Preparando repositorio...
if exist "%PROJECT_DIR%" (
    echo [OK] Pasta ja existe: %PROJECT_DIR%
    echo [*] Atualizando repositorio...
    cd /d "%PROJECT_DIR%"
    git pull origin main >nul 2>&1
    echo [OK] Repositorio atualizado!
) else (
    echo [*] Clonando repositorio do GitHub...
    git clone %REPO_URL% "%PROJECT_DIR%" >nul 2>&1
    if errorlevel 1 (
        echo [X] Erro ao clonar repositorio!
        pause
        exit /b 1
    )
    echo [OK] Repositorio clonado com sucesso!
)
echo.

REM ============================================================================
REM 4. CRIAR AMBIENTE VIRTUAL
REM ============================================================================
if exist "%VENV_DIR%" (
    echo [OK] Ambiente virtual ja existe
) else (
    echo [*] Criando ambiente virtual...
    cd /d "%PROJECT_DIR%"
    python -m venv venv >nul 2>&1
    if errorlevel 1 (
        echo [X] Erro ao criar ambiente virtual!
        pause
        exit /b 1
    )
    echo [OK] Ambiente virtual criado!
)
echo.

REM ============================================================================
REM 5. INSTALAR DEPENDÊNCIAS
REM ============================================================================
echo [*] Instalando dependencias...
cd /d "%PROJECT_DIR%"

REM Upgrade pip
echo [*] Atualizando pip...
%PYTHON_EXE% -m pip install --upgrade pip >nul 2>&1

REM Instalar requirements
echo [*] Instalando pacotes necessarios...
%PIP_EXE% install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo [X] Erro ao instalar dependencias!
    pause
    exit /b 1
)
echo [OK] Dependencias instaladas!
echo.

REM ============================================================================
REM 6. INICIAR SERVIDOR
REM ============================================================================
echo ============================================================================
echo.
echo [OK] TUDO PRONTO!
echo.
echo [*] Iniciando Web Scraper PRO V4...
echo [*] O navegador abrira automaticamente em alguns segundos...
echo.
echo ============================================================================
echo.

REM Aguardar um pouco
timeout /t 2 /nobreak >nul

REM Rodar servidor (sem mostrar janela do console)
cd /d "%PROJECT_DIR%"
start "" %PYTHON_EXE% server_pro_v4.py

REM Aguardar servidor iniciar (mais tempo para evitar duplicação)
timeout /t 5 /nobreak >nul

REM Aguardar um pouco mais
timeout /t 2 /nobreak >nul

echo.
echo ============================================================================
echo.
echo [OK] SERVIDOR INICIADO!
echo.
echo Dicas de uso:
echo   - Clique em "Iniciar Scraping PRO" para comcar
echo   - Aguarde os dados serem coletados
echo   - Os graficos aparecem em tempo real
echo   - Feche o navegador para parar o servidor
echo.
echo ============================================================================
echo.

REM Manter janela aberta
pause

exit /b 0
