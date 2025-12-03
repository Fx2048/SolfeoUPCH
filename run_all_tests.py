#!/usr/bin/env python3
"""
Script de pruebas automatizadas para Algoritmia
Ejecuta todos los archivos de prueba y genera un reporte
"""

import subprocess
import os
import sys
from datetime import datetime


# Colores para la salida en terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_header(text):
    """Imprime un encabezado formateado"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'=' * 60}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}{text:^60}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'=' * 60}{Colors.END}\n")


def print_section(text):
    """Imprime una sección"""
    print(f"\n{Colors.BLUE}{Colors.BOLD}{'─' * 60}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}{text}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}{'─' * 60}{Colors.END}")


def run_test(test_file, test_name, input_data=None):
    """
    Ejecuta un test individual

    Args:
        test_file: Nombre del archivo .alg a ejecutar
        test_name: Nombre descriptivo del test
        input_data: Datos de entrada para tests interactivos (opcional)

    Returns:
        Tuple (success, output, error)
    """
    if not os.path.exists(test_file):
        return False, "", f"Archivo {test_file} no encontrado"

    print(f"{Colors.YELLOW}► Ejecutando: {Colors.END}{test_name}")
    print(f"  Archivo: {test_file}")

    try:
        # Ejecutar el intérprete
        process = subprocess.Popen(
            ['python', 'algoritmia.py', test_file],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Pasar input si es necesario
        if input_data:
            stdout, stderr = process.communicate(input=input_data, timeout=10)
        else:
            stdout, stderr = process.communicate(timeout=10)

        # Verificar si hubo errores
        if process.returncode != 0 or "Error" in stderr:
            print(f"  {Colors.RED}✗ FALLÓ{Colors.END}")
            if stderr:
                print(f"  Error: {stderr[:200]}")
            return False, stdout, stderr
        else:
            print(f"  {Colors.GREEN}✓ ÉXITO{Colors.END}")

            # Verificar archivos generados
            base_name = test_file.replace('.alg', '')
            files_generated = []

            if os.path.exists(f"{base_name}.pdf"):
                files_generated.append("PDF")
            if os.path.exists(f"{base_name}.mid"):
                files_generated.append("MIDI")
            if os.path.exists(f"{base_name}.wav"):
                files_generated.append("WAV")

            if files_generated:
                print(f"  Archivos generados: {', '.join(files_generated)}")

            return True, stdout, stderr

    except subprocess.TimeoutExpired:
        print(f"  {Colors.RED}✗ TIMEOUT (excedió 10 segundos){Colors.END}")
        process.kill()
        return False, "", "Timeout"
    except Exception as e:
        print(f"  {Colors.RED}✗ ERROR: {str(e)}{Colors.END}")
        return False, "", str(e)


def clean_output_files():
    """Limpia archivos de salida anteriores"""
    extensions = ['.pdf', '.mid', '.midi', '.wav', '.ly', '.ps']
    cleaned = 0

    for file in os.listdir('.'):
        if any(file.endswith(ext) for ext in extensions):
            # No eliminar archivos de ejemplo importantes
            if not file.startswith('example'):
                try:
                    os.remove(file)
                    cleaned += 1
                except:
                    pass

    return cleaned


def main():
    """Función principal que ejecuta todos los tests"""

    print_header("SUITE DE PRUEBAS - ALGORITMIA")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Verificar que existe el intérprete
    if not os.path.exists('algoritmia.py'):
        print(f"{Colors.RED}Error: No se encontró algoritmia.py{Colors.END}")
        sys.exit(1)

    # Limpiar archivos de salida anteriores
    print_section("Preparación")
    cleaned = clean_output_files()
    print(f"Archivos de salida anteriores limpiados: {cleaned}")

    # Definir tests
    tests = [
        {
            'file': 'examples.alg',
            'name': 'Ejemplo básico - Hello Algoritmia',
            'input': None
        },
        {
            'file': 'test_listas.alg',
            'name': 'Operaciones con listas',
            'input': None
        },
        {
            'file': 'test_escalas.alg',
            'name': 'Generador de escalas musicales',
            'input': None
        },
        {
            'file': 'test_melodia.alg',
            'name': 'Composición musical compleja',
            'input': None
        },
        {
            'file': 'test_hanoi_musical.alg',
            'name': 'Torres de Hanoi con música',
            'input': None
        },
        {
            'file': 'test_factorial.alg',
            'name': 'Cálculo de factorial',
            'input': None
        },
        {
            'file': 'test_euclides.alg',
            'name': 'Algoritmo de Euclides (MCD)',
            'input': '48\n18\n'  # Input automático: 48 y 18
        },
    ]

    # Ejecutar tests
    print_section("Ejecutando Tests")
    results = []

    for test in tests:
        success, stdout, stderr = run_test(
            test['file'],
            test['name'],
            test.get('input')
        )
        results.append({
            'name': test['name'],
            'file': test['file'],
            'success': success,
            'stdout': stdout,
            'stderr': stderr
        })

    # Reporte final
    print_section("Reporte Final")

    total = len(results)
    passed = sum(1 for r in results if r['success'])
    failed = total - passed
    success_rate = (passed / total * 100) if total > 0 else 0

    print(f"\n{Colors.BOLD}Resultados:{Colors.END}")
    print(f"  Total de tests: {total}")
    print(f"  {Colors.GREEN}✓ Exitosos: {passed}{Colors.END}")
    print(f"  {Colors.RED}✗ Fallidos: {failed}{Colors.END}")
    print(f"  Tasa de éxito: {success_rate:.1f}%")

    # Detalle de tests fallidos
    if failed > 0:
        print(f"\n{Colors.RED}{Colors.BOLD}Tests fallidos:{Colors.END}")
        for result in results:
            if not result['success']:
                print(f"  ✗ {result['name']} ({result['file']})")
                if result['stderr']:
                    print(f"    Error: {result['stderr'][:150]}")

    # Detalle de tests exitosos
    if passed > 0:
        print(f"\n{Colors.GREEN}{Colors.BOLD}Tests exitosos:{Colors.END}")
        for result in results:
            if result['success']:
                print(f"  ✓ {result['name']}")

    # Verificar archivos generados
    print_section("Archivos Generados")
    output_files = {
        'PDF': [],
        'MIDI': [],
        'WAV': []
    }

    for file in os.listdir('.'):
        if file.endswith('.pdf'):
            output_files['PDF'].append(file)
        elif file.endswith('.mid') or file.endswith('.midi'):
            output_files['MIDI'].append(file)
        elif file.endswith('.wav'):
            output_files['WAV'].append(file)

    for file_type, files in output_files.items():
        if files:
            print(f"\n{file_type} ({len(files)}):")
            for f in files:
                size = os.path.getsize(f) / 1024  # KB
                print(f"  • {f} ({size:.1f} KB)")

    # Mensaje final
    print_header("Pruebas Completadas")

    if failed == 0:
        print(f"{Colors.GREEN}{Colors.BOLD}¡Todos los tests pasaron exitosamente! 🎉{Colors.END}\n")
        return 0
    else:
        print(f"{Colors.YELLOW}Algunos tests fallaron. Revisa los errores arriba.{Colors.END}\n")
        return 1


if __name__ == '__main__':
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Tests interrumpidos por el usuario{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
        sys.exit(1)