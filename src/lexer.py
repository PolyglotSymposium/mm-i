STRING_DELIMITERS = ['"', "'"]

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
        self.__current_delim = None
        current = ''
        for c in characters:
            current += c
            if c in STRING_DELIMITERS:
                if self.__in_string() and self.__ends_string(c):
                    self.__current_delim = None
                elif not self.__in_string():
                    self.__current_delim = c
            elif not self.__in_string() and c == ' ':
                yield current
                current = ''
        yield current

    def __ends_string(self, char):
        return self.__current_delim == char

    def __in_string(self):
        return self.__current_delim


def decorate_with_type(token, characters):
    if characters[0] in STRING_DELIMITERS:
        found_type = TokenType.string
    else:
        found_type = TokenType.integer

    token.is_a = lambda ttype: ttype == found_type

    return token

class TokenType:
    def integer(): pass
    def string(): pass
