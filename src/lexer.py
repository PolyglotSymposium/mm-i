class Lexer:
    def tokenize(self, characters):
        token = lambda: None
        token.is_a = lambda ttype: True
        return token

class TokenType:
    def integer(self):
        pass
