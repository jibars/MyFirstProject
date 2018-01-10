import unittest
import functions.math as math

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.source_matrix = [[1.0, 1.0, 0.0], [1.0, 0.0, 1.0], [0.0, 1.0, 0.0]]
        self.inverse_matrix = [[1.0, 0.0, -1.0], [0.0, 0.0, 1.0], [-1.0, 1.0, 1.0]]

    def test_matrix_inverse(self):
        self.assertEqual(math.inverse(self.source_matrix), self.inverse_matrix)

    def test_matrix_product(self):
        a = [[2.0, 0.0, 1.0], [3.0, 0.0, 0.0], [5.0, 1.0, 1.0]]
        b = [[1.0, 0.0, 1.0], [1.0, 2.0, 1.0], [1.0, 1.0, 0.0]]
        ab = [[3.0, 1.0, 2.0], [3.0, 0.0, 3.0], [7.0, 3.0, 6.0]]

        self.assertEqual(ab, math.product(a, b))

    def test_determinant_is_zero(self):
        a = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
        self.assertEqual(0.0, math.determinant(a))

    def test_determinant_is_not_zero(self):
        b = [[2.0, 3.0, 3.0, 6.0], [2.0, 3.0, 6.0, 7.0], [4.0, 4.0, 0.0, 3.0], [2.0, 5.0, 2.0, 3.0]]
        self.assertEqual(-116.0, math.determinant(b))
