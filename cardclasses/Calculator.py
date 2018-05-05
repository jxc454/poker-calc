from abc import ABC

import cardclasses.utils as utils

class Calculator(ABC):
    def __init__(self, hands):
        self._hands = None
        self.hands = hands

    def winner(self, *args):
        utils.validate_callable_type

        scores = {}

        for hand in self._hands:
            best_hands = []
            for func in args:
                best_hands.append(func(hand))
                
            best_hand = max(best_hands)
            scores[hand.pocket.to_string()] = best_hand

        max_hand = max(scores.values())

        winners = 0
        winner = None

        for key in scores.keys():
            if scores[key] == max_hand:
                winners += 1
                winner = key

        return winner if winners == 1 else None
    
    @property
    def hands(self):
        return self._hands

    @hands.setter
    def hands(self, hands):
        utils.validate_hand_type(*hands)
        self._hands = hands

class HoldEmCalculator(Calculator):
    def __init__(self, hands):
        super().__init__(hands)

    def winner(self, *args):
        return super().winner(*args)