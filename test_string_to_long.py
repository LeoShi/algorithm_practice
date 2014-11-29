from unittest import TestCase
from string_to_long import to_long


class StringToLongTest(TestCase):
    def test_invalid_string_should_return_none(self):
        self.assertIsNone(to_long('invalid_string1234'))

    def test_should_return_positive_value_given_sign_is_plus(self):
        string = "+1234567"
        self.assertEqual(1234567, to_long(string))

    def test_should_return_negative_value_given_sign_is_minus(self):
        string = "-1234567"
        self.assertEqual(-1234567, to_long(string))

    def test_should_return_right_number_given_fucking_long_string(self):
        string = "123456789012345678901234567890123456789012345678901234567890"
        self.assertEqual(123456789012345678901234567890123456789012345678901234567890, to_long(string))
