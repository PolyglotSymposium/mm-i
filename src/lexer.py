class Lexer:
    def __init__(self):
        self.__current_delim = None

    def tokenize(self, characters):
        return [TokenFactory().create(word) for word in self.__split_words(characters)]

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

class Token:
    def __init__(self, word, ttype):
        self.raw_value = word
        self.__ttype = ttype

    def is_a(self, ttype):
        return self.__ttype == ttype

class TokenType:
    def integer(): pass
    def string(): pass
    def identifier(): pass
    def left_paren(): pass
    def right_paren(): pass
    def right_square_bracket(): pass
    def left_square_bracket(): pass

class TokenFactory:
    def create(self, word):
        return Token(word, self.__get_type(word))
    def __get_type(self, word):
        if word[0] in STRING_DELIMITERS:
            return TokenType.string
        if word[0] in CHAR_TO_TYPE:
            return CHAR_TO_TYPE[word[0]]
        if word.isdigit():
            return TokenType.integer
        return TokenType.identifier

STRING_DELIMITERS = ['"', "'"]

CHAR_TO_TYPE = {
    '(': TokenType.left_paren,
    ')': TokenType.right_paren,
    ']': TokenType.right_square_bracket,
    '[': TokenType.left_square_bracket,
}

