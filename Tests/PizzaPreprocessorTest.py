import unittest

from Pizza.PizzaPreprocessor import PizzaPreprocessor


class PizzaPreprocessorTest(unittest.TestCase):
    def setUp(self):
        self.processor = PizzaPreprocessor()

    def test_simple_preprocess(self):
        result = self.processor.preprocess_pizza([['X', 'O', 'X']], 1, 3)
        self.assertEqual(result, [[1, 1, 1]])

    # def test_another_preprocess(self):
    #     result = self.processor.preprocess_pizza([['X', 'O', 'X'], ['X', 'O', 'X']], 1, 6)
    #     self.assertEqual(result, [[1, 1, 1], [1, 1, 1]])


    def test_