#!/usr/bin/python3

import unittest
import matcher
import mmi_token

import uuid

def anything():
    pass

class MockToken(object):
    def __init__(self, value):
        self.raw_value = value

class MockPassingMatcher(object):
    def __init__(self, raw_value = 'some parsed value'):
        self.raw_value = raw_value
        self.remaining_text = str(uuid.uuid1())

    def match(self, text):
        self.was_matched_against = text
        return MockToken(self.raw_value)

class MockFailingMatcher(object):
    def match(self, _):
        return None

class CompoundSpecs(unittest.TestCase):
    def example_compound_matcher(self, *matchers):
        return matcher.Compound(*matchers).matches_to(MockToken)

    def test_when_two_matchers_succeed_the_compund_succeeds(self):
        self.assertTrue(
            self.example_compound_matcher(
                MockPassingMatcher(),
                MockPassingMatcher()).match(anything()))

    def test_when_first_fails_the_compound_fails(self):
        self.assertEqual(
            None,
            self.example_compound_matcher(
                MockFailingMatcher(),
                MockPassingMatcher()).match(anything()))

    def test_when_second_fails_the_compound_fails(self):
        self.assertEqual(
            None,
            self.example_compound_matcher(
                MockPassingMatcher(),
                MockFailingMatcher()).match(anything()))

    def test_when_both_succeed_their_sum_text_is_returned(self):
        matcher_1 = MockPassingMatcher('foo')
        matcher_2 = MockPassingMatcher('bar')

        result = self.example_compound_matcher(matcher_1, matcher_2).match('...')

        self.assertEqual('foobar', result.raw_value)

    def test_when_first_succeeds_second_is_asked_to_match_its_remaining_text(self):
        matcher_1 = MockPassingMatcher()
        matcher_2 = MockPassingMatcher()

        self.example_compound_matcher(matcher_1, matcher_2).match('...')

        self.assertEqual(
            matcher_1.remaining_text,
            matcher_2.was_matched_against)

    def test_when_both_succeed_seconds_remaining_text_is_preserved(self):
        matcher_1 = MockPassingMatcher()
        matcher_2 = MockPassingMatcher()
        compound_matcher = self.example_compound_matcher(matcher_1, matcher_2)

        compound_matcher.match('...')

        self.assertEqual(
            matcher_2.remaining_text,
            compound_matcher.remaining_text)

    def test_a_whole_bunch_of_successes_are_a_compound_success(self):
        self.assertTrue(
            self.example_compound_matcher(
                MockPassingMatcher(),
                MockPassingMatcher(),
                MockPassingMatcher(),
                MockPassingMatcher()))

class ExactTextSpecs(unittest.TestCase):
    def example_exact_literal_matcher(self):
        return matcher.ExactText('->').matches_to(MockToken)

    def test_matches(self):
        self.assertTrue(self.example_exact_literal_matcher().match('->'))

    def test_no_match_if_first_is_different(self):
        self.assertFalse(self.example_exact_literal_matcher().match('_>'))

    def test_match_even_if_later_text_is_there(self):
        self.assertTrue(self.example_exact_literal_matcher().match('->later text'))

    def test_match_calculates_correct_remaining_text(self):
        matcher = self.example_exact_literal_matcher()
        matcher.match('->later text')
        self.assertEqual('later text', matcher.remaining_text)

class WhileSpecs(unittest.TestCase):
    def example_while_matcher(self):
        return matcher.While(lambda c: c not in ' \t\n').matches_to(MockToken)

    def test_matches_but_not_as_the_first_character(self):
        self.assertEqual(
            None,
            self.example_while_matcher().match(' foobar'))

    def test_matches(self):
        self.assertEqual(
            'foobar',
            self.example_while_matcher().match('foobar and stuff').raw_value)

    def test_matches_and_ends_string(self):
        self.assertEqual(
            'foobar',
            self.example_while_matcher().match('foobar').raw_value)

    def test_matches_has_correct_remaining_value(self):
        matcher = self.example_while_matcher()
        matcher.match("foobar and stuff")
        self.assertEqual(
            " and stuff",
            matcher.remaining_text)

class WithinSpecs(unittest.TestCase):
    def example_string_matcher(self):
        return matcher.Within("'").escaped_by('\\').matches_to(mmi_token.string)

    def test_does_not_match_the_given_value(self):
        self.assertEqual(
            None,
            self.example_string_matcher().match('no quotes here'))

    def test_matches_but_not_as_the_first_character(self):
        self.assertEqual(
            None,
            self.example_string_matcher().match("there's a late quote here"))

    def test_matches(self):
        self.assertEqual(
            'foobar',
            self.example_string_matcher().match("'foobar' and stuff").raw_value)

    def test_has_different_later_quote(self):
        self.assertEqual(
            None,
            self.example_string_matcher().match("'foobar\" and stuff"))

    def test_has_escaped_quote(self):
        self.assertEqual(
            "foo's bar",
            self.example_string_matcher().match("'foo\\'s bar' and stuff").raw_value)

    def test_matches_and_has_remaining_text(self):
        matcher = self.example_string_matcher()
        matcher.match("'foo\\'s bar and fig\\'s foo' and stuff")
        self.assertEqual(
            " and stuff",
            matcher.remaining_text)

    def example_comment_matcher(self):
        return matcher.Within('/*', '*/').matches_to(mmi_token.block_comment)

    def test_no_match_for_complex_delims_where_string_doesnt_start_with_exact_delim(self):
        self.assertEqual(
            None,
            self.example_comment_matcher().match('/- comment */'))

    def test_match_for_complex_delims(self):
        self.assertTrue(self.example_comment_matcher().match('/**/'))

    def test_match_for_complex_delims_value(self):
        self.assertEqual(
            ' comment ',
            self.example_comment_matcher().match('/* comment */').raw_value)

    def test_match_for_complex_delims_remaining_text(self):
        matcher = self.example_comment_matcher()
        matcher.match('/* comment */this text remains')
        self.assertEqual('this text remains', matcher.remaining_text)

    def test_matcher_gets_reset_after_complex_match(self):
        matcher = self.example_comment_matcher()
        self.assertEqual(
            ' first comment ',
            matcher.match('/* first comment */').raw_value)
        self.assertEqual(
            ' second comment ',
            matcher.match('/* second comment */').raw_value)

if __name__ == '__main__':
    unittest.main()
