import unittest
from main import read_input, extract, not_op, and_op, or_op, lshift_op, rshift_op

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input.txt"
        lines = read_input(filename)

        self.assertEqual(len(lines), 8)
    
    def test_assign_operation(self):
        lines = ["123 -> ab"]
        self.assertEqual(extract(lines), {"ab": "0000000001111011"})
    
    def test_not_operation(self):
        lines = ["123 -> x", "NOT x -> h"]
        self.assertEqual(extract(lines), {"x": "0000000001111011", "h": "1111111110000100"})
    
    def test_not_op_function(self):
        src = "0000000001111011"
        self.assertEqual(not_op(src), "1111111110000100")
    
    def test_and_op_function(self):
        x = "0000000001111011"
        y = "0000000001000110"
        self.assertEqual(and_op(x, y), "0000000001000010")
    
    def test_or_op_function(self):
        x = "0000000001111011"
        y = "0000000001000110"
        self.assertEqual(or_op(x, y), "0000000001111111")
    
    def test_lshift_op_function(self):
        s = "0000000001111011"
        self.assertEqual(lshift_op(s, 2), "0000000111101100")
        
    def test_rshift_op_function(self):
        s = "0000000001111011"
        self.assertEqual(rshift_op(s, 2), "0000000000011110")
    
    def test_or_opreation(self):
        lines = ["123 -> x", "456 -> y", "x AND y -> d"]
        self.assertEqual(extract(lines), {
            "x": "0000000001111011", 
            "y": "0000000111001000",
            "d": "0000000001001000"
        })
    
    def test_lshift_operation(self):
        lines = ["123 -> x", "x LSHIFT 2 -> f"]
        self.assertEqual(extract(lines), {
            "x": "0000000001111011", 
            "f": "0000000111101100"
        })
    
    def test_rshift_operation(self):
        lines = ["123 -> x", "x RSHIFT 2 -> g"]
        self.assertEqual(extract(lines), {
            "x": "0000000001111011", 
            "g": "0000000000011110"
        })