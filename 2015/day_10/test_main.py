import unittest
from main import read_input, group, transform

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input.txt"
        s = read_input(filename)

        self.assertEqual(s, "111221")

    def test_group(self):
        s = "111221"
        expected = [(3, "1"), (2, "2"), (1, "1")]

        self.assertEqual(group(s), expected)
    
    def test_transform(self):
        grouped = [(3, "1"), (2, "2"), (1, "1")]
        expected = "312211"

        self.assertEqual(transform(grouped), expected)