#!/usr/bin/python3

import unittest
import mmi_token as token
from mmi_parser import Parser, constant_value, function_call

def one_integer():
    yield token.integer()

def two_identifiers():
    yield token.identifier()
    yield token.identifier()

class ParserSpecs(unittest.TestCase):
    def test_single_token_in_input_stream_results_in_single_expression_in_output_stream(self):
        expressions = Parser().parse(one_integer())
        self.assertEqual(1, len(list(expressions)))

    def test_single_integer_token_parses_to_constant_value_expression(self):
        expr = next(Parser().parse(one_integer()))
        self.assertTrue(expr.is_a(constant_value()))

    def test_two_identifier_tokens_parse_to_function_application(self):
        expr = next(Parser().parse(two_identifiers()))
        self.assertTrue(expr.is_a(function_call()))

if __name__ == '__main__':
    unittest.main()
