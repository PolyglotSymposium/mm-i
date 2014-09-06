class Lexer:
    def tokenize(self, characters):
        tokens = []
        for word in self.__split_words(characters):
            token = lambda: None
            token = decorate_with_type(token, word)
            token.raw_value = word
            tokens.append(token)
        return tokens

    def __split_words(self, characters):
        current_delim = None
        current = ''
        for c in characters:
            current += c
            if c in ['"', "'"]:
                current_delim = None if current_delim else c
            elif current_delim:
                continue
            elif c == ' ':
                yield current
                current = ''
        yield current


def decorate_with_type(token, characters):
    if characters[0] in ["'", '"']:
        found_type = TokenType.string
    else:
        found_type = TokenType.integer

    token.is_a = lambda ttype: ttype == found_type

    return token

class TokenType:
    def integer(): pass
    def string(): pass
