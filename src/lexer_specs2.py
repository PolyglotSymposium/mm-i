#!/usr/bin/python3

from freeverse import SpecFor, Should, Expect, FlatOutput
from lexer import *

spec = SpecFor('The MM/I Lexer')

spec.add('The lexer', Lexer,
    ('should parse', lambda lexer: lexer.tokenize,
        ('a ( character', lambda: '(',
            ('as a left-parenthesis token', lambda token:
                token.should_be(token.left_paren())
            )
        ),
        ('a ) character', lambda: ')',
            ('as a right-parenthesis token', lambda token:
                token.should_be(token.right_paren())
            )
        )
    )
)

if __name__ == '__main__':
    import sys
    spec.run_and_write_to(FlatOutput(sys.stdout))
