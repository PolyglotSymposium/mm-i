class Lexer:
    def tokenize(self, characters):
        token = lambda: None
        if characters[0] == "'":
          token.is_a = lambda ttype: ttype == TokenType().string()
        else:
          token.is_a = lambda ttype: ttype == TokenType().integer()
        return token

class TokenType:
    def integer(self):
        return 0

    def string(self):
        return 1
