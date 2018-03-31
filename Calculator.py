from abc import ABC

import utils

class Calculator(ABC):
    def __init__(self, hands, community):
        utils.validate_cards_type(hands + community)

        self.hands = hands
        self.community = community

    def winner(self, *args):
        utils.validate_callable_type

        scores = {}

        for hand in self.hands:
            best_hands = []
            for func in args:
                best_hands.append(func(hand))
                
            best_hand = max(best_hands)
            scores[hand] = best_hand

        max_hand = max(scores.values())

        winners = 0
        winner = None
        for (k, v) in scores:
            if v == max_hand:
                winners += 1
                winner = k
        
        return winner if winners == 1 else None
        
