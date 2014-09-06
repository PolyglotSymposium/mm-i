#!/usr/bin/python3

import unittest
from repl import Evaluator

class MockPrinter:
    def print(self, output):
        self.output = output

class EvaluatorSpecs(unittest.TestCase):
    def test_integer_evaluates_as_that_integer(self):
        self.printer = MockPrinter()
        self.evaluator = Evaluator(self.printer.print)
        self.evaluator.eval_and_print('42')
        self.assertEqual(42, self.printer.output)

if __name__ == '__main__':
    unittest.main()
