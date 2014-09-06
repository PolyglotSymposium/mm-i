STRING_DELIMITERS = ['"', "'"]

class Lexer:
    def __init__(self):
        self.__current_delim = None

    def tokenize(self, characters):
        tokens = []
        for word in self.__split_words(characters):
            token = lambda: None
            token.raw_value = word
            token = decorate_with_type(token)
            tokens.append(token)
        return tokens

    def __split_words(self, characters):
        current_word = ''
        for c in characters:
            current_word += c
            if c in STRING_DELIMITERS:
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

def decorate_with_type(token):
    if token.raw_value[0] in STRING_DELIMITERS:
        found_type = TokenType.string
    elif token.raw_value[0] == '(':
        found_type = TokenType.left_paren
    elif all_chars_are_numeric(token.raw_value):
        found_type = TokenType.integer
    else:
        found_type = TokenType.identifier

    token.is_a = lambda ttype: ttype == found_type

    return token

def all_chars_are_numeric(word):
    return len([i for i in word if 48 <= ord(i) and 57 >= ord(i)]) == len(word)

class TokenType:
    def integer(): pass
    def string(): pass
    def identifier(): pass
    def left_paren(): pass
