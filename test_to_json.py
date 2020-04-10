import unittest
from to_json import to_json


class TestToJson(unittest.TestCase):

    def test_to_json_float(self):
        self.assertEqual(to_json(35.2), '35.2')

    def test_to_json_tuple(self):
        self.assertEqual(to_json((1, 2, 3)), '[1, 2, 3]')

    def test_to_json_bool(self):
        self.assertEqual(to_json(True), 'true')

    def test_to_json_dict(self):
        self.assertEqual(to_json({"name": "John", "age": 30}), '{"name": "John", "age": 30}')


if __name__ == "__main__":
    unittest.main()
