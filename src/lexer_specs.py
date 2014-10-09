#!/usr/bin/python3

import unittest
from lexer import *

def nth(generator, n):
    for i in range(1, n):
        next(generator)
    return next(generator)

tokenize = lambda text: Lexer().tokenize(text)
first_token = lambda chars: next(tokenize(chars))

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

    def test_parses_pipe(self):
        self.assert_first_token('|', token.pipe())

    def test_comma_type(self):
        self.assert_first_token(',', token.comma())

    def test_parses_dot(self):
        self.assert_first_token('.', token.dot())

    def test_parses_semicolon(self):
        self.assert_first_token(';', token.semicolon())

    def test_begin_block_type(self):
        self.assert_first_token(':', token.begin_block())

    def test_begin_block_type(self):
        self.assert_first_token('/* block comment */', token.block_comment())

    def test_string_type(self):
        self.assert_first_token("'this is a string'", token.string())

    def test_string_value(self):
        self.assert_first_value("'this is a string'", 'this is a string')

    def test_parses_integers(self):
        self.assert_first_token('42', token.integer())
        self.assert_first_value('42', '42')
        self.assert_first_token('1337', token.integer())
        self.assert_first_value('1337', '1337')

    def test_parses_alphabetic_as_identifier(self):
        self.assert_first_token('foo', token.identifier())
        self.assert_first_value('foo', 'foo')

    def test_parses_alphanumeric_as_identifier(self):
        self.assert_first_token('forty2', token.identifier())
        self.assert_first_value('forty2', 'forty2')

    def test_parses_minus_as_identifier(self):
        self.assert_first_token('-', token.identifier())

    def test_parses_underscore_as_identifier(self):
        self.assert_first_token('_', token.identifier())

    def test_parses_plus_as_identifier(self):
        self.assert_first_token('+', token.identifier())

    def test_parses_times_as_identifier(self):
        self.assert_first_token('*', token.identifier())

    def test_parses_slash_as_identifier(self):
        self.assert_first_token('/', token.identifier())

    def test_parses_question_mark_as_identifier(self):
        self.assert_first_token('?', token.identifier())

    def test_parses_angle_brackets_as_identifier(self):
        self.assert_first_token('<>', token.identifier())

    def test_parses_equals_sign_as_identifier(self):
        self.assert_first_token('=', token.identifier())

    ## Helpers

    def assert_first_value(self, chars, expected_value):
        self.assertEqual(expected_value, first_token(chars).raw_value)

    def assert_first_token(self, chars, expected_token):
        self.assertTrue(first_token(chars).is_a(expected_token))

if __name__ == '__main__':
    unittest.main()
