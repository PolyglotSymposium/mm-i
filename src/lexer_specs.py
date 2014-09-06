#!/usr/bin/python3

import unittest
from lexer import Lexer, TokenType

class LexerSpecs(unittest.TestCase):
    def test_when_lexing_integer_type_is_integer(self):
        first_token = Lexer().tokenize('2814')[0]
        self.assertTrue(first_token.is_a(TokenType.integer))

    def test_when_lexing_integer_with_value_42_its_raw_value_is_42(self):
        first_token = Lexer().tokenize('42')[0]
        self.assertEqual('42', first_token.raw_value)

    def test_when_lexing_string_with_value_42_its_raw_value_is_42_quoted(self):
        first_token = Lexer().tokenize('"42"')[0]
        self.assertEqual('"42"', first_token.raw_value)

    def test_when_lexing_two_integers_two_tokens_come_back(self):
        tokens = Lexer().tokenize('42 35')
        self.assertEqual(2, len(tokens))

    def test_when_lexing_two_integers_first_is_integer(self):
        first_token = Lexer().tokenize('42 35')[0]
        self.assertTrue(first_token.is_a(TokenType.integer))

    def test_when_lexing_two_integers_second_is_integer(self):
        second_token = Lexer().tokenize('42 35')[1]
        self.assertTrue(second_token.is_a(TokenType.integer))

    def test_when_lexing_two_integers_second_has_correct_raw_value(self):
        second_token = Lexer().tokenize('42 35')[1]
        self.assertEqual('35', second_token.raw_value)

    def test_when_lexing_a_single_quoted_thing_its_type_is_string(self):
        first_token = Lexer().tokenize("'single-quoted!!!'")[0]
        self.assertTrue(first_token.is_a(TokenType.string))

    def test_when_lexing_a_double_quoted_thing_its_type_is_string(self):
        first_token = Lexer().tokenize('"double-quoted=more-work"')[0]
        self.assertTrue(first_token.is_a(TokenType.string))

    def test_when_lexing_double_quoted_string_with_spaces_in_it_one_token_is_returned(self):
        tokens = Lexer().tokenize('"string with spaces"')
        self.assertEqual(1, len(tokens))

    def test_when_lexing_single_quoted_string_with_spaces_in_it_one_token_is_returned(self):
        tokens = Lexer().tokenize("'string with spaces'")
        self.assertEqual(1, len(tokens))

    def test_when_lexing_double_quoted_string_with_spaces_in_it_its_raw_value_is_correct(self):
        first_token = Lexer().tokenize('"string with spaces"')[0]
        self.assertEqual('"string with spaces"', first_token.raw_value)

if __name__ == '__main__':
    unittest.main()
