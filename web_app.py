#!/usr/bin/env python3
"""
Aplicación Web para Algoritmia
Interfaz web para ejecutar código Algoritmia
"""

from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import os
import sys
import subprocess
import tempfile
import shutil
from datetime import datetime
import traceback

app = Flask(__name__)
CORS(app)

# Configuración
OUTPUT_DIR = os.path.join('static', 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Ruta a Timidity (ajustar según tu instalación)
TIMIDITY_PATH = r'C:\Users\USER\Downloads\TiMidity++-2.15.0-w32\TiMidity++-2.15.0\timidity.exe'


def clean_old_outputs():
    """Limpia archivos de salida antiguos (más de 1 hora)"""
    try:
        current_time = datetime.now().timestamp()
        for filename in os.listdir(OUTPUT_DIR):
            filepath = os.path.join(OUTPUT_DIR, filename)
            if os.path.isfile(filepath):
                file_time = os.path.getmtime(filepath)
                if current_time - file_time > 3600:  # 1 hora
                    os.remove(filepath)
    except Exception as e:
        print(f"Error limpiando archivos: {e}")


@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')


@app.route('/api/execute', methods=['POST'])
def execute_code():
    """
    Ejecuta código Algoritmia y devuelve resultados
    """
    try:
        data = request.get_json()
        code = data.get('code', '')
        procedure = data.get('procedure', 'Main')
        user_input = data.get('input', '')

        if not code.strip():
            return jsonify({
                'success': False,
                'error': 'El código está vacío'
            })

        # Generar nombre único para archivos
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        temp_filename = f'temp_{timestamp}'
        temp_alg = os.path.join(OUTPUT_DIR, f'{temp_filename}.alg')

        # Guardar código en archivo temporal
        with open(temp_alg, 'w', encoding='utf-8') as f:
            f.write(code)

        # Ejecutar intérprete
        try:
            process = subprocess.Popen(
                ['python', 'algoritmia.py', temp_alg, procedure],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=os.getcwd()
            )

            stdout, stderr = process.communicate(input=user_input, timeout=30)

            # Verificar si hubo errores
            if process.returncode != 0:
                return jsonify({
                    'success': False,
                    'error': stderr or 'Error desconocido',
                    'output': stdout
                })

            # Buscar archivos generados
            base_name = temp_alg.replace('.alg', '')
            generated_files = {}

            # PDF
            pdf_file = f'{base_name}.pdf'
            if os.path.exists(pdf_file):
                # Mover a directorio de salida
                dest_pdf = os.path.join(OUTPUT_DIR, f'{temp_filename}.pdf')
                shutil.move(pdf_file, dest_pdf)
                generated_files['pdf'] = f'/static/outputs/{temp_filename}.pdf'

            # MIDI
            midi_file = f'{base_name}.mid'
            if not os.path.exists(midi_file):
                midi_file = f'{base_name}.midi'

            if os.path.exists(midi_file):
                dest_midi = os.path.join(OUTPUT_DIR, f'{temp_filename}.mid')
                shutil.move(midi_file, dest_midi)
                generated_files['midi'] = f'/static/outputs/{temp_filename}.mid'

            # WAV - generar desde MIDI con Timidity
            if 'midi' in generated_files:
                dest_midi = os.path.join(OUTPUT_DIR, f'{temp_filename}.mid')
                dest_wav = os.path.join(OUTPUT_DIR, f'{temp_filename}.wav')

                try:
                    subprocess.run([
                        TIMIDITY_PATH, '-c', 'NUL', dest_midi,
                        '-Ow', '-o', dest_wav
                    ], check=True, capture_output=True, timeout=10)

                    if os.path.exists(dest_wav):
                        generated_files['wav'] = f'/static/outputs/{temp_filename}.wav'
                except Exception as e:
                    print(f"Error generando WAV: {e}")

            # Limpiar archivos temporales
            for ext in ['.alg', '.ly', '.ps']:
                temp_file = f'{base_name}{ext}'
                if os.path.exists(temp_file):
                    try:
                        os.remove(temp_file)
                    except:
                        pass

            # Limpiar archivos antiguos
            clean_old_outputs()

            return jsonify({
                'success': True,
                'output': stdout,
                'files': generated_files
            })

        except subprocess.TimeoutExpired:
            process.kill()
            return jsonify({
                'success': False,
                'error': 'Timeout: El código tardó más de 30 segundos en ejecutarse'
            })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error del servidor: {str(e)}',
            'traceback': traceback.format_exc()
        })


@app.route('/api/examples')
def get_examples():
    """Devuelve ejemplos de código predefinidos"""
    examples = {
        'hello': {
            'name': 'Hello Algoritmia',
            'code': '''Main |:
    <w> "Hello Algoritmia"
    (:) {C D E F G}
:|'''
        },
        'variables': {
            'name': 'Variables y operaciones',
            'code': '''Main |:
    x <- 10
    y <- 20
    <w> "La suma es:" x + y
    (:) {C D E}
:|'''
        },
        'condicional': {
            'name': 'Condicionales',
            'code': '''Main |:
    x <- 15
    if x > 10 |:
        <w> "Mayor que 10"
        (:) {C E G}
    :| else |:
        <w> "Menor o igual a 10"
        (:) {C D E}
    :|
:|'''
        },
        'listas': {
            'name': 'Operaciones con listas',
            'code': '''Main |:
    notas <- {C D E F G}
    <w> "Notas:" notas
    <w> "Longitud:" #notas
    notas << A
    notas << B
    <w> "Nueva lista:" notas
    (:) notas
:|'''
        },
        'escalas': {
            'name': 'Escalas musicales',
            'code': '''Main |:
    <w> "Escala ascendente"
    i <- 0
    while i < 8 |:
        nota <- C + i
        (:) nota
        i <- i + 1
    :|
:|'''
        },
        'hanoi': {
            'name': 'Torres de Hanoi',
            'code': '''Hanoi n origen desti aux |:
    if n > 0 |:
        temp <- n - 1
        Hanoi temp origen aux desti
        nota <- 28 + n * 2
        (:) nota
        <w> origen "-->" desti
        Hanoi temp aux desti origen
    :|
:|

Main |:
    Hanoi 3 1 3 2
:|'''
        }
    }
    return jsonify(examples)


@app.route('/api/clear', methods=['POST'])
def clear_outputs():
    """Limpia todos los archivos de salida"""
    try:
        for filename in os.listdir(OUTPUT_DIR):
            filepath = os.path.join(OUTPUT_DIR, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
        return jsonify({'success': True, 'message': 'Archivos limpiados'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    print("=" * 60)
    print("Aplicación Web Algoritmia".center(60))
    print("=" * 60)
    print("\nServidor iniciado en: http://localhost:5000")
    print("Presiona Ctrl+C para detener el servidor\n")
    print("=" * 60)

    app.run(debug=True, host='0.0.0.0', port=5000)