import mmi_token as token
from matcher import Within, Symbol

class Matches(object): # TODO I would like to get rid of this layer of indirection. It's not holding its weight.
    def __init__(self, match_type, *details, **params):
        self.match_type = match_type
        self.details = details
        self.params = params

    def to(self, value):
        return lambda: self.match_type(value, *self.details, **self.params)

MATCHERS = [
    # TODO I think an even more fluent interface would be appropriate here...
    # TODO because of the nature of the configuration we are doing...
    # TODO e.g. something like:
    # TODO
    # TODO Within('"').escaped_by('\\').match(token.string)
    # TODO Between('/*', '*/').match(token.block_comment)
    # TODO
    # TODO I don't know, it's late and I'm just thinking out loud. It doesn't
    # TODO seem like an escape character should be required.
    Matches(Within, ["'", '"'], escape = '\\').to(token.string), # TODO can we have an escaped_by method instead?
    # TODO also I think the fact that Within takes a list of delims is actually adding unneeded complexity
    # TODO I think the line above should be split into two lines, one for each type of quote
    # TODO That might feel more verbose, but it would actually be _simpler_
    Matches(Within, ['/*', '*/']).to(token.block_comment), # TODO can we allow different begin and endd matches?
    Matches(Symbol, '(').to(token.left_paren),
    Matches(Symbol, ')').to(token.right_paren),
    Matches(Symbol, '[').to(token.left_square_bracket),
    Matches(Symbol, ']').to(token.right_square_bracket),
    Matches(Symbol, '->').to(token.function),
    Matches(Symbol, '=').to(token.bind),
    Matches(Symbol, ',').to(token.comma),
    Matches(Symbol, ':').to(token.begin_block),
    Matches(Symbol, '42').to(token.integer)
]

class Lexer:
    def __init__(self, matchers = MATCHERS):
        self.matchers = matchers

    def tokenize(self, characters):
        while characters:
            for matcher in self.matchers:
                match = matcher().match(characters) # TODO why recreate the matcher every time?

                if match:
                    yield match
                    characters = matcher.remaining_text
                    break

            if not match:
                # So we don't end up in an infinite loop
                raise Exception("No match for '" + characters + "'")
