from abc import ABC

import utils

class Calculator(ABC):
    def __init__(self, hands, community):
        utils.validate_hand_type(*hands)
        utils.validate_hand_type(community)

        self.hands = hands
        self.community = community

    def winner(self, *args):
        utils.validate_callable_type

        scores = {}

        for hand in self.hands:
            best_hands = []
            for func in args:
                best_hands.append(func(hand.add_cards(*self.community.cards)))
                
            best_hand = max(best_hands)
            scores[hand] = best_hand

        max_hand = max(scores.values())

        winners = 0
        winner = None
        for key in scores.keys():
            if scores[key] == max_hand:
                winners += 1
                winner = key

        return winner if winners == 1 else None
        
class HoldEmCalculator(Calculator):
    def __init__(self, hands, community):
        super().__init__(hands, community)

    def winner(self, *args):
        return super().winner(*args)