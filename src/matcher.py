class WithinMatcher(object):
    def __init__(self, token, delims, **keyargs):
        self.delims = delims
        self.token = token
        self.escape = keyargs['escape']
        self.last_was_escape = False
        self.result_value = ''
        self.amount_to_chomp = 2

    def match(self, text):
        if not self.__is_delim(text[0]): return None
        self.delim = text[0]

        for c in text[1:]:
            if self.__is_escape_character(c):
                self.__chomp_escape(c)
            elif self.__is_ending_delim(c):
                return self.__split_remaining_text_and_get_token(text)
            else:
                self.__chomp_non_escape(c)

    def __split_remaining_text_and_get_token(self, text):
        self.remaining_text = text[self.amount_to_chomp:]
        return self.token(self.result_value)

    def __chomp_escape(self, char):
        self.amount_to_chomp += 1
        self.last_was_escape = True

    def __chomp_non_escape(self, char):
        self.amount_to_chomp += 1
        self.result_value += char
        self.last_was_escape = False

    def __is_delim(self, char):
        return char in self.delims

    def __is_escape_character(self, char):
        return char == self.escape

    def __is_ending_delim(self, char):
        return char == self.delim and not self.last_was_escape
