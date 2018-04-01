from abc import ABC
import random

import utils
from Deck import Deck

class Shoe(ABC):
    def __init__(self, *args):
        utils.validate_decks_type(args)
        self.cards = [card for deck in args for card in deck.cards]

    def shuffle(self):
        for index in range(0, len(self.cards)):
            j = random.randint(0, index)
            self.cards[index], self.cards[j] = self.cards[j], self.cards[index]
        return self

    def take_from_top(self, count):
        if count > len(self.cards):
            raise Exception
        
        dealt = self.cards[:count]
        self.cards = self.cards[count:]
        return dealt

    def deal_random(self, count):
        if count > len(self.cards):
            raise Exception
        
        dealt = []
        for _ in list(range(count)):
            card = None
            while card is None:
                index = random.randint(0, len(self.cards))
                card = self.cards(index)
            
            dealt.append(card)
            self.cards = None

        self.cards = [x for x in self.cards if x]

    def _get_card_from_tuple(self, card_tuple):
        for index, card in enumerate(self.cards):
            if card.pip_str == card_tuple[0] and card.suit_str == card_tuple[1]:
                return self.cards.pop(index)
        raise Exception

    def deal_specific(self, *args):
        return [self._get_card_from_tuple(card) for card in args]


class HoldEmShoe(Shoe):
    def __init__(self, *args):
        super().__init__(*args)
    
    def shuffle(self):
        return super().shuffle()

    def take_from_top(self, count):
        return super().take_from_top(count)

    def deal_random(self, count):
        return super().deal_random(count)

    def deal_hand_from_tuples(self, hand_class, card_tuple1, card_tuple2):
        cards = super().deal_specific(card_tuple1, card_tuple2)
        return hand_class(*cards)
        
    def deal_specific(self, *args):
        return super().deal_specific(*args)