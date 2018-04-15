from abc import ABC

from cardclasses.Card import Card

class Hand(ABC):
    def __init__(self, *args):
        self.cards = [*args]

    def to_string(self):
        return ''.join([card.to_string() for card in self.cards])

    @classmethod
    def create_hand_from_tuples(cls, card_class=None, *args):
        return cls([card_class(*card_tuple) for card_tuple in args])

    def sort_by_pip(self):
        self.cards.sort(key=lambda x: x.pip)
        return self

    def sort_by_suit(self):
        self.cards.sort(key=lambda x: x.suit)
        return self

    def add_cards(self, *args):
        self.cards += args
        return self

    def add_card_from_tuple(self, card_class, card_tuple, force=False):
        self.cards.append(card_class(card_tuple[0], card_tuple[1], force=force))
        return self

    def has_pip(self, pip):
        for card in self.cards:
            if card.pip_str == pip:
                return True
        return False

    def has_suit(self, suit):
        for card in self.cards:
            if card.suit_str == suit:
                return True
        return False

    def remove_card(self, card):
        if isinstance(card, Card):
            for index, card_in_hand in enumerate(self.cards):
                if card_in_hand == card:
                    del self.cards[index]
                    return self
        elif isinstance(card, tuple):
            for index, card_in_hand in enumerate(self.cards):
                if (card_in_hand.pip, card_in_hand.suit) == card:
                    del self.cards[index]
                    return self
        else:
            raise ValueError
        


class HoldEmHand(Hand):
    def __init__(self, card1, card2):
        super().__init__(card1, card2)
        self.pocket = (card1, card2)
    
    def to_string(self):
        return ''.join([card.to_string() for card in self.pocket])

    @classmethod
    def create_hand_from_tuples(cls, card1, card2, card_class=None):
        if (card_class is None):
            raise ValueError
            
        holdem_card1 = card_class(*card1)
        holdem_card2 = card_class(*card2)
        return cls(holdem_card1, holdem_card2)

class Community(Hand):
    def __init__(self, *args):
        super().__init__(*args)

    def to_string(self):
        return super().to_string()