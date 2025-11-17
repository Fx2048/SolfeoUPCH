#!/usr/bin/env python3
"""
Aplicación Web para Algoritmia - Versión Mejorada
Interfaz web para ejecutar código Algoritmia con mejor manejo de audio
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
import platform

app = Flask(__name__)
CORS(app)

# Configuración
OUTPUT_DIR = os.path.join('static', 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Detectar sistema operativo y configurar rutas
IS_WINDOWS = platform.system() == 'Windows'

# Rutas a herramientas (ajustar según tu instalación)
if IS_WINDOWS:
    TIMIDITY_PATH = r'C:\Users\USER\Downloads\TiMidity++-2.15.0-w32\TiMidity++-2.15.0\timidity.exe'
    # Ruta directa a FluidSynth
    FLUIDSYNTH_PATH = r'C:\FluidSynth\bin\fluidsynth.exe'
else:
    TIMIDITY_PATH = shutil.which('timidity')
    FLUIDSYNTH_PATH = shutil.which('fluidsynth')


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
                    print(f"Archivo antiguo eliminado: {filename}")
    except Exception as e:
        print(f"Error limpiando archivos: {e}")


def convert_midi_to_wav(midi_path, wav_path):
    """
    Convierte MIDI a WAV usando FluidSynth o Timidity
    Retorna True si la conversión fue exitosa
    """
    try:
        # Intentar con FluidSynth primero (más confiable)
        if FLUIDSYNTH_PATH and os.path.exists(FLUIDSYNTH_PATH):
            print("Usando FluidSynth para conversión MIDI->WAV")
            # Buscar un soundfont (archivo .sf2)
            soundfont_paths = [
                r'C:\soundfonts\FluidR3_GM.sf2',
                '/usr/share/sounds/sf2/FluidR3_GM.sf2',  # Linux
                '/usr/share/soundfonts/default.sf2',
                'C:\\soundfonts\\default.sf2',  # Windows
            ]
            
            soundfont = None
            for sf in soundfont_paths:
                if os.path.exists(sf):
                    soundfont = sf
                    break
            
            if soundfont:
                subprocess.run([
                    FLUIDSYNTH_PATH,
                    '-ni',  # No interactive mode
                    soundfont,
                    midi_path,
                    '-F', wav_path,
                    '-r', '44100'  # Sample rate
                ], check=True, capture_output=True, timeout=30)
                return True
            else:
                print("No se encontró soundfont para FluidSynth")
        
        # Intentar con Timidity
        if TIMIDITY_PATH and os.path.exists(TIMIDITY_PATH):
            print("Usando Timidity para conversión MIDI->WAV")
            
            if IS_WINDOWS:
                # En Windows, Timidity puede necesitar configuración especial
                subprocess.run([
                    TIMIDITY_PATH,
                    '-c', 'NUL',  # Sin archivo de configuración
                    midi_path,
                    '-Ow',  # Formato WAV
                    '-o', wav_path
                ], check=True, capture_output=True, timeout=30)
            else:
                subprocess.run([
                    TIMIDITY_PATH,
                    midi_path,
                    '-Ow',
                    '-o', wav_path
                ], check=True, capture_output=True, timeout=30)
            
            return True
            
    except subprocess.CalledProcessError as e:
        print(f"Error en conversión MIDI->WAV: {e}")
        print(f"stderr: {e.stderr}")
        return False
    except subprocess.TimeoutExpired:
        print("Timeout en conversión MIDI->WAV")
        return False
    except Exception as e:
        print(f"Error inesperado en conversión: {e}")
        return False
    
    return False


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
                [sys.executable, 'algoritmia.py', temp_alg, procedure],
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

                # Intentar generar WAV desde MIDI
                dest_wav = os.path.join(OUTPUT_DIR, f'{temp_filename}.wav')
                print(f"Intentando convertir MIDI a WAV...")
                
                if convert_midi_to_wav(dest_midi, dest_wav):
                    if os.path.exists(dest_wav) and os.path.getsize(dest_wav) > 0:
                        generated_files['wav'] = f'/static/outputs/{temp_filename}.wav'
                        print("✓ Conversión WAV exitosa")
                    else:
                        print("✗ Archivo WAV generado pero está vacío")
                else:
                    print("✗ No se pudo convertir MIDI a WAV")
                    # No es un error crítico, seguimos con PDF y MIDI

            # Limpiar archivos temporales
            for ext in ['.alg', '.ly', '.ps', '.eps']:
                temp_file = f'{base_name}{ext}'
                if os.path.exists(temp_file):
                    try:
                        os.remove(temp_file)
                    except Exception as e:
                        print(f"No se pudo eliminar {temp_file}: {e}")

            # Limpiar archivos antiguos
            clean_old_outputs()

            return jsonify({
                'success': True,
                'output': stdout,
                'files': generated_files,
                'info': {
                    'has_audio': 'wav' in generated_files or 'midi' in generated_files,
                    'has_score': 'pdf' in generated_files,
                    'timestamp': timestamp
                }
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
            'name': '👋 Hello Algoritmia',
            'code': '''Main |:
    <w> "Hello Algoritmia"
    (:) {C D E F G A B C}
:|'''
        },
        'variables': {
            'name': '🔢 Variables y operaciones',
            'code': '''Main |:
    x <- 10
    y <- 20
    suma <- x + y
    <w> "La suma de" x "y" y "es:" suma
    (:) {C E G}
:|'''
        },
        'condicional': {
            'name': '🔀 Condicionales',
            'code': '''Main |:
    x <- 15
    if x > 10 |:
        <w> "El número es mayor que 10"
        (:) {C E G C}
    :| else |:
        <w> "El número es menor o igual a 10"
        (:) {C D E F}
    :|
:|'''
        },
        'listas': {
            'name': '📋 Operaciones con listas',
            'code': '''Main |:
    notas <- {C D E F G}
    <w> "Notas iniciales:" notas
    <w> "Longitud:" #notas
    
    ### Añadir notas ###
    notas << A
    notas << B
    <w> "Notas finales:" notas
    
    ### Reproducir todas ###
    (:) notas
:|'''
        },
        'escalas': {
            'name': '🎼 Escalas musicales',
            'code': '''Main |:
    <w> "Escala de Do Mayor (ascendente)"
    i <- 0
    while i < 8 |:
        nota <- C + i
        (:) nota
        i <- i + 1
    :|
    
    <w> "Escala completada"
:|'''
        },
        'fibonacci': {
            'name': '🔄 Fibonacci Musical',
            'code': '''Fibonacci n |:
    if n <= 1 |:
        (:) C
    :| else |:
        n1 <- n - 1
        n2 <- n - 2
        Fibonacci n1
        Fibonacci n2
    :|
:|

Main |:
    <w> "Secuencia de Fibonacci en música"
    Fibonacci 5
:|'''
        },
        'hanoi': {
            'name': '🗼 Torres de Hanoi',
            'code': '''Hanoi n origen destino auxiliar |:
    if n > 0 |:
        temp <- n - 1
        Hanoi temp origen auxiliar destino
        
        ### Tocar la nota correspondiente al disco ###
        nota <- C + n * 2
        (:) nota
        <w> "Mover disco" n "de" origen "a" destino
        
        Hanoi temp auxiliar destino origen
    :|
:|

Main |:
    <w> "Torres de Hanoi con 3 discos"
    Hanoi 3 1 3 2
    <w> "Completado"
:|'''
        },
        'melodia': {
            'name': '🎵 Melodía Simple',
            'code': '''Main |:
    <w> "Tocando una melodía"
    
    ### Frase 1 ###
    (:) {C C G G A A G}
    
    ### Frase 2 ###
    (:) {F F E E D D C}
    
    <w> "Melodía completada"
:|'''
        }
    }
    return jsonify(examples)


@app.route('/api/clear', methods=['POST'])
def clear_outputs():
    """Limpia todos los archivos de salida"""
    try:
        count = 0
        for filename in os.listdir(OUTPUT_DIR):
            filepath = os.path.join(OUTPUT_DIR, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
                count += 1
        return jsonify({
            'success': True,
            'message': f'{count} archivos limpiados'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })


@app.route('/api/system-info')
def system_info():
    """Información del sistema para diagnóstico"""
    info = {
        'platform': platform.system(),
        'python_version': sys.version,
        'has_timidity': TIMIDITY_PATH is not None and os.path.exists(TIMIDITY_PATH) if TIMIDITY_PATH else False,
        'has_fluidsynth': FLUIDSYNTH_PATH is not None,
        'has_lilypond': shutil.which('lilypond') is not None,
        'output_dir': OUTPUT_DIR,
        'working_dir': os.getcwd()
    }
    return jsonify(info)


if __name__ == '__main__':
    print("=" * 70)
    print("🎵 Aplicación Web Algoritmia - Versión Mejorada 🎵".center(70))
    print("=" * 70)
    print("\n📍 Servidor iniciado en: http://localhost:5000")
    print("📍 También accesible desde: http://0.0.0.0:5000")
    print("\n🔧 Herramientas disponibles:")
    print(f"   • Timidity: {'✓' if TIMIDITY_PATH and os.path.exists(TIMIDITY_PATH) else '✗'}")
    print(f"   • FluidSynth: {'✓' if FLUIDSYNTH_PATH else '✗'}")
    print(f"   • LilyPond: {'✓' if shutil.which('lilypond') else '✗'}")
    print("\n💡 Presiona Ctrl+C para detener el servidor")
    print("=" * 70 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)