import unittest
from src.river import River
from src.fish import Fish

class TestRiver(unittest.TestCase):
    

    def setUp(self):
        self.river = River("white cart", "salmon")
        self.fish = Fish("haddock")
    
    def test_has_name(self):
        self.assertEqual("white cart", self.river.name)
    
    def test_river_has_fish(self):
        self.assertEqual(["salmon"], self.river.fishes)

    def test_amount_fish(self):
        self.assertEqual(1, len(self.river.fishes))

    def test_can_lose_fish(self):
        self.river.add_fish(self.fish)
        self.river.lose_fish(self.fish)
        self.assertEqual(1, len(self.river.fishes))
