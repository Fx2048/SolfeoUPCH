#!/usr/bin/env python3
"""
Intérprete de Algoritmia - Lenguaje de Programación Musical
Universidad Peruana Cayetano Heredia
"""

import sys
import os
from antlr4 import *
from AlgoritmiaLexer import AlgoritmiaLexer
from AlgoritmiaParser import AlgoritmiaParser
from AlgoritmiaVisitor import AlgoritmiaVisitor
from typing import Any, Dict, List, Optional
import subprocess

# Ruta a Timidity
TIMIDITY_PATH = r'C:\Users\USER\Downloads\TiMidity++-2.15.0-w32\TiMidity++-2.15.0\timidity.exe'
# Mapeo de notas musicales a valores enteros
NOTES = {
    # Notas sin número (octava central - octava 4)
    'C': 28, 'D': 29, 'E': 30, 'F': 31, 'G': 32, 'A': 33, 'B': 34,
    # Notas con números (octavas 0-8)
    'A0': 0, 'B0': 1,
    'C1': 2, 'D1': 3, 'E1': 4, 'F1': 5, 'G1': 6, 'A1': 7, 'B1': 8,
    'C2': 9, 'D2': 10, 'E2': 11, 'F2': 12, 'G2': 13, 'A2': 14, 'B2': 15,
    'C3': 16, 'D3': 17, 'E3': 18, 'F3': 19, 'G3': 20, 'A3': 21, 'B3': 22,
    'C4': 23, 'D4': 24, 'E4': 25, 'F4': 26, 'G4': 27, 'A4': 28, 'B4': 29,
    'C5': 30, 'D5': 31, 'E5': 32, 'F5': 33, 'G5': 34, 'A5': 35, 'B5': 36,
    'C6': 37, 'D6': 38, 'E6': 39, 'F6': 40, 'G6': 41, 'A6': 42, 'B6': 43,
    'C7': 44, 'D7': 45, 'E7': 46, 'F7': 47, 'G7': 48, 'A7': 49, 'B7': 50,
    'C8': 51,
}

# Mapeo inverso de enteros a notas para LilyPond
NOTE_NAMES = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
NOTE_OCTAVES = {
    0: ",,,,", 1: ",,,", 2: ",,", 3: ",", 4: "",
    5: "'", 6: "''", 7: "'''", 8: "''''"
}


class Procedure:
    """Representa un procedimiento en Algoritmia"""

    def __init__(self, name: str, params: List[str], block):
        self.name = name
        self.params = params
        self.block = block


class AlgoritmiaInterpreter(AlgoritmiaVisitor):
    """Intérprete del lenguaje Algoritmia"""

    def __init__(self):
        self.procedures: Dict[str, Procedure] = {}
        self.call_stack: List[Dict[str, Any]] = []
        self.score: List[int] = []  # Partitura como lista de enteros
        self.current_scope: Dict[str, Any] = {}

    def visitRoot(self, ctx):
        """Visita el nodo raíz y recolecta todos los procedimientos"""
        # Primera pasada: recolectar todos los procedimientos
        for proc_ctx in ctx.procedure():
            self.visitProcedure(proc_ctx)
        return None

    def visitProcedure(self, ctx):
        """Define un procedimiento"""
        name = ctx.ID().getText()
        params = []
        if ctx.params():
            params = [id_node.getText() for id_node in ctx.params().ID()]

        procedure = Procedure(name, params, ctx.block())
        self.procedures[name] = procedure
        return None

    def execute_procedure(self, name: str, args: List[Any]):
        """Ejecuta un procedimiento con argumentos"""
        if name not in self.procedures:
            raise RuntimeError(f"Procedimiento '{name}' no encontrado")

        proc = self.procedures[name]

        # Verificar número de parámetros
        if len(args) != len(proc.params):
            raise RuntimeError(
                f"Procedimiento '{name}' espera {len(proc.params)} parámetros, "
                f"pero se pasaron {len(args)}"
            )

        # Crear nuevo ámbito local
        local_scope = {}
        for param, arg in zip(proc.params, args):
            if isinstance(arg, list):
                local_scope[param] = arg.copy()  # Copiar listas
            else:
                local_scope[param] = arg

        # Guardar scope anterior y establecer el nuevo
        prev_scope = self.current_scope
        self.current_scope = local_scope
        self.call_stack.append(local_scope)

        # Ejecutar el bloque del procedimiento
        try:
            self.visit(proc.block)
        finally:
            # Restaurar scope anterior
            self.call_stack.pop()
            self.current_scope = prev_scope

    def visitBlock(self, ctx):
        """Ejecuta un bloque de instrucciones"""
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitAssignment(self, ctx):
        """Asignación de variable"""
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())

        # Copiar listas para evitar aliasing
        if isinstance(value, list):
            value = value.copy()

        self.current_scope[var_name] = value
        return None

    def visitRead(self, ctx):
        """Lectura de entrada estándar"""
        var_name = ctx.ID().getText()
        try:
            value = int(input())
            self.current_scope[var_name] = value
        except ValueError:
            raise RuntimeError("Error: se esperaba un número entero")
        return None

    def visitWrite(self, ctx):
        """Escritura a salida estándar"""
        outputs = []
        for param in ctx.writeParam():
            if param.STRING():
                # Texto entre comillas
                text = param.STRING().getText()
                outputs.append(text[1:-1])  # Quitar comillas
            else:
                # Expresión
                value = self.visit(param.expr())
                if isinstance(value, list):
                    outputs.append('[' + ' '.join(map(str, value)) + ']')
                else:
                    outputs.append(str(value))

        print(' '.join(outputs))
        return None

    def visitPlay(self, ctx):
        """Reproducción de notas"""
        value = self.visit(ctx.expr())

        if isinstance(value, list):
            # Añadir cada nota de la lista
            for note in value:
                if isinstance(note, int):
                    self.score.append(note)
        elif isinstance(value, int):
            # Añadir una sola nota
            self.score.append(value)
        else:
            raise RuntimeError(f"Play espera un entero o lista, recibió {type(value)}")

        return None

    def visitConditional(self, ctx):
        """Condicional if-else"""
        condition = self.visit(ctx.expr())

        if condition != 0:  # Verdadero
            self.visit(ctx.block(0))
        elif len(ctx.block()) > 1:  # Hay else
            self.visit(ctx.block(1))

        return None

    def visitIteration(self, ctx):
        """Bucle while"""
        while True:
            condition = self.visit(ctx.expr())
            if condition == 0:  # Falso
                break
            self.visit(ctx.block())

        return None

    def visitProcCall(self, ctx):
        """Llamada a procedimiento"""
        proc_name = ctx.ID().getText()
        args = [self.visit(expr) for expr in ctx.expr()]
        self.execute_procedure(proc_name, args)
        return None

    def visitListAppend(self, ctx):
        """Añadir elemento a lista"""
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())

        if var_name not in self.current_scope:
            self.current_scope[var_name] = []

        if not isinstance(self.current_scope[var_name], list):
            raise RuntimeError(f"'{var_name}' no es una lista")

        self.current_scope[var_name].append(value)
        return None

    def visitListCut(self, ctx):
        """Eliminar elemento de lista"""
        var_name = ctx.ID().getText()
        index = self.visit(ctx.expr())

        if var_name not in self.current_scope:
            raise RuntimeError(f"Variable '{var_name}' no definida")

        lst = self.current_scope[var_name]
        if not isinstance(lst, list):
            raise RuntimeError(f"'{var_name}' no es una lista")

        # Índices comienzan en 1
        if index < 1 or index > len(lst):
            raise RuntimeError(f"Índice {index} fuera de rango para lista de tamaño {len(lst)}")

        lst.pop(index - 1)
        return None

    # Expresiones
    def visitMulDivMod(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text

        if op == '*':
            return left * right
        elif op == '/':
            return left // right  # División entera
        elif op == '%':
            return left % right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text

        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    def visitRelational(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text

        result = False
        if op == '=':
            result = left == right
        elif op == '/=':
            result = left != right
        elif op == '<':
            result = left < right
        elif op == '>':
            result = left > right
        elif op == '<=':
            result = left <= right
        elif op == '>=':
            result = left >= right

        return 1 if result else 0

    def visitParenthesis(self, ctx):
        return self.visit(ctx.expr())

    def visitListAccess(self, ctx):
        var_name = ctx.ID().getText()
        index = self.visit(ctx.expr())

        if var_name not in self.current_scope:
            raise RuntimeError(f"Variable '{var_name}' no definida")

        lst = self.current_scope[var_name]
        if not isinstance(lst, list):
            raise RuntimeError(f"'{var_name}' no es una lista")

        # Índices comienzan en 1
        if index < 1 or index > len(lst):
            raise RuntimeError(f"Índice {index} fuera de rango")

        return lst[index - 1]

    def visitListSize(self, ctx):
        var_name = ctx.ID().getText()

        if var_name not in self.current_scope:
            return 0

        value = self.current_scope[var_name]
        if isinstance(value, list):
            return len(value)
        else:
            return 0

    def visitListLiteral(self, ctx):
        elements = []
        for expr in ctx.expr():
            elements.append(self.visit(expr))
        return elements

    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()

        # Si es una nota musical, devolver su valor
        if var_name in NOTES:
            return NOTES[var_name]

        # Si no está definida, devolver 0
        if var_name not in self.current_scope:
            return 0

        return self.current_scope[var_name]

    def visitNumber(self, ctx):
        return int(ctx.NUM().getText())

    def visitNote(self, ctx):
        note_name = ctx.NOTE().getText()
        if note_name in NOTES:
            return NOTES[note_name]
        raise RuntimeError(f"Nota '{note_name}' no reconocida")


def generate_lilypond(score: List[int], output_filename: str):
    """Genera archivo LilyPond a partir de la partitura"""

    def note_to_lilypond(note_value: int) -> str:
        """Convierte un valor entero a notación LilyPond"""
        # Mapeo aproximado (simplificado)
        note_names_ly = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

        # Calcular octava y nota
        octave = note_value // 7
        note_index = note_value % 7

        note_str = note_names_ly[note_index]

        # Añadir modificador de octava
        if octave < 3:
            note_str += ',' * (3 - octave)
        elif octave > 3:
            note_str += "'" * (octave - 3)

        return note_str + '4'  # Negra

    # Generar contenido LilyPond
    lilypond_notes = ' '.join([note_to_lilypond(note) for note in score])

    lilypond_content = f'''\\version "2.20.0"
\\score {{
  \\new Staff {{
    \\clef treble
    {{ {lilypond_notes} }}
  }}
  \\layout {{ }}
  \\midi {{ }}
}}
'''

    # Escribir archivo .ly
    ly_filename = output_filename.replace('.alg', '.ly')
    with open(ly_filename, 'w') as f:
        f.write(lilypond_content)

    return ly_filename


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 algoritmia.py <archivo.alg> [procedimiento_inicial]")
        sys.exit(1)

    input_file = sys.argv[1]
    start_proc = sys.argv[2] if len(sys.argv) > 2 else "Main"

    if not os.path.exists(input_file):
        print(f"Error: archivo '{input_file}' no encontrado")
        sys.exit(1)

    # Leer archivo fuente
    input_stream = FileStream(input_file, encoding='utf-8')

    # Análisis léxico
    lexer = AlgoritmiaLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Análisis sintáctico
    parser = AlgoritmiaParser(stream)
    tree = parser.root()

    # Interpretación
    interpreter = AlgoritmiaInterpreter()
    interpreter.visitRoot(tree)

    # Ejecutar procedimiento inicial
    try:
        interpreter.execute_procedure(start_proc, [])
    except RuntimeError as e:
        print(f"Error de ejecución: {e}")
        sys.exit(1)

    # Generar archivos de salida si hay partitura
    if interpreter.score:
        base_name = input_file.replace('.alg', '')

        # Generar LilyPond
        ly_file = generate_lilypond(interpreter.score, input_file)

        # Compilar con LilyPond
        try:
            subprocess.run(['lilypond', '-o', base_name, ly_file],
                           check=True, capture_output=True)
            print(f"Partitura generada: {base_name}.pdf")
            # Generar WAV con timidity (buscar .mid o .midi)
            midi_file = base_name + '.mid'
            if not os.path.exists(midi_file):
                midi_file = base_name + '.midi'

            if os.path.exists(midi_file):
                subprocess.run([TIMIDITY_PATH, '-c', 'NUL', midi_file, '-Ow', '-o',
                                base_name + '.wav'],
                               check=True, capture_output=True)
                print(f"Audio generado: {base_name}.wav")
        except subprocess.CalledProcessError as e:
            print(f"Error al generar archivos de salida: {e}")
        except FileNotFoundError:
            print("Advertencia: lilypond o timidity no encontrados en el sistema")


if __name__ == '__main__':
    main()