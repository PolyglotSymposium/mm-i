#!/usr/bin/python3

import unittest
from lexer import *

def nth(generator, n):
    for i in range(1, n):
        next(generator)
    return next(generator)

def tokenize(text):
    return Lexer().tokenize(text)

def get_first_token(to_tokenize):
    return next(tokenize(to_tokenize))

class LexerSpecs(unittest.TestCase):
    def test_when_lexing_multiple_spaces_no_tokens_are_returned(self):
        tokens = tokenize('       ')
        self.assertEqual([], list(tokens))

    def test_when_lexing_integer_type_is_integer(self):
        first_token = get_first_token('2814')
        self.assertTrue(first_token.is_a(token.integer()))

    def test_when_begins_numeric_and_becomes_chars_its_an_identifier(self):
        first_token = get_first_token('42answer')
        self.assertTrue(first_token.is_a(token.identifier()))

    def test_when_lexing_integer_with_value_42_its_raw_value_is_42(self):
        first_token = get_first_token('42')
        self.assertEqual('42', first_token.raw_value)

    def test_when_lexing_string_with_value_42_its_raw_value_is_42_quoted(self):
        first_token = get_first_token('"42"')
        self.assertEqual('"42"', first_token.raw_value)

    def test_when_lexing_two_integers_two_tokens_come_back(self):
        tokens = tokenize('42 35')
        self.assertEqual(2, len(list(tokens)))

    def test_when_lexing_two_integers_first_is_integer(self):
        first_token = get_first_token('42 35')
        self.assertTrue(first_token.is_a(token.integer()))

    def test_when_lexing_two_integers_first_has_correct_value(self):
        first_token = get_first_token('42 35')
        self.assertEqual('42', first_token.raw_value)

    def test_when_lexing_two_integers_second_is_integer(self):
        second_token = nth(tokenize('42 35'), 2)
        self.assertTrue(second_token.is_a(token.integer()))

    def test_when_lexing_two_integers_second_has_correct_raw_value(self):
        second_token = nth(tokenize('42 35'), 2)
        self.assertEqual('35', second_token.raw_value)

    def test_when_lexing_a_single_quoted_thing_its_type_is_string(self):
        first_token = get_first_token("'single-quoted!!!'")
        self.assertTrue(first_token.is_a(token.string()))

    def test_when_lexing_a_double_quoted_thing_its_type_is_string(self):
        first_token = get_first_token('"double-quoted=more-work"')
        self.assertTrue(first_token.is_a(token.string()))

    def test_when_lexing_double_quoted_string_with_spaces_in_it_one_token_is_returned(self):
        tokens = tokenize('"string with spaces"')
        self.assertEqual(1, len(list(tokens)))

    def test_when_lexing_single_quoted_string_with_spaces_in_it_one_token_is_returned(self):
        tokens = tokenize("'string with spaces'")
        self.assertEqual(1, len(list(tokens)))

    def test_when_lexing_single_quoted_string_with_double_quotes_in_it_one_token_is_returned(self):
        tokens = tokenize("'quo\"te'")
        self.assertEqual(1, len(list(tokens)))

    def test_when_lexing_double_quoted_string_with_single_quotes_in_it_one_token_is_returned(self):
        tokens = tokenize('"quo\'te"')
        self.assertEqual(1, len(list(tokens)))

    def test_when_lexing_double_quoted_string_with_spaces_in_it_its_raw_value_is_correct(self):
        first_token = get_first_token('"string with spaces"')
        self.assertEqual('"string with spaces"', first_token.raw_value)

    def test_quotes_and_spaces_in_string_is_still_single_string(self):
        tokens = tokenize('"quo\'te f\'oo  bar\'"')
        self.assertEqual(1, len(list(tokens)))

    def test_plus_sign_is_just_an_generic_identifier(self):
        first_token = get_first_token('+')
        self.assertTrue(first_token.is_a(token.identifier()))

    def test_left_paren_type(self):
        first_token = get_first_token('(')
        self.assertTrue(first_token.is_a(token.left_paren()))

    def test_right_paren_type(self):
        first_token = get_first_token(')')
        self.assertTrue(first_token.is_a(token.right_paren()))

    def test_paren_mashed_with_identifier_is_two_tokens(self):
        tokens = tokenize(')mash')
        self.assertEqual(2, len(list(tokens)))

    def test_left_square_bracket_type(self):
        first_token = get_first_token('[')
        self.assertTrue(first_token.is_a(token.left_square_bracket()))

    def test_right_square_bracket_type(self):
        first_token = get_first_token(']')
        self.assertTrue(first_token.is_a(token.right_square_bracket()))

if __name__ == '__main__':
    unittest.main()
