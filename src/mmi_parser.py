import mmi_token as token

def constant_value():
    pass

def function_call():
    pass

class Expression:
    def is_a(self, exprtype):
        return True

class Parser:
    def parse(self, tokens):
        yield Expression()
