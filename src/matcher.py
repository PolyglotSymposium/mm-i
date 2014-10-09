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

class While(BaseMatcher):
    def __init__(self, condition):
        self.meets_condition = condition

    def match(self, text):
        if not self.meets_condition(text[0]): return None

        result_value = ''
        amount_to_chomp = 0
        for c in text:
            if not self.meets_condition(c):
                break
            amount_to_chomp += 1
            result_value += c

        self.remaining_text = text[amount_to_chomp:]
        return self.token(result_value)

class Within(BaseMatcher):
    def __init__(self, delim, ending_delim = None):
        self.delim = delim
        self.ending_delim = ending_delim or delim
        self.__reset()
        self.escape = None

    def escaped_by(self, escape_character):
        self.escape = escape_character
        return self

    def match(self, text):
        if not text.startswith(self.delim): return None

        for c in text[len(self.delim):]:
            if self.escape == c:
                self.__chomp_escape(c)
            elif self.__is_ending_delim(text):
                result = self.token(self.result_value)
                self.remaining_text = text[self.amount_to_chomp:]
                self.__reset()
                return result
            else:
                self.__chomp_non_escape(c)

    def __reset(self):
        self.last_was_escape = False
        self.result_value = ''
        self.amount_to_chomp = len(self.delim + self.ending_delim)

    def __chomp_escape(self, char):
        self.amount_to_chomp += 1
        self.last_was_escape = True

    def __chomp_non_escape(self, char):
        self.amount_to_chomp += 1
        self.result_value += char
        self.last_was_escape = False

    def __is_ending_delim(self, text):
        return self.__current_chomp(text).startswith(self.ending_delim) and not self.last_was_escape

    def __current_chomp(self, text):
        return text[self.amount_to_chomp-len(self.ending_delim):]
