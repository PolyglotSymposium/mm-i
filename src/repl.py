class Evaluator:
    def __init__(self, print):
        self.__print = print
    def eval_and_print(self, line):
        self.__print(42)
