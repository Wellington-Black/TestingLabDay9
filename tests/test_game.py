import unittest
from src.game import *
from src.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Giuliano", "paper")
        self.player_2 = Player("Wellington", "rock")
        self.player_3 = Player("Hannah", "scissors")

    def test_play_paper_vs_rock_returns_name_of_player_paper(self):
        self.assertEqual(self.player_1.name, play(self.player_1, self.player_2))

    def test_play_rock_vs_paper_returns_name_of_player_paper(self):
        self.assertEqual(self.player_1.name, play(self.player_1, self.player_2))

    def test_play_paper_vs_scissors_returns_name_of_player_scissors(self):
        self.assertEqual(self.player_3.name, play(self.player_1, self.player_3))
    
    def test_play_scissors_vs_paper_returns_name_of_player_scissors(self):
        self.assertEqual(self.player_3.name, play(self.player_1, self.player_3))

    def test_play_paper_vs_paper_returns_name_of_player_paper(self):
        self.assertEqual('Draw', play(self.player_1, self.player_1))