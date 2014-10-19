#!/usr/bin/python3

from freeform import spec, should
from lexer import *

spec('The lexer', Lexer,
    ('should parse', lambda lexer: lexer.tokenize,
        ('a ( character', lambda: '(',
            should('as a left-parenthesis token', lambda token:
                token.should_equal(token.left_paren())
            )
        ),
        ('a ) character', lambda: ')',
            should('as a right-parenthesis token', lambda token:
                token.should_equal(token.right_paren())
            )
        )
    )
)

if __name__ == '__main__':
    freeform.run_specs()
