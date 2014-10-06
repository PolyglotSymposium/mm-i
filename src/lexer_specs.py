#!/usr/bin/python3

import unittest
from lexer import *

def nth(generator, n):
    for i in range(1, n):
        next(generator)
    return next(generator)

def tokenize(text):
    return Lexer().tokenize(text)

def first_token(chars):
    return next(tokenize(chars))

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

    def test_bind_type(self):
        self.assert_first_token('=', token.bind())

    def test_comma_type(self):
        self.assert_first_token(',', token.comma())

    def test_string_type(self):
        self.assert_first_token("'this is a string'", token.string())

    def test_string_value(self):
        self.assert_first_value("'this is a string'", 'this is a string')

    def assert_first_value(self, chars, expected_value):
        self.assertEqual(expected_value, first_token(chars).raw_value)

    def assert_first_token(self, chars, expected_token):
        self.assertTrue(first_token(chars).is_a(expected_token))

if __name__ == '__main__':
    unittest.main()
