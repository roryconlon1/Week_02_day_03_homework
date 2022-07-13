import unittest
from src.fish import Fish

class TestFish(unittest.TestCase):

    def setUp(self):
        self.fish = Fish("nemo")
        self.fish_2 = Fish("james")

    def test_get_fish_name(self):
        self.assertEqual("nemo", self.fish.name)
