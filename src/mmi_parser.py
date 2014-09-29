import mmi_token as token

def constant_value():
    return Expression(0)

def function_call():
    return Expression(1)

class Expression:
    def __init__(self, exprtype):
        self.__exprtype = exprtype
    def is_a(self, expr):
        return self.__exprtype == expr.__exprtype

class Parser:
    def parse(self, tokens):
        next(tokens)
        try:
            next(tokens)
            yield function_call()
        except StopIteration:
            yield constant_value()
