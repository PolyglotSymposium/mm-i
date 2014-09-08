from itertools import count as __count

class Token:
    def __init__(self, word, ttype):
        self.raw_value = word
        self.__ttype = ttype

    def is_a(self, token):
        return self.__ttype == token.__ttype

types = (
    (lambda ttype: lambda word=None: Token(word, ttype))(tt)
    for tt in __count())

integer = next(types)
string = next(types)
identifier = next(types)
left_paren = next(types)
right_paren = next(types)
right_square_bracket = next(types)
left_square_bracket = next(types)

