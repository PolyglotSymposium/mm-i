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
            return string_token(word)
        if word.isdigit():
            return integer_token(word)
        return identifier_token(word)

    def __handle_string_delimiter(self, delim):
        if self.__lexing_string() and self.__ends_string(delim):
            self.__current_delim = None
        elif not self.__lexing_string():
            self.__current_delim = delim

    def __ends_string(self, char):
        return self.__current_delim == char

    def __lexing_string(self):
        return self.__current_delim

class Token:
    def __init__(self, word, ttype):
        self.raw_value = word
        self.__ttype = ttype

    def is_a(self, token):
        return self.__ttype == token.__ttype

def integer_token(word=None):
    return Token(word, 0)
def string_token(word=None): 
    return Token(word, 1)
def identifier_token(word=None):
    return Token(word, 2)
def left_paren_token(word=None):
    return Token(word, 3)
def right_paren_token(word=None):
    return Token(word, 4)
def right_square_bracket_token(word=None):
    return Token(word, 5)
def left_square_bracket_token(word=None):
    return Token(word, 6)

STRING_DELIMITERS = ['"', "'"]

CHAR_TO_TYPE = {
    '(': left_paren_token,
    ')': right_paren_token,
    ']': right_square_bracket_token,
    '[': left_square_bracket_token,
}

