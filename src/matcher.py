class BaseMatcher(object):
    def matches_to(self, value):
        self.token = value
        return self

class ExactText(BaseMatcher):
    def __init__(self, text):
        self.text = text

    def match(self, text):
        if text[:len(self.text)] == self.text:
            self.remaining_text = text[len(self.text):]
            return self.token(self.text)

class Within(BaseMatcher):
    def __init__(self, delim):
        self.delim = delim
        self.last_was_escape = False
        self.result_value = ''
        self.amount_to_chomp = 2
        self.escape = None

    def escaped_by(self, escape_character):
        self.escape = escape_character
        return self

    def match(self, text):
        if not text[0] == self.delim: return None

        for c in text[1:]:
            if self.__is_escape_character(c):
                self.__chomp_escape(c)
            elif self.__is_ending_delim(c):
                result = self.token(self.result_value)
                self.remaining_text = text[self.amount_to_chomp:]
                self.__reset()
                return result
            else:
                self.__chomp_non_escape(c)

    def __reset(self):
        self.result_value = ''
        self.amount_to_chomp = 2

    def __chomp_escape(self, char):
        self.amount_to_chomp += 1
        self.last_was_escape = True

    def __chomp_non_escape(self, char):
        self.amount_to_chomp += 1
        self.result_value += char
        self.last_was_escape = False

    def __is_delim(self, char):
        return char == self.delim

    def __is_escape_character(self, char):
        return char == self.escape

    def __is_ending_delim(self, char):
        return char == self.delim and not self.last_was_escape
