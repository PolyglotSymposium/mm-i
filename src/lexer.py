import mmi_token as token
from matcher import Within, Literal

class Matches(object):
    def __init__(self, match_type, *details, **params):
        self.match_type = match_type
        self.details = details
        self.params = params

    def to(self, value):
        return lambda: self.match_type(value, *self.details, **self.params)


MATCHERS = [
    Matches(Within, ["'", '"'], escape = '\\').to(token.string),
    Matches(Within, ['/*', '*/']).to(token.block_comment),
    Matches(Literal, '(').to(token.left_paren),
    Matches(Literal, ')').to(token.right_paren),
    Matches(Literal, '[').to(token.left_square_bracket),
    Matches(Literal, ']').to(token.right_square_bracket),
    Matches(Literal, '->').to(token.function),
    Matches(Literal, '=').to(token.bind),
    Matches(Literal, ',').to(token.comma),
    Matches(Literal, ':').to(token.begin_block),
    Matches(Literal, '42').to(token.integer)
]

class Lexer:
    def __init__(self, matchers = MATCHERS):
        self.matchers = matchers

    def tokenize(self, characters):
        while characters:
            for matcher in self.matchers:
                match = matcher().match(characters)

                if match:
                    yield match
                    characters = matcher.remaining_text
                    break

            if not match:
                # So we don't end up in an infinite loop
                raise Exception("No match for '" + characters + "'")
