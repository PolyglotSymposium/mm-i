#!/usr/bin/python3

import unittest
from lexer import *

def nth(generator, n):
    for i in range(1, n):
        next(generator)
    return next(generator)

def tokenize(text):
    return Lexer().tokenize(text)

class LexerSpecs(unittest.TestCase):
    def test_left_paren_type(self):
        self.assert_first_token('(', token.left_paren())

    def test_right_paren_type(self):
        self.assert_first_token(')', token.right_paren())

    def test_left_square_bracket_type(self):
        self.assert_first_token('[', token.left_square_bracket())

    def test_right_square_bracket_type(self):
        self.assert_first_token(']', token.right_square_bracket())

    def test_function_type(self):
        self.assert_first_token('->', token.function())

    def assert_first_token(self, chars, expected_token):
        self.assertTrue(next(tokenize(chars)).is_a(expected_token))

if __name__ == '__main__':
    unittest.main()
