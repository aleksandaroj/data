from unittest import TestCase

from classes.validacija import username_is_valid


class TestValidator(TestCase):
    def test_username_is_valid(self):
        self.assertTrue(username_is_valid(self, username="Ski4567890"))

    def test_it_will_reject_username_if_too_long(self):
        self.assertFalse(username_is_valid(self, username="Skiiiiiiiiiiiiiiiiiiiiiiiiiii"))

    def test_it_will_reject_username_if_there_is_space(self):
        self.assertFalse(username_is_valid(self, username="Sk i"))

    def test_it_will_reject_username_if_all_lower(self):
        self.assertFalse(username_is_valid(self, username="ski"))
