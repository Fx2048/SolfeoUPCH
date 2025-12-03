@echo off
REM Script para ejecutar todos los tests en Windows
REM Proyecto Algoritmia

echo ============================================================
echo        SUITE DE PRUEBAS - ALGORITMIA
echo ============================================================
echo.

REM Verificar que existe Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    pause
    exit /b 1
)

REM Verificar que existe el interprete
if not exist algoritmia.py (
    echo ERROR: No se encontro algoritmia.py
    pause
    exit /b 1
)

echo Ejecutando script de pruebas...
echo.

REM Ejecutar el script de Python
python run_tests_simple.py

echo.
echo ============================================================
echo                   PRUEBAS COMPLETADAS
echo ============================================================
echo.

pause