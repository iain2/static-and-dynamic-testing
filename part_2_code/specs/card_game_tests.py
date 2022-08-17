from pickle import FALSE
import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Spades", 10)
        self.card_game = CardGame()

    def test_card_is_ace(self):
        e = self.card_game.check_for_ace(self.card1)
        self.assertEqual(FALSE, e)

    def test_check_highest_card(self):
        e = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card1, e)

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        e = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 1", e)
