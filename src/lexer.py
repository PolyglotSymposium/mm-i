class Lexer:
    def tokenize(self, characters):
        token = lambda: None
        token = decorate_with_type(token, characters)
        return [token]

def decorate_with_type(token, characters):
    if characters[0] in ["'", '"']:
        found_type = TokenType.string
    else:
        found_type = TokenType.integer
    token.is_a = lambda ttype: ttype == found_type

    token.raw_value = characters

    return token

class TokenType:
    def integer(): pass
    def string(): pass
