#!/usr/bin/env python3
"""
Script de pruebas simplificado para Algoritmia (compatible con Windows)
"""

import subprocess
import os
import sys
from datetime import datetime


def print_separator(char='=', length=60):
    """Imprime un separador"""
    print(char * length)


def run_test(test_file, test_name, input_data=None):
    """Ejecuta un test individual"""
    if not os.path.exists(test_file):
        return False, "", f"Archivo {test_file} no encontrado"

    print(f"\n► Ejecutando: {test_name}")
    print(f"  Archivo: {test_file}")

    try:
        process = subprocess.Popen(
            ['python', 'algoritmia.py', test_file],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if input_data:
            stdout, stderr = process.communicate(input=input_data, timeout=10)
        else:
            stdout, stderr = process.communicate(timeout=10)

        if process.returncode != 0 or "Error" in stderr:
            print(f"  ✗ FALLO")
            if stderr:
                print(f"  Error: {stderr[:200]}")
            return False, stdout, stderr
        else:
            print(f"  ✓ EXITO")

            base_name = test_file.replace('.alg', '')
            files_generated = []

            if os.path.exists(f"{base_name}.pdf"):
                files_generated.append("PDF")
            if os.path.exists(f"{base_name}.mid"):
                files_generated.append("MIDI")
            if os.path.exists(f"{base_name}.wav"):
                files_generated.append("WAV")

            if files_generated:
                print(f"  Archivos: {', '.join(files_generated)}")

            return True, stdout, stderr

    except subprocess.TimeoutExpired:
        print(f"  ✗ TIMEOUT")
        process.kill()
        return False, "", "Timeout"
    except Exception as e:
        print(f"  ✗ ERROR: {str(e)}")
        return False, "", str(e)


def main():
    """Ejecuta todos los tests"""

    print_separator()
    print("SUITE DE PRUEBAS - ALGORITMIA".center(60))
    print_separator()
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if not os.path.exists('algoritmia.py'):
        print("Error: No se encontro algoritmia.py")
        sys.exit(1)

    # Definir tests
    tests = [
        ('examples.alg', 'Ejemplo basico', None),
        ('test_listas.alg', 'Operaciones con listas', None),
        ('test_escalas.alg', 'Escalas musicales', None),
        ('test_melodia.alg', 'Composicion musical', None),
        ('test_hanoi_musical.alg', 'Torres de Hanoi musical', None),
        ('test_factorial.alg', 'Factorial', None),
        ('test_euclides.alg', 'Algoritmo de Euclides', '48\n18\n'),
    ]

    print("\n")
    print_separator('-')
    print("Ejecutando Tests")
    print_separator('-')

    results = []
    for test_file, test_name, input_data in tests:
        success, stdout, stderr = run_test(test_file, test_name, input_data)
        results.append((test_name, test_file, success))

    # Reporte
    print("\n")
    print_separator('-')
    print("Reporte Final")
    print_separator('-')

    total = len(results)
    passed = sum(1 for _, _, success in results if success)
    failed = total - passed

    print(f"\nTotal: {total} | Exitosos: {passed} | Fallidos: {failed}")
    print(f"Tasa de exito: {(passed / total * 100):.1f}%")

    if failed > 0:
        print("\nTests fallidos:")
        for name, file, success in results:
            if not success:
                print(f"  ✗ {name} ({file})")

    if passed > 0:
        print("\nTests exitosos:")
        for name, _, success in results:
            if success:
                print(f"  ✓ {name}")

    print("\n")
    print_separator()

    if failed == 0:
        print("¡Todos los tests pasaron! 🎉")
    else:
        print(f"{failed} test(s) fallaron")

    print_separator()

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nTests interrumpidos")
        sys.exit(1)