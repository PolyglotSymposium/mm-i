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

string_matcher = Matches(within, ["'", '"'], escape = '\\').to(token.string)
left_paren_matcher = Matches(literal, '(').to(token.left_paren)
right_paren_matcher = Matches(literal, ')').to(token.right_paren)
left_square_bracket_matcher = Matches(literal, '[').to(token.left_square_bracket)
right_square_bracket_matcher = Matches(literal, ']').to(token.right_square_bracket)
function_matcher = Matches(literal, '->').to(token.function)
bind_matcher = Matches(literal, '=').to(token.bind)
comma_matcher = Matches(literal, ',').to(token.comma)
forty_two_matcher = Matches(literal, '42').to(token.integer)

MATCHERS = [
    string_matcher,
    left_paren_matcher,
    right_paren_matcher,
    left_square_bracket_matcher,
    right_square_bracket_matcher,
    function_matcher,
    bind_matcher,
    comma_matcher,
    forty_two_matcher
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
                # So new tests will fail
                raise Exception("No match for '" + characters + "'")
