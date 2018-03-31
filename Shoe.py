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
        
class HoldEmShoe(Shoe):
    def __init__(self, *args):
        super().__init__(*args)
    
    def shuffle(self):
        return super().shuffle()

    def take_from_top(self, count):
        return super().take_from_top(count)

    def deal_random(self, count):
        return super().deal_random(count)