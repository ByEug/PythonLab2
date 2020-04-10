import unittest
from ext_sort import merge_sort


class TestExtSort(unittest.TestCase):

    def test_merge_sort(self):
        buffer = [2, 5, 1, 8]
        merge_sort(buffer)
        self.assertEqual(buffer, [1, 2, 5, 8])


if __name__ == "__main__":
    unittest.main()
