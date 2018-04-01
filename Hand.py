from abc import ABC

import utils

class Hand(ABC):
    def __init__(self, *args):
        utils.validate_cards_type(cards=args)
        
        self.pocket = args

    def to_string(self):
        return ''.join([card.to_string() for card in self.pocket])

    @classmethod
    def create_hand_from_tuples(cls, card_class=None, *args):
        return cls([card_class(*card_tuple) for card_tuple in args])


class HoldEmHand(Hand):
    def __init__(self, card1, card2):
        super().__init__(card1, card2)
    
    def to_string(self):
        return super().to_string()

    @classmethod
    def create_hand_from_tuples(cls, card1, card2, card_class=None):
        holdem_card1 = card_class(*card1)
        holdem_card2 = card_class(*card2)
        return cls(holdem_card1, holdem_card2)