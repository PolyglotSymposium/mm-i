import mmi_token as token
from matcher import WithinMatcher as within
from matcher import ExactLiteralMatcher as literal

class Matches(object):
    def __init__(self, match_type, *details, **params):
        self.match_type = match_type
        self.details = details
        self.params = params

    def to(self, value):
        return lambda: self.match_type(value, *self.details, **self.params)


MATCHERS = [
    Matches(within, ["'", '"'], escape = '\\').to(token.string),
    Matches(literal, '(').to(token.left_paren),
    Matches(literal, ')').to(token.right_paren),
    Matches(literal, '[').to(token.left_square_bracket),
    Matches(literal, ']').to(token.right_square_bracket),
    Matches(literal, '->').to(token.function),
    Matches(literal, '=').to(token.bind),
    Matches(literal, ',').to(token.comma),
    Matches(literal, ':').to(token.begin_block),
    Matches(literal, '42').to(token.integer)
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
