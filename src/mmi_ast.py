class Expression:
    def is_a(self, expr_class):
        return self.__class__ == expr_class
    
class ConstantValue(Expression):
    def __init__(self, value):
        pass

class FunctionCall(Expression):
    pass
