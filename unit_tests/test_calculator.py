import sys
sys.path.append('../')
import unittest

from cardclasses import *
from cardclasses.Card import HoldEmCard, Card
from cardclasses.Deck import PokerDeck
from cardclasses.Hand import HoldEmHand, Community
from cardclasses.Calculator import HoldEmCalculator
import classifiers

class TestHoldEmCalculator(unittest.TestCase):
    def test_2pair_kicker(self):
        hand1 = HoldEmHand.create_hand_from_tuples(
            ('4', 'h'),
            ('4', 'd'),
            HoldEmCard
        )
        hand2 = HoldEmHand.create_hand_from_tuples(
            ('5', 's'),
            ('5', 'c'),
            HoldEmCard
        )
        community = Community(
            HoldEmCard('8', 'h'),
            HoldEmCard('8', 'd'),
            HoldEmCard('6', 'h'),
            HoldEmCard('6', 'd'),
            HoldEmCard('A', 's')
        )

        calc = HoldEmCalculator(hands=[hand1, hand2], community=community, hand_class=Community)

        self.assertIsNone(calc.winner(classifiers.check_pairs))

    def test_4K_split(self):
        hand1 = HoldEmHand.create_hand_from_tuples(
            ('A', 'h'),
            ('Q', 'd'),
            HoldEmCard
        )
        hand2 = HoldEmHand.create_hand_from_tuples(
            ('A', 's'),
            ('Q', 'c'),
            HoldEmCard
        )
        hand3 = HoldEmHand.create_hand_from_tuples(
            ('4', 's'),
            ('4', 'c'),
            HoldEmCard
        )
        community = Community(
            HoldEmCard('A', 'c'),
            HoldEmCard('A', 'd'),
            HoldEmCard('Q', 's'),
            HoldEmCard('4', 'd'),
            HoldEmCard('4', 'h')
        )

        calc = HoldEmCalculator(hands=[hand1, hand2, hand3], community=community, hand_class=Community)
        self.assertEqual(calc.winner(classifiers.check_pairs), hand3)

    def test_FH_split(self):
        hand1 = HoldEmHand.create_hand_from_tuples(
            ('A', 'h'),
            ('Q', 'd'),
            HoldEmCard
        )
        hand2 = HoldEmHand.create_hand_from_tuples(
            ('A', 's'),
            ('Q', 'c'),
            HoldEmCard
        )
        hand3 = HoldEmHand.create_hand_from_tuples(
            ('4', 's'),
            ('4', 'c'),
            HoldEmCard
        )
        community = Community(
            HoldEmCard('A', 'c'),
            HoldEmCard('A', 'd'),
            HoldEmCard('Q', 's'),
            HoldEmCard('4', 'd'),
            HoldEmCard('2', 'h')
        )

        calc = HoldEmCalculator(hands=[hand1, hand2, hand3], community=community, hand_class=Community)
        self.assertIsNone(calc.winner(classifiers.check_pairs))

if __name__ == '__main__':
    unittest.main()
