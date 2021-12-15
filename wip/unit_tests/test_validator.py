import unittest

from classes.validacija import Validator


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_it_will_reject_username_if_too_long(self):
        # Assume
        username = "InvalidTooLong"

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_it_will_reject_username_if_there_is_space(self):
        # Assume
        username = "Pass word"

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_it_will_reject_username_if_all_lower(self):
        # Assume
        username = "password"

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_it_will_accept_username(self):
        # Assume
        username = "Username"

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertTrue(result)

# if __name__ == '__main__':
#     unittest.main()
