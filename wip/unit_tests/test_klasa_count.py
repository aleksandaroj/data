from unittest import TestCase
from klasa_count import Count
# from unittest.mock import patch # patch moze da se koristi kao dekorator i kao kontekst menadzer


class Test(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_count(self):
        self.assertEqual(min(Count(1, 7)), 1)
        self.assertEqual(max(Count(1, 7)), 7)
        self.assertEqual(min(Count(1, 2)), 1)
        self.assertEqual(max(Count(1, 2)), 2)
        self.assertEqual(min(Count(0, 2)), 0)
        self.assertEqual(max(Count(0, 2)), 2)
