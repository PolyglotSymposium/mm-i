#!/usr/bin/python3

import unittest
from matcher import *
import mmi_token

class TestWithinMatcher(unittest.TestCase):
    def example_string_matcher(self):
        return WithinMatcher(mmi_token.string, ['"', "'"], escape = '\\')

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
