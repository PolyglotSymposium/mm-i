#!/usr/bin/python3

from freeverse import spec, expect

import mmi_token as token
from mmi_parser import Parser
from mmi_ast import ConstantValue, FunctionCall

def one_integer(x=0):
    yield token.integer(x)

spec(('The MM/I Parser', Parser,
    ('when it parses', lambda parser: parser.parse,
        ('a single-token input stream', lambda parse: parse(one_integer()),
            ('should yield a single-expression output stream', lambda stream:
                expect(len(list(stream))).to_be(1)
            )
        ),
        ('a stream which begins with an integer token', lambda parse: parse(one_integer(7)),
            ('the first expression in the output stream', lambda ouput: next(ouput),
                ('should be a single, constant-value expression', lambda expr:
                    expect(expr.is_a(ConstantValue)).to_be(True)
                )
            )
        )
    )
))

if __name__ == '__main__':
    freeverse.run_specs()
