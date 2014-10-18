import mmi_ast as ast

class Parser:
    def parse(self, tokens):
        token1 = next(tokens)
        try:
            token2 = next(tokens)
            try:
                token3 = next(tokens)
                yield ast.FunctionCall(token2, [token1, token3])
            except StopIteration:
                yield ast.FunctionCall(token1, [token2])
        except StopIteration:
            yield ast.ConstantValue(token1)
