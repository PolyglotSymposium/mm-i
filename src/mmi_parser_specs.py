#!/usr/bin/python3

import unittest
import mmi_token as token
from mmi_parser import Parser
from mmi_ast import ConstantValue, FunctionCall

def one_integer(x=0):
    yield token.integer(x)

def n_identifiers(n):
    for i in range(n):
        yield token.identifier('id%d' % i)

class ParserSpecs(unittest.TestCase):
    def test_single_token_in_input_stream_results_in_single_expression_in_output_stream(self):
        expressions = Parser().parse(one_integer())
        self.assertEqual(1, len(list(expressions)))

    def test_single_integer_token_parses_as_constant_value_expression(self):
        expr = next(Parser().parse(one_integer(7)))
        self.assertTrue(expr.is_a(ConstantValue))
        self.assertEqual(token.integer(7), expr.token)

    def test_two_identifier_tokens_parse_as_function_application(self):
        expr = next(Parser().parse(n_identifiers(2)))
        self.assertTrue(expr.is_a(FunctionCall))

    def test_two_identifier_tokens_parse_as_second_applied_to_first(self):
        expr = next(Parser().parse(n_identifiers(2)))
        self.assertEqual(token.identifier('id0'), expr.function)
        self.assertEqual(token.identifier('id1'), expr.arguments[0])

    def test_three_identifier_tokens_parse_to_function_application(self):
        expr = next(Parser().parse(n_identifiers(3)))
        self.assertTrue(expr.is_a(FunctionCall))

    def test_three_identifier_tokens_parse_as_first_and_third_applied_to_second(self):
        expr = next(Parser().parse(n_identifiers(3)))
        self.assertEqual(token.identifier('id1'), expr.function)
        self.assertEqual(token.identifier('id0'), expr.arguments[0])
        self.assertEqual(token.identifier('id2'), expr.arguments[1])

if __name__ == '__main__':
    unittest.main()
