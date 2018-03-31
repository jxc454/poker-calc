from abc import ABC
from Card import Card
import utils

class Hand(ABC):
    def __init__(self, pocket=None, community=None):
        utils.validate_cards_type(cards=pocket)
        utils.validate_cards_type(cards=community)
        
        self.pocket = pocket
        self.community = community
        self.rank = -1

    def value(self):
        raise NotImplementedError


class HoldEmHand(Hand):
    def __init__(self, pocket=None, community=None):
        super().__init__(pocket=pocket, community=community)

    def value(self):
        cards = self.pocket + self.community

        high_card = 0

        for card in cards:
            high_card = card.pip if card.pip > high_card else high_card

        