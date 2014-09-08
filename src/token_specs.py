#!/usr/bin/python3

import unittest
import mmitoken as token

class TokenSpecs(unittest.TestCase):
    def test_token_types_are_unique(self):
        self.assertFalse(token.integer().is_a(token.string()))

if __name__ == '__main__':
    unittest.main()
