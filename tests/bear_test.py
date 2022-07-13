from unicodedata import name
import unittest
from src.bear import Bear
from src.fish import Fish


class TestBear(unittest.TestCase):

    def setUp(self):
        self.bear = Bear("Grylls", "Polar")

    def test_get_bear_name(self):
        self.assertEqual("Grylls", self.bear.name)

    def test_get_bear_type(self):
        self.assertEqual("Polar", self.bear.type)

    def test_can_eat_fish(self):
        self.bear.can_eat("nemo")
        self.assertEqual(["nemo"], self.bear.stomach)

    def test_bear_food_count(self):
        self.assertEqual([], self.bear.stomach)
        
    

