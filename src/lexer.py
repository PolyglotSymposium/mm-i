import mmi_token as token
from matcher import WithinMatcher as within
from matcher import ExactLiteralMatcher as literal

string_matcher = within(token.string, ['"', "'"], escape = '\\')
left_paren_matcher = literal(token.left_paren, '(')
right_paren_matcher = literal(token.right_paren, ')')
left_square_bracket_matcher = literal(token.left_square_bracket, '[')
right_square_bracket_matcher = literal(token.right_square_bracket, ']')
function_matcher = literal(token.function, '->')
fourty_two_matcher = literal(token.integer, '42')

MATCHERS = [
    string_matcher,
    left_paren_matcher,
    right_paren_matcher,
    left_square_bracket_matcher,
    right_square_bracket_matcher,
    function_matcher,
    fourty_two_matcher
]

class Lexer:
    def __init__(self, matchers = MATCHERS):
        self.matchers = matchers

    def tokenize(self, characters):
        while characters:
            for matcher in self.matchers:
                match = matcher.match(characters)

                if match:
                    yield match
                    characters = matcher.remaining_text
                    break

            if not match:
                # So new tests will fail
                raise Exception("No match for '" + characters + "'")
