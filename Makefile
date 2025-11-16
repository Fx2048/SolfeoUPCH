# Makefile para el proyecto Algoritmia

.PHONY: all clean grammar test install help

# Variables
ANTLR4 = java -jar /usr/local/lib/antlr-4.13.1-complete.jar
PYTHON = python3
GRAMMAR = Algoritmia.g4
MAIN = algoritmia.py

all: grammar

grammar:
	@echo "Generando parser desde gramática..."
	$(ANTLR4) -Dlanguage=Python3 -visitor $(GRAMMAR)
	@echo "Parser generado exitosamente"

install:
	@echo "Instalando dependencias..."
	pip install -r requirements.txt
	@echo "Verificando herramientas externas..."
	@which lilypond > /dev/null || echo "ADVERTENCIA: lilypond no encontrado"
	@which timidity > /dev/null || echo "ADVERTENCIA: timidity no encontrado"
	@echo "Instalación completa"

test: grammar
	@echo "Ejecutando suite de pruebas..."
	$(PYTHON) test_algoritmia.py

run-examples: grammar
	@echo "Ejecutando ejemplo: Hello Algoritmia"
	@echo 'Main |: <w> "Hello Algoritmia" (:) {C D E} :|' > temp.alg
	$(PYTHON) $(MAIN) temp.alg
	@rm -f temp.alg

clean:
	@echo "Limpiando archivos generados..."
	rm -f AlgoritmiaLexer.py AlgoritmiaParser.py
	rm -f AlgoritmiaVisitor.py AlgoritmiaListener.py
	rm -f *.tokens *.interp
	rm -f *.pdf *.midi *.wav *.ly *.ps
	rm -rf __pycache__
	@echo "Limpieza completa"

help:
	@echo "Comandos disponibles:"
	@echo "  make grammar      - Genera el parser desde la gramática"
	@echo "  make install      - Instala dependencias"
	@echo "  make test         - Ejecuta pruebas"
	@echo "  make run-examples - Ejecuta ejemplos"
	@echo "  make clean        - Limpia archivos generados"
	@echo "  make help         - Muestra esta ayuda"