from unittest import TestCase
from obicna_funkcija import TestiranjeNule


class Test(TestCase):
    def test_oduzimanje(self):
        result = TestiranjeNule.oduzimanje(1, 5)
        self.assertEqual(result, 4)

    def test_oduzimanje_2(self):
        result = TestiranjeNule.oduzimanje(1, 0)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    TestCase.main()
