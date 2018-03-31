from abc import ABC

class Card(ABC):
    def __init__(self, pip=None, suit=None):
        if pip in Card.pips():
            self.pip = pip
        else:
            raise Exception
        
        if suit in Card.suits():
            self.suit = suit
        else:
            raise Exception

    def to_string(self):
        return str(self.pip) + self.suit

    @classmethod
    def suits(cls):
        return ['h', 's', 'd', 'c']

    @classmethod
    def pips(cls):
        return [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']

class HoldEmCard(Card):
    def __init__(self, pip=None, suit=None):
        super().__init__(pip, suit)

    @classmethod
    def suits(cls):
        return super().suits()

    @classmethod
    def pips(cls):
        return super().pips()
    