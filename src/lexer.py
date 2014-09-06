class Lexer:
    def tokenize(self, characters):
        token = lambda: None
        if characters[0] in ["'", '"']:
          token.is_a = lambda ttype: ttype == TokenType.string
        else:
          token.is_a = lambda ttype: ttype == TokenType.integer
        return token

class TokenType:
    def integer(): pass
    def string(): pass
