import sys
sys.path.append('../')
import unittest

from cardclasses import *
from cardclasses.Card import HoldEmCard, Card
from cardclasses.Deck import PokerDeck
from cardclasses.Hand import HoldEmHand

class TestHoldEmCard(unittest.TestCase):
    def test_good_card(self):
        self.assertEqual(HoldEmCard('2', 'h').to_string(), '2h')

        card = HoldEmCard('-1', 'h', True)
        self.assertEqual(str(card.pip) + str(card.suit), '-10') 

        with self.assertRaises(TypeError):
            HoldEmCard('-1', 'h')

class TestPokerDeck(unittest.TestCase):
    def test_poker_deck(self):
        deck = PokerDeck.fresh_deck(HoldEmCard)
        deck_str = [c.to_string() for c in deck.cards]

        correct_deck = ['2h', '3h', '4h', '5h']

        self.assertListEqual(deck_str[0:4], correct_deck)

class TestHoldEmHand(unittest.TestCase):
    def test_create_hand_from_tuples(self):
        hand = HoldEmHand.create_hand_from_tuples(('4', 's'), ('T', 'h'), HoldEmCard)
        
        self.assertTrue(isinstance(hand, HoldEmHand))
        
        with self.assertRaises(ValueError):
            bad_hand = HoldEmHand.create_hand_from_tuples(('4', 's'), ('T', 'a'))


if __name__ == '__main__':
    unittest.main()
