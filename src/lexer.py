import mmi_token as token
from matcher import Within, ExactText, While, Compound

def is_valid_identifier_character(char):
    return char.isalnum() or char in '-+*<>_/?'

MATCHERS = [
    Within("'").escaped_by('\\').matches_to(token.string),
    Within('"').escaped_by('\\').matches_to(token.string),
    Within('/*', '*/').matches_to(token.block_comment),
    Within('//', '\n').matches_to(token.line_comment),
    ExactText('(').matches_to(token.left_paren),
    ExactText(')').matches_to(token.right_paren),
    ExactText('[').matches_to(token.left_square_bracket),
    ExactText(']').matches_to(token.right_square_bracket),
    ExactText('->').matches_to(token.function),
    ExactText('=').matches_to(token.identifier),
    ExactText('|').matches_to(token.pipe),
    ExactText(',').matches_to(token.comma),
    ExactText('.').matches_to(token.dot),
    ExactText(';').matches_to(token.semicolon),
    ExactText('::').matches_to(token.type_denote),
    ExactText(':').matches_to(token.begin_block),
    ExactText(' ').matches_to(token.indentation_unit),
    ExactText('\t').matches_to(token.indentation_unit),
    While(str.isdigit).matches_to(token.integer),
    Compound(
        ExactText('#').is_required_but_ignored(),
        While(is_valid_identifier_character)
    ).matches_to(token.named_comma),
    While(is_valid_identifier_character).matches_to(token.identifier)
]

class Lexer:
    def __init__(self, matchers = MATCHERS):
        self.matchers = matchers

    def tokenize(self, characters):
        while characters:
            for matcher in self.matchers:
                match = matcher.match(characters)

                if match:
                    characters = matcher.remaining_text
                    yield match
                    break

            if not match:
                # So we don't end up in an infinite loop
                raise Exception("No match for '" + characters + "'")
