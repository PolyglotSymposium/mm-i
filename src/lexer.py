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
        in_string = False
        words = []
        current = ''
        for c in characters:
            current += c
            if c == '"':
                in_string = not in_string
            elif in_string:
                continue
            elif c == ' ':
                words.append(current)
                current = ''
        words.append(current)
        return words


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
