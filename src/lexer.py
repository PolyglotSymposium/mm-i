class Lexer:
    def __init__(self):
        self.__current_delim = None

    def tokenize(self, characters):
        tokens = []
        for word in self.__split_words(characters):
            token = lambda: None
            token.raw_value = word
            token.is_a = lambda ttype: ttype == TokenTypeFactory(token).create()
            tokens.append(token)
        return tokens

    def __split_words(self, characters):
        current_word = ''
        for c in characters:
            current_word += c
            if current_word in CHAR_TO_TYPE:
                yield current_word
                current_word = ''
            elif c in STRING_DELIMITERS:
                self.__handle_string_delimiter(c)
            elif not self.__lexing_string() and c == ' ':
                if current_word != ' ':
                    yield current_word[:-1]
                current_word = ''
        if current_word != '':
            yield current_word

    def __handle_string_delimiter(self, delim):
        if self.__lexing_string() and self.__ends_string(delim):
            self.__current_delim = None
        elif not self.__lexing_string():
            self.__current_delim = delim

    def __ends_string(self, char):
        return self.__current_delim == char

    def __lexing_string(self):
        return self.__current_delim

class TokenType:
    def integer(): pass
    def string(): pass
    def identifier(): pass
    def left_paren(): pass
    def right_paren(): pass
    def right_square_bracket(): pass
    def left_square_bracket(): pass

class TokenTypeFactory:
    def __init__(self, token):
        self.__text = token.raw_value

    def create(self):
        if self.__text[0] in STRING_DELIMITERS:
            return TokenType.string
        elif self.__text[0] in CHAR_TO_TYPE:
            return CHAR_TO_TYPE[self.__text[0]]
        elif self.__all_chars_are_numeric():
            return TokenType.integer

        return TokenType.identifier

    def __all_chars_are_numeric(self):
        return len([i for i in self.__text if 48 <= ord(i) and 57 >= ord(i)]) == len(self.__text)

STRING_DELIMITERS = ['"', "'"]

CHAR_TO_TYPE = {
    '(': TokenType.left_paren,
    ')': TokenType.right_paren,
    ']': TokenType.right_square_bracket,
    '[': TokenType.left_square_bracket,
}
