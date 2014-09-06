#!/usr/bin/python3

import unittest
from lexer import Lexer, TokenType

class LexerSpecs(unittest.TestCase):
    def test_when_lexing_integer_type_is_integer(self):
        first_token = Lexer().tokenize('2814')[0]
        self.assertTrue(first_token.is_a(TokenType.integer))

    def test_when_lexing_a_single_quoted_thing_its_type_is_string(self):
        first_token = Lexer().tokenize("'single quoted!!!'")[0]
        self.assertTrue(first_token.is_a(TokenType.string))

    def test_when_lexing_a_double_quoted_thing_its_type_is_string(self):
        first_token = Lexer().tokenize('"double quoted = more work"')[0]
        self.assertTrue(first_token.is_a(TokenType.string))

if __name__ == '__main__':
    unittest.main()
