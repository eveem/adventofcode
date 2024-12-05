import unittest
from main import read_input, escape, encode

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input.txt"
        lines = read_input(filename)

        self.assertEqual(len(lines), 4)
    
    def test_escape_double_quote(self):
        s = '"aaa\\\"aaa"'
        self.assertEqual(escape(s), 9)
    
    def test_escape_backslash(self):
        s = '''"ab\\\\"'''
        self.assertEqual(escape(s), 5)
    
    def test_escape_ascii(self):
        s = '"ab\\x28de\\x27"'
        self.assertEqual(escape(s), 8)

    def test_encode_double_quote_middle(self):
        s = '"aaa\\\"aaa"'
        self.assertEqual(encode(s), 14)
    
    def test_encode_double_quote_edge(self):
        s = '"abc"'
        self.assertEqual(encode(s), 7)
    
    def test_encode_backslash(self):
        s = '"\\x27"'
        self.assertEqual(encode(s), 9)