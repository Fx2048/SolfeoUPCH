#!/usr/bin/env python3
"""
Suite de pruebas para el intérprete de Algoritmia
"""

import unittest
import sys
import io
from contextlib import redirect_stdout
from antlr4 import *
from AlgoritmiaLexer import AlgoritmiaLexer
from AlgoritmiaParser import AlgoritmiaParser
from algoritmia import AlgoritmiaInterpreter


class TestAlgoritmiaBasics(unittest.TestCase):
    """Tests básicos del intérprete"""

    def parse_and_run(self, code, start_proc="Main", input_data=None):
        """Ejecuta código Algoritmia y retorna output capturado"""
        input_stream = InputStream(code)
        lexer = AlgoritmiaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AlgoritmiaParser(stream)
        tree = parser.root()

        interpreter = AlgoritmiaInterpreter()
        interpreter.visitRoot(tree)

        # Capturar stdout
        captured_output = io.StringIO()

        # Simular stdin si es necesario
        if input_data:
            sys.stdin = io.StringIO(input_data)

        with redirect_stdout(captured_output):
            try:
                interpreter.execute_procedure(start_proc, [])
            except Exception as e:
                return None, str(e), interpreter.score

        # Restaurar stdin
        sys.stdin = sys.__stdin__

        return captured_output.getvalue(), None, interpreter.score

    def test_hello_world(self):
        """Test: Hello Algoritmia"""
        code = '''
        Main |:
            <w> "Hello Algoritmia"
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(output.strip(), "Hello Algoritmia")

    def test_arithmetic_operations(self):
        """Test: Operaciones aritméticas"""
        code = '''
        Main |:
            a <- 10
            b <- 3
            <w> a + b
            <w> a - b
            <w> a * b
            <w> a / b
            <w> a % b
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        lines = output.strip().split('\n')
        self.assertEqual(lines[0], "13")
        self.assertEqual(lines[1], "7")
        self.assertEqual(lines[2], "30")
        self.assertEqual(lines[3], "3")
        self.assertEqual(lines[4], "1")

    def test_conditional(self):
        """Test: Condicional if-else"""
        code = '''
        Main |:
            x <- 5
            if x > 3 |:
                <w> "Mayor"
            :| else |:
                <w> "Menor o igual"
            :|
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(output.strip(), "Mayor")

    def test_while_loop(self):
        """Test: Bucle while"""
        code = '''
        Main |:
            i <- 1
            suma <- 0
            while i <= 5 |:
                suma <- suma + i
                i <- i + 1
            :|
            <w> suma
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(output.strip(), "15")

    def test_procedure_call(self):
        """Test: Llamada a procedimiento"""
        code = '''
        Main |:
            Saludar "Mundo"
        :|

        Saludar nombre |:
            <w> "Hola" nombre
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(output.strip(), "Hola Mundo")

    def test_recursion(self):
        """Test: Recursión (factorial)"""
        code = '''
        Main |:
            n <- 5
            result <- Factorial n
            <w> result
        :|

        Factorial n |:
            if n <= 1 |:
                result <- 1
            :| else |:
                result <- n * Factorial n - 1
            :|
        :|
        '''
        # Nota: Este test requeriría funciones que devuelvan valores
        # El lenguaje actual no soporta return, así que lo adaptamos
        code = '''
        Main |:
            Factorial 5
        :|

        Factorial n |:
            if n <= 1 |:
                <w> 1
            :| else |:
                <w> n
                Factorial n - 1
            :|
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)


class TestAlgoritmiaLists(unittest.TestCase):
    """Tests de operaciones con listas"""

    def parse_and_run(self, code, start_proc="Main"):
        input_stream = InputStream(code)
        lexer = AlgoritmiaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AlgoritmiaParser(stream)
        tree = parser.root()

        interpreter = AlgoritmiaInterpreter()
        interpreter.visitRoot(tree)

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            try:
                interpreter.execute_procedure(start_proc, [])
            except Exception as e:
                return None, str(e), interpreter.score

        return captured_output.getvalue(), None, interpreter.score

    def test_list_creation(self):
        """Test: Creación de listas"""
        code = '''
        Main |:
            lista <- {10 20 30}
            <w> lista
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(output.strip(), "[10 20 30]")

    def test_list_size(self):
        """Test: Tamaño de lista"""
        code = '''
        Main |:
            lista <- {1 2 3 4 5}
            <w> #lista
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(output.strip(), "5")

    def test_list_access(self):
        """Test: Acceso a elementos"""
        code = '''
        Main |:
            lista <- {100 200 300}
            <w> lista[1]
            <w> lista[2]
            <w> lista[3]
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        lines = output.strip().split('\n')
        self.assertEqual(lines[0], "100")
        self.assertEqual(lines[1], "200")
        self.assertEqual(lines[2], "300")

    def test_list_append(self):
        """Test: Añadir elementos"""
        code = '''
        Main |:
            lista <- {1 2}
            lista << 3
            lista << 4
            <w> lista
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(output.strip(), "[1 2 3 4]")

    def test_list_cut(self):
        """Test: Eliminar elementos"""
        code = '''
        Main |:
            lista <- {10 20 30 40}
            8< lista[2]
            <w> lista
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(output.strip(), "[10 30 40]")


class TestAlgoritmiaMusic(unittest.TestCase):
    """Tests de funcionalidad musical"""

    def parse_and_run(self, code, start_proc="Main"):
        input_stream = InputStream(code)
        lexer = AlgoritmiaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AlgoritmiaParser(stream)
        tree = parser.root()

        interpreter = AlgoritmiaInterpreter()
        interpreter.visitRoot(tree)

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            try:
                interpreter.execute_procedure(start_proc, [])
            except Exception as e:
                return None, str(e), interpreter.score

        return captured_output.getvalue(), None, interpreter.score

    def test_single_note(self):
        """Test: Reproducir nota única"""
        code = '''
        Main |:
            (:) C
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(len(score), 1)
        self.assertIsInstance(score[0], int)

    def test_note_list(self):
        """Test: Reproducir lista de notas"""
        code = '''
        Main |:
            (:) {C D E}
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(len(score), 3)

    def test_note_transpose(self):
        """Test: Transposición de notas"""
        code = '''
        Main |:
            nota <- C
            (:) nota
            (:) nota + 7
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        self.assertEqual(len(score), 2)
        self.assertEqual(score[1] - score[0], 7)


class TestAlgoritmiaComplexPrograms(unittest.TestCase):
    """Tests de programas complejos"""

    def parse_and_run(self, code, start_proc="Main", input_data=None):
        input_stream = InputStream(code)
        lexer = AlgoritmiaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AlgoritmiaParser(stream)
        tree = parser.root()

        interpreter = AlgoritmiaInterpreter()
        interpreter.visitRoot(tree)

        captured_output = io.StringIO()
        if input_data:
            sys.stdin = io.StringIO(input_data)

        with redirect_stdout(captured_output):
            try:
                interpreter.execute_procedure(start_proc, [])
            except Exception as e:
                return None, str(e), interpreter.score

        sys.stdin = sys.__stdin__
        return captured_output.getvalue(), None, interpreter.score

    def test_fibonacci(self):
        """Test: Secuencia de Fibonacci"""
        code = '''
        Main |:
            Fib 6
        :|

        Fib n |:
            a <- 0
            b <- 1
            i <- 0
            while i < n |:
                <w> a
                temp <- a + b
                a <- b
                b <- temp
                i <- i + 1
            :|
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        lines = output.strip().split('\n')
        expected = ["0", "1", "1", "2", "3", "5"]
        self.assertEqual(lines, expected)

    def test_hanoi(self):
        """Test: Torres de Hanoi"""
        code = '''
        Main |:
            Hanoi 2 1 2 3
        :|

        Hanoi n origen destino auxiliar |:
            if n > 0 |:
                Hanoi n-1 origen auxiliar destino
                <w> "Mover de" origen "a" destino
                Hanoi n-1 auxiliar destino origen
            :|
        :|
        '''
        output, error, score = self.parse_and_run(code)
        self.assertIsNone(error)
        lines = output.strip().split('\n')
        # Con 2 discos deberían ser 3 movimientos
        self.assertEqual(len(lines), 3)


def run_tests():
    """Ejecuta todas las pruebas"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestAlgoritmiaBasics))
    suite.addTests(loader.loadTestsFromTestCase(TestAlgoritmiaLists))
    suite.addTests(loader.loadTestsFromTestCase(TestAlgoritmiaMusic))
    suite.addTests(loader.loadTestsFromTestCase(TestAlgoritmiaComplexPrograms))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)