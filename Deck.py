from abc import ABC
import utils

from Card import Card

class Deck(ABC):
    def __init__(self, cards=None):
        utils.validate_cards_type(cards)
        self.cards = cards

    @classmethod
    def fresh_deck(cls):
        pass

class PokerDeck(Deck):
    def __init__(self, cards=None):
        super().__init__(cards)

    @classmethod
    def fresh_deck(cls, card_class):
        cards = []

        for suit in card_class.suits():
            for pip in card_class.pips():
                cards.append(card_class(pip=pip, suit=suit))

        return cls(cards)