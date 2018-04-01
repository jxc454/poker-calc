from abc import ABC

class Card(ABC):
    suit_list = ['h', 's', 'd', 'c']
    pip_list = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']

    def __init__(self, pip=None, suit=None, force=False):
        if pip in Card.pip_list:
            self.pip = Card.pip_list.index(pip)
            self.pip_str = pip
        elif force == True:
            self.pip = pip
            self.pip_str = str(pip)
        else:
            raise Exception
        
        if suit in Card.suits():
            self.suit = Card.suit_list.index(suit)
            self.suit_str = suit
        else:
            raise Exception

    def to_string(self):
        return str(Card.pip_list[self.pip]) + Card.suit_list[self.suit]

    @classmethod
    def suits(cls):
        return cls.suit_list

    @classmethod
    def pips(cls):
        return cls.pip_list

class HoldEmCard(Card):
    def __init__(self, pip=None, suit=None, force=False):
        super().__init__(pip, suit, force=force)

    @classmethod
    def suits(cls):
        return super().suits()

    @classmethod
    def pips(cls):
        return super().pips()
    