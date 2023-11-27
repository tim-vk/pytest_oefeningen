# Voor pytest
import unittest

# de te testen functie(s)
from bar import order_beer


class MyTestCase(unittest.TestCase):

    # voeg hier je testen toe!
    def test_eq(self):
        self.assertEqual("blabla", "blabla")

    def test_error(self):
        with self.assertRaises(ArithmeticError):
            bam = 1 / 0

    def test_fails(self):
        self.assertGreater(0, 1)


if __name__ == '__main__':
    unittest.main()

