import unittest
from vector_class import Vector


class TestVector(unittest.TestCase):

    def setUp(self):
        self.vector = Vector()

    def test_sum_with(self):
        self.assertEqual(self.vector.sum_with(self.vector), [14, 16, 18])

    def test_is_equal(self):
        self.assertEqual(self.vector.is_equal(self.vector), True)

    def test_vector_length(self):
        self.assertAlmostEqual(self.vector.vector_length(), 13.93, 1)

    def test_subtract_with(self):
        self.assertEqual(self.vector.subtract_with(self.vector), [0, 0, 0])

    def test_multiply_on_const(self):
        self.assertEqual(self.vector.multiply_on_const(2), [14, 16, 18])

    def test_scalar_multiplication(self):
        self.assertEqual(self.vector.scalar_multiplication(self.vector), 194)

    def test_element(self):
        self.assertEqual(self.vector.element(2), 9)

    def test_vector_string(self):
        self.assertEqual(self.vector.vector_string(), "(7, 8, 9)")


if __name__ == "__main__":
    unittest.main()
