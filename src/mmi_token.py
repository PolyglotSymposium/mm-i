from itertools import count as __count

class Token:
    def __init__(self, word, ttype):
        self.raw_value = word
        self.__ttype = ttype

    def __eq__(self, other):
        return self.raw_value == other.raw_value and other.is_a(self)

    def is_a(self, token):
        return self.__ttype == token.__ttype

types = (
    (lambda ttype: lambda word=None: Token(word, ttype))(tt)
    for tt in __count())

# Content-bearing tokens
integer = next(types)
string = next(types)
identifier = next(types)
named_comma = next(types)
block_comment = next(types)
line_comment = next(types)

# Tokens which come in pairs
left_paren = next(types)
right_paren = next(types)
right_square_bracket = next(types)
left_square_bracket = next(types)

# Symbols
function = next(types)
pipe = next(types)
bind = next(types)
dot = next(types)
comma = next(types)
semicolon = next(types)
begin_block = next(types)
type_denote = next(types)
space = next(types)
tab = next(types)
