import mmi_ast as ast

class Parser:
    def parse(self, tokens):
        token1 = next(tokens)
        try:
            token2 = next(tokens)
            yield ast.FunctionCall(token1, [token2])
        except StopIteration:
            yield ast.ConstantValue(token1)
