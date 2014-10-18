import mmi_ast as ast

class Parser:
    def parse(self, tokens):
        token1 = next(tokens)
        try:
            next(tokens)
            yield ast.FunctionCall()
        except StopIteration:
            yield ast.ConstantValue(token1)
