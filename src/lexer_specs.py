#!/usr/bin/python3

import unittest
from lexer import Lexer, TokenType

class LexerSpecs(unittest.TestCase):
    def test_when_lexing_integer_type_is_integer(self):
        token = Lexer().tokenize('2814')
        self.assertTrue(token.is_a(TokenType().integer()))

if __name__ == '__main__':
    unittest.main()
