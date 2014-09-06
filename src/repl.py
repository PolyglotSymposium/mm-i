#!/usr/bin/python3

class Evaluator:
    def __init__(self, lexer):
        self.__lexer = lexer
    def evaluate(self, line):
        return int(next(self.__lexer.tokenize(line)).raw_value)

class REPL:
    def __init__(self, read, print, evaluate):
        self.__read = read
        self.__eval = evaluate
        self.__print = print

    def loop(self):
        while True:
            try:
                line = self.__read('mm-i> ')
                result = self.__eval(line)
                self.__print(result)
            except KeyboardInterrupt:
                break

if __name__ == '__main__':
    from lexer import Lexer
    REPL(input, print, Evaluator(Lexer()).evaluate).loop()
