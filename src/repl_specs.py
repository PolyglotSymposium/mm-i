#!/usr/bin/python3

import unittest
from repl import Evaluator
from lexer import Lexer

class EvaluatorSpecs(unittest.TestCase):
    def test_integer_evaluates_as_that_integer(self):
        self.assertEqual(42, Evaluator(Lexer()).evaluate('42'))

if __name__ == '__main__':
    unittest.main()
