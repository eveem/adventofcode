import unittest
from main import read_input, find_routes

class TestMain(unittest.TestCase):
    def test_read_small_input(self):
        filename = "small_input.txt"
        adj_list = read_input(filename)

        self.assertEqual(adj_list, {
            "London": [["Dublin", 464], ["Belfast", 518]],
            "Dublin": [["London", 464], ["Belfast", 141]],
            "Belfast": [["London", 518], ["Dublin", 141]]
        })
    
    def test_find_route(self):
        adj_list = {
            "London": [["Dublin", 464], ["Belfast", 518]],
            "Dublin": [["London", 464], ["Belfast", 141]],
            "Belfast": [["London", 518], ["Dublin", 141]]
        }

        self.assertEqual(find_routes("London", adj_list), [
            ["London", "Dublin", "Belfast", 605],
            ["London", "Belfast", "Dublin", 659]
        ])