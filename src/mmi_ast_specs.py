#!/usr/bin/python3

import unittest
from mmi_ast import ConstantValue, FunctionCall

class AbstractSyntaxTreeSpecs(unittest.TestCase):
    def test_expression_types_are_unique(self):
        self.assertTrue(ConstantValue(1126).is_a(ConstantValue))
        self.assertFalse(ConstantValue(1126).is_a(FunctionCall))

if __name__ == '__main__':
    unittest.main()
