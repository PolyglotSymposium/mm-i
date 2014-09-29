#!/usr/bin/python3

import unittest
import mmi_token as token
from mmi_parser import Parser, constant_value

class ParserSpecs(unittest.TestCase):
    def test_single_token_in_input_stream_results_in_single_expression_in_output_stream(self):
        def one_token():
            yield token.integer()
        expressions = Parser().parse(one_token())
        self.assertEqual(1, len(list(expressions)))
    def test_single_token_in_input_stream_results_in_constant_value_expression(self):
        def one_token():
            yield token.integer()
        expr = next(Parser().parse(one_token()))
        self.assertTrue(expr.is_a(constant_value()))

if __name__ == '__main__':
    unittest.main()
