from collections import defaultdict

from Card import HoldEmCard
from Hand import HoldEmHand, Community
from Deck import PokerDeck
from Shoe import HoldEmShoe
from Calculator import HoldEmCalculator
from classifiers import check_straight_and_flush, check_pairs

if __name__ == '__main__':
    def get_shoe(shoe, card, deck, deck_count=1):
        decks = []
        for _ in list(range(deck_count)):
            decks.append(deck.fresh_deck(card))
        return shoe(*decks)

    shoe = get_shoe(HoldEmShoe, HoldEmCard, PokerDeck).shuffle()

    hands = [shoe.deal_hand_from_tuples(HoldEmHand, cards[0], cards[1]) for cards in \
        [
            [('T', 'h'), ('J', 'h')],
            [('J', 'd'), (2, 'd')],
            [('K', 'd'), (6, 'd')],
            [('Q', 's'), (7, 'd')],
            [('A', 'd'), (4, 'd')],
        ]
    ]

    hand_scores = defaultdict(int)
    hand_scores['split'] = 0
    for hand in hands:
        hand_scores[hand.to_string()] = 0

    iterations = 2500
    for index in range(0, iterations):
        community = Community(*shoe.deal_random(5))
        calculator = HoldEmCalculator(hands, community, Community)
        winning_hand = calculator.winner(check_straight_and_flush, check_pairs)
        shoe.add_cards(*community.cards)
        
        if winning_hand:
            hand_scores[winning_hand.to_string()] += 1
        else:
            hand_scores['split'] += 1

    for score in hand_scores.items():
        print('{0}: {1}%'.format(score[0], round(100 * score[1] / float(iterations),1)))
