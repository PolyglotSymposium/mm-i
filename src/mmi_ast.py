class Expression:
    def is_a(self, expr_class):
        return self.__class__ == expr_class
    
class ConstantValue(Expression):
    def __init__(self, value_token):
        self.token = value_token

class FunctionCall(Expression):
    pass
