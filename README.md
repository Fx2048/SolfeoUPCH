<hr style="border: 1px solid #1E90FF;">

[![Python](https://img.shields.io/badge/Python-%20-101010?style=for-the-badge&logo=python&logoColor=white&labelColor=FFD43B)](https://www.python.org/)
[![ANTLR](https://img.shields.io/badge/ANTLR-%20-101010?style=for-the-badge&logo=antlr&logoColor=white&labelColor=FF5252)](https://www.antlr.org/)
[![Flask](https://img.shields.io/badge/Flask-%20-101010?style=for-the-badge&logo=flask&logoColor=white&labelColor=000000)](https://flask.palletsprojects.com/)
[![HTML](https://img.shields.io/badge/HTML-%20-101010?style=for-the-badge&logo=html5&logoColor=white&labelColor=E34F26)](https://developer.mozilla.org/es/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-%20-101010?style=for-the-badge&logo=css3&logoColor=white&labelColor=264de4)](https://developer.mozilla.org/es/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JS-%20-101010?style=for-the-badge&logo=javascript&logoColor=white&labelColor=f7df1e)](https://developer.mozilla.org/es/docs/Web/JavaScript)
[![FluidSynth](https://img.shields.io/badge/FluidSynth-%20-101010?style=for-the-badge&logo=musicbrainz&logoColor=white&labelColor=2ECC71)](https://www.fluidsynth.org/)
[![TiMidity](https://img.shields.io/badge/TiMidity-%20-101010?style=for-the-badge&logo=musicbrainz&logoColor=white&labelColor=8E44AD)](http://timidity.sourceforge.net/)
[![LilyPond](https://img.shields.io/badge/LilyPond-%20-101010?style=for-the-badge&logo=musicbrainz&logoColor=white&labelColor=1ABC9C)](https://lilypond.org/)

<p align="center">
  <a href="https://cayetano.edu.pe/">
    <img src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=F1C40F&size=25&center=true&vCenter=true&width=700&height=100&lines=UNIVERSIDAD+PERUANA+CAYETANO+HEREDIA;LENGUAJE+DE+PROGRAMACIÓN+MUSICAL;IMPLEMENTACIÓN+DE+UN+DOBLE+INTÉRPRETE+DE+ALGORITMIA">
  </a>
</p>

  
    # 🎵 Algoritmia - Lenguaje de Programación Musical - Doble Intérprete
<p align="justify">
Intérprete de Algoritmia es desarrollado como proyecto final para el curso de **Implementación de Lenguajes de Programación** de la Universidad Peruana Cayetano Heredia.
</p>
<p align="justify">
Algoritmia es un lenguaje de programación orientado a la composición algorítmica que permite generar partituras musicales en formato PDF, MIDI y WAV, en base a reglas Sintácticas y Léxicas.
</p>

## 📋 Características

- ✅ Variables y asignaciones
- ✅ Operaciones aritméticas (+, -, *, /, %)
- ✅ Operadores relacionales (=, /=, <, >, <=, >=)
- ✅ Condicionales (if/else)
- ✅ Bucles (while)
- ✅ Listas y operaciones con listas
- ✅ Procedimientos con parámetros
- ✅ Recursividad
- ✅ Entrada/Salida (lectura y escritura)
- ✅ Reproducción de notas musicales
- ✅ Generación automática de partituras (PDF)
- ✅ Generación de archivos de audio (MIDI y WAV)

## 🛠️ Requisitos

### Software necesario:

- **Python 3.8+**
- **Java JDK 17+** (para ANTLR)
- **ANTLR 4.13.1**
- **LilyPond** (para generar partituras)
- **Timidity++** (para generar archivos WAV)
- **FluidSynth** (Para repuesto en generación de audio)

### Librerías Python:

```
antlr4-python3-runtime==4.13.1
```

## 📥 Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd PythonProject2
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En Linux/Mac:
source .venv/bin/activate
```

### 3. Instalar dependencias de Python

```bash
pip install -r requirements.txt
```

### 4. Instalar herramientas externas

#### LilyPond:
- **Windows**: Descargar desde http://lilypond.org/download.html
- **Linux**: `sudo apt-get install lilypond`
- **Mac**: `brew install lilypond`

#### Timidity++:
- **Windows**: Descargar desde https://sourceforge.net/projects/timidity/
- **Linux**: `sudo apt-get install timidity`
- **Mac**: `brew install timidity`

#### FluidSynth:
- **Windows**: Descargar desde https://www.fluidsynth.org/ (se recomienda la versión con instalador o usar MSYS2 para instalar fluidsynth)
- **Linux**: `sudo apt-get install fluidsynth` (Debian/Ubuntu) o `sudo dnf install fluidsynth` (Fedora)
- **Mac**: `brew install fluidsynth`

### 5. Generar parser de ANTLR

```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor Algoritmia.g4
```

O usar el Makefile (Linux/Mac):
```bash
make grammar
```

## 🚀 Uso

### Sintaxis básica:

```bash
python algoritmia.py <archivo.alg> [procedimiento_inicial]
```

### Ejemplos:

```bash
# Ejecutar desde el procedimiento Main (por defecto)
python algoritmia.py examples.alg

# Ejecutar desde un procedimiento específico
python algoritmia.py examples.alg MiProcedimiento
```

## 📝 Ejemplos de código

### Hello World

```algoritmia
Main |:
    <w> "Hello Algoritmia"
    (:) {C D E F G}
:|
```

### Variables y operaciones

```algoritmia
Main |:
    x <- 10
    y <- 20
    <w> "La suma es:" x + y
    (:) {C D E}
:|
```

### Condicionales

```algoritmia
Main |:
    <?> n
    if n > 0 |:
        <w> "Positivo"
    :| else |:
        <w> "No positivo"
    :|
:|
```

### Bucles

```algoritmia
Main |:
    i <- 1
    while i <= 5 |:
        <w> i
        i <- i + 1
    :|
:|
```

### Procedimientos recursivos

```algoritmia
Factorial n |:
    if n <= 1 |:
        <w> 1
    :| else |:
        temp <- n - 1
        resultado <- n
        i <- temp
        while i > 0 |:
            resultado <- resultado * i
            i <- i - 1
        :|
        <w> resultado
    :|
:|

Main |:
    Factorial 5
:|
```

### Torres de Hanoi musical

```algoritmia
Hanoi n origen desti aux |:
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
:|
```

## 🧪 Archivos de prueba incluidos

- `examples.alg` - Ejemplo básico
- `test_euclides.alg` - Algoritmo de Euclides (MCD)
- `test_hanoi_musical.alg` - Torres de Hanoi con música
- `test_escalas.alg` - Generador de escalas musicales
- `test_listas.alg` - Operaciones con listas
- `test_factorial.alg` - Cálculo de factorial
- `test_melodia.alg` - Composición musical compleja

### Ejecutar todos los tests:

```bash
python run_all_tests.py
```

## 🎼 Sistema de notas musicales

Algoritmia utiliza el sistema de notación musical inglés:

### Notas sin número (octava central - Do4):
```
C, D, E, F, G, A, B
```

### Notas con octavas (0-8):
```
A0, B0, C1, D1, ..., A7, B7, C8
```

### Transposición:
```algoritmia
nota <- C      ### Do central (28)
nota <- nota + 7  ### Una octava más alta
```

## 📂 Estructura del proyecto

```
PythonProject2/
├── algoritmia.py              # Intérprete principal
├── Algoritmia.g4              # Gramática ANTLR
├── AlgoritmiaLexer.py         # Analizador léxico (generado)
├── AlgoritmiaParser.py        # Analizador sintáctico (generado)
├── AlgoritmiaVisitor.py       # Visitor pattern (generado)
├── AlgoritmiaListener.py      # Listener pattern (generado)
├── requirements.txt           # Dependencias Python
├── Makefile                   # Comandos de compilación
├── README.md                  # Este archivo
├── examples.alg               # Ejemplo básico
├── test_*.alg                 # Archivos de prueba
└── antlr-4.13.1-complete.jar  # ANTLR runtime
```

## 📤 Archivos de salida

Para cada archivo `.alg` ejecutado con éxito, se generan:

- **`archivo.ly`** - Código fuente LilyPond
- **`archivo.pdf`** - Partitura en formato PDF
- **`archivo.mid`** - Audio en formato MIDI
- **`archivo.wav`** - Audio en formato WAV
- 
#### ➡️ [Diagrama de flujo](Diagrama de flujo/Diagrama_flujo.md)

###  Flujo principal:

* **Validación inicial**: Verificación de argumentos y existencia del archivo
* **Análisis**: Léxico y sintáctico usando ANTLR4
* **Recolección**: Identificación y almacenamiento de procedimientos
* **Ejecución**: Invocación del procedimiento inicial con gestión de ámbitos
* **Procesamiento de instrucciones**: Asignaciones, lectura/escritura, condicionales, bucles, listas y reproducción musical
* **Evaluación de expresiones**: Variables, números, notas musicales, operaciones y listas
* **Generación de salida**: Conversión de la partitura a formato LilyPond, compilación a PDF/MIDI y conversión a WAV


## 🐛 Solución de problemas

### Error: "No such file or directory: algoritmia.py"
Asegúrate de estar en el directorio correcto del proyecto.

### Error: "java: command not found"
Instala Java JDK y agrégalo al PATH del sistema.

### Error: "lilypond: command not found"
Instala LilyPond y agrégalo al PATH del sistema.

### Error: "timidity: Can't read configuration file"
En Windows, ejecuta timidity con el parámetro `-c NUL`:
```bash
timidity -c NUL archivo.mid -Ow -o archivo.wav
```

## 👥 Autores

Proyecto desarrollado para el curso de Implementación de Lenguajes de Programación.

**Universidad Peruana Cayetano Heredia**

1. Frank Kevin Jauregui Bendezu
2. Jesus Anselmo Morales Alvarado
3. Brigitte Bernal Belisario
4. Nardy Liz Condori Mamani

## 📄 Licencia

Este proyecto es de uso académico para el curso de Implementación de Lenguajes de Programación.

## 🙏 Agradecimientos

- ANTLR - Framework para generación de parsers
- LilyPond - Software de notación musical
- Timidity++ - Sintetizador MIDI

---

**¡Disfruta componiendo con Algoritmia! 🎵**
