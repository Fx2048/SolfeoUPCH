
"""
# !/bin/bash
# Script para ejecutar todas las pruebas

echo
"==================================="
echo
"Suite de Pruebas - Algoritmia"
echo
"==================================="

# Colores
GREEN = '\033[0;32m'
RED = '\033[0;31m'
NC = '\033[0m'  # No Color

# Función para ejecutar un test
run_test()
{
    local
name =$1
local
code =$2
local
expected =$3

echo - n
"Test: $name ... "

# Crear archivo temporal
echo
"$code" > test_temp.alg

# Ejecutar
output =$(python3 algoritmia.py test_temp.alg 2 > & 1)

# Verificar
if echo
"$output" | grep - q
"$expected";
then
echo - e
"${GREEN}OK${NC}"
return 0
else
echo - e
"${RED}FAIL${NC}"
echo
"  Esperado: $expected"
echo
"  Obtenido: $output"
return 1
fi
}

# Test 1: Hello World
run_test
"Hello World" \
'Main |: <w> "Hello" :|' \
"Hello"

# Test 2: Aritmética
run_test
"Aritmética básica" \
'Main |: a <- 5 b <- 3 <w> a + b :|' \
"8"

# Test 3: Condicional
run_test
"Condicional" \
'Main |: x <- 10 if x > 5 |: <w> "Mayor" :| :|' \
"Mayor"

# Test 4: Lista
run_test
"Listas" \
'Main |: lista <- {1 2 3} <w> #lista :|' \
"3"

# Limpiar
rm - f
test_temp.alg
test_temp.pdf
test_temp.midi
test_temp.wav
test_temp.ly

echo
"==================================="
echo
"Pruebas completadas"
echo
"===================================" \
"""