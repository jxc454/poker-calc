from collections import defaultdict

from Card import HoldEmCard
import utils

def check_straight_and_flush(hand):
    utils.validate_hand_type
    
    def check_straight(hand):
        pips = list(set([card.pip for card in hand.cards]))

        if len(pips) < 5:
            return False

        # check for ace
        if hand.has_pip('A'):
            pips.append(-1)

        pips.sort(reverse=True)

        for index in range(0, len(pips) - 5):
            if pips[index] - pips[index + 4] == 4:
                return ('e', ''.join([str(pip).zfill(2) for pip in pips[index:index + 5]]))
        
        return False
    
    def check_flush(hand):
        suits = defaultdict(list)
        for card in hand.cards:
            suits[card.suit].append(card.pip)

        flush = []
        for pips in suits.values():
            if len(pips) >= 5:
                pips.sort(reverse=True)
                flush = ('f', ''.join([str(pip).zfill(2) for pip in pips[:5]]))

        return flush if flush else False
        

    straight = check_straight(hand)
    flush = check_flush(hand)

    if straight and flush and straight[1] == flush[1]:
        return 'i' + flush[1]
    elif flush:
        return ''.join(flush)
    elif straight:
        return ''.join(straight)

    return "0"
