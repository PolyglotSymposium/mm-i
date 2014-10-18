#!/usr/bin/python3

import unittest
import mmi_token as token

class TokenSpecs(unittest.TestCase):
    def test_token_types_are_unique(self):
        self.assertTrue(token.integer().is_a(token.integer()))
        self.assertFalse(token.integer().is_a(token.string()))

    def test_tokens_with_the_same_type_and_different_data_are_not_equal(self):
        self.assertNotEqual(token.string('a'), token.string('b'))

    def test_tokens_with_the_different_type_and_same_data_are_not_equal(self):
        self.assertNotEqual(token.string('a'), token.identifier('a'))

    def test_tokens_with_the_same_type_and_data_are_equal(self):
        self.assertEqual(token.string('a'), token.string('a'))

if __name__ == '__main__':
    unittest.main()
