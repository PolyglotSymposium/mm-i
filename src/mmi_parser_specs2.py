#!/usr/bin/python3

from freeverse import SpecFor, Should, Expect, FlatOutput

import mmi_token as token
from mmi_parser import Parser
from mmi_ast import ConstantValue, FunctionCall

def one_integer(x=0):
    yield token.integer(x)

spec = SpecFor('The MM/I Parser')

spec.add('Parsing', lambda: Parser().parse,
    ('a single-token input stream', lambda parse: parse(one_integer()),
        Should('yield a single-expression output stream', lambda stream:
            Expect(len(list(stream))).to_be(1)
        )
    ),
    ('a stream which begins with an integer token', lambda parse: parse(one_integer(7)),
        ('the first expression in the output stream', lambda ouput: next(ouput),
            Should('be a single, constant-value expression', lambda expr:
                Expect(expr.is_a(ConstantValue)).to_be(True)
            )
        )
    )
)

if __name__ == '__main__':
    import sys
    spec.run_and_write_to(FlatOutput(sys.stdout))
