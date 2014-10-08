#!/usr/bin/python3

import unittest
from matcher import *
import mmi_token

class MockToken(object):
    def __init__(self, value):
        self.raw_value = value

class ExactLiteralMatcherSpecs(unittest.TestCase):
    def example_exact_literal_matcher(self):
        return ExactLiteralMatcher(MockToken, '->')  

    def test_matches(self):
        self.assertTrue(self.example_exact_literal_matcher().match('->'))

    def test_no_match_if_first_is_different(self):
        self.assertFalse(self.example_exact_literal_matcher().match('_>'))

    def test_match_even_if_later_text_is_there(self):
        self.assertTrue(self.example_exact_literal_matcher().match('->later text'))

    def test_match_calculates_correct_remaining_text(self):
        matcher = self.example_exact_literal_matcher()
        matcher.match('->later text')
        self.assertEqual('later text', matcher.remaining_text)

class UntilMatcherSpecs(unittest.TestCase):
    def example_until_matcher(self):
        return UntilMatcher(MockToken, lambda c: c in ' \t\n')

    def test_matches_but_not_as_the_first_character(self):
        self.assertEqual(
            None,
            self.example_until_matcher().match(' foobar'))

    def test_matches(self):
        self.assertEqual(
            'foobar',
            self.example_until_matcher().match('foobar and stuff').raw_value)

    def test_matches_and_ends_string(self):
        self.assertEqual(
            'foobar',
            self.example_until_matcher().match('foobar').raw_value)

    def test_matches_has_correct_remaining_value(self):
        matcher = self.example_until_matcher()
        matcher.match("foobar and stuff")
        self.assertEqual(
            " and stuff",
            matcher.remaining_text)

class WhileMatcherSpecs(unittest.TestCase):
    def example_while_matcher(self):
        return WhileMatcher(MockToken, lambda c: c not in ' \t\n')

    def test_matches_but_not_as_the_first_character(self):
        self.assertEqual(
            None,
            self.example_while_matcher().match(' foobar'))

    def test_matches(self):
        self.assertEqual(
            'foobar',
            self.example_while_matcher().match('foobar and stuff').raw_value)

    def test_matches_and_ends_string(self):
        self.assertEqual(
            'foobar',
            self.example_while_matcher().match('foobar').raw_value)

    def test_matches_has_correct_remaining_value(self):
        matcher = self.example_while_matcher()
        matcher.match("foobar and stuff")
        self.assertEqual(
            " and stuff",
            matcher.remaining_text)

class WithinMatcherSpecs(unittest.TestCase):
    def example_string_matcher(self):
        return WithinMatcher(mmi_token.string, '"\'', escape = '\\')

    def test_does_not_match_the_given_value(self):
        self.assertEqual(
            None,
            self.example_string_matcher().match('no quotes here'))

    def test_matches_but_not_as_the_first_character(self):
        self.assertEqual(
            None,
            self.example_string_matcher().match("there's a late quote here"))

    def test_matches(self):
        self.assertEqual(
            'foobar',
            self.example_string_matcher().match("'foobar' and stuff").raw_value)

    def test_has_different_later_quote(self):
        self.assertEqual(
            None,
            self.example_string_matcher().match("'foobar\" and stuff"))

    def test_has_escaped_quote(self):
        self.assertEqual(
            "foo's bar",
            self.example_string_matcher().match("'foo\\'s bar' and stuff").raw_value)

    def test_matches_and_has_remaining_text(self):
        matcher = self.example_string_matcher()
        matcher.match("'foo\\'s bar and fig\\'s foo' and stuff")
        self.assertEqual(
            " and stuff",
            matcher.remaining_text)

if __name__ == '__main__':
    unittest.main()
