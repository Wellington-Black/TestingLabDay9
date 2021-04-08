import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Ben", "paper")
    
    def test_player_has_name(self):
        self.assertEqual("Ben", self.player.name)
        
    def test_player_has_gesture(self):
        self.assertEqual("paper", self.player.gesture)