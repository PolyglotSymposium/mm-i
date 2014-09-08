import mmitoken as token

class Lexer:
    def __init__(self):
        self.__current_delim = None # This is bad. The lexer itself should not be stateful.

    def tokenize(self, characters):
        current_word = ''
        for c in characters:
            current_word += c
            if current_word in CHAR_TO_TYPE:
                yield CHAR_TO_TYPE[current_word](current_word)
                current_word = ''
            elif c in STRING_DELIMITERS:
                self.__handle_string_delimiter(c)
            elif not self.__lexing_string() and c == ' ':
                if current_word != ' ':
                    yield self.__get_token(current_word[:-1])
                current_word = ''
        if current_word != '':
            yield self.__get_token(current_word)

    def __get_token(self, word):
        if word[0] in STRING_DELIMITERS:
            return token.string(word)
        if word.isdigit():
            return token.integer(word)
        return token.identifier(word)

    def __handle_string_delimiter(self, delim):
        if self.__lexing_string() and self.__ends_string(delim):
            self.__current_delim = None
        elif not self.__lexing_string():
            self.__current_delim = delim

    def __ends_string(self, char):
        return self.__current_delim == char

    def __lexing_string(self):
        return self.__current_delim

STRING_DELIMITERS = ['"', "'"]

CHAR_TO_TYPE = {
    '(': token.left_paren,
    ')': token.right_paren,
    ']': token.right_square_bracket,
    '[': token.left_square_bracket,
}

