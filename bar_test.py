# Voor pytest
import unittest
# de te testen functie(s)
from bar import order_beer


class MyTestCase(unittest.TestCase):

    # voeg hier je testen toe!
    def test_eq(self):
        self.assertEqual("blabla", "blabla")

    def test_error(self):
        with self.assertRaises(Exception):
            bam = 1 / 0

    def test_non_equality(self):
        self.assertGreater(0, 1)
        
    def test_order_beer_positive_numbers(self):
        self.assertEqual(order_beer(1), 1)
        
    def test_order_beer_negative_numbers(self):
        with self.assertRaises(Exception):
            order_beer(-1)    
        

class MockExample(unittest.TestCase):
    def test_friday(self):
        with unittest.mock.patch('custom_datetime.datetime_.today', return_value=datetime.datetime(2023, 11, 24)):
            self.assertTrue(is_it_friday())

    def test_monday(self):
        with unittest.mock.patch('custom_datetime.datetime_.today', return_value=datetime.datetime(2023, 11, 25)):
            self.assertFalse(is_it_friday())

class CoverageExample(unittest.TestCase):
    def test_hi(self):
        say_hello(1)

if __name__ == '__main__':
    unittest.main()

