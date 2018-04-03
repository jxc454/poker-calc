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
            [(3, 'c'), (4, 's')],
            [('Q', 'h'), (9, 'c')],
            [(8, 'h'), (8, 'c')],
            [(3, 'd'), (4, 'c')],
            [(4, 'd'), (8, 'd')]
        ]
    ]

    hand_scores = defaultdict(int)
    hand_scores['split'] = 0
    for hand in hands:
        hand_scores[hand.to_string()] = 0

    community = Community(*shoe.deal_random(5))
    calculator = HoldEmCalculator(hands, community, Community)

    iterations = 8000
    for index in range(0, iterations):
        winning_hand = calculator.winner(check_straight_and_flush, check_pairs)
        shoe.add_cards(*community.cards)
        
        if winning_hand:
            hand_scores[winning_hand.to_string()] += 1
        else:
            hand_scores['split'] += 1
        
        community = Community(*shoe.deal_random(5))
        calculator.community = community

    for score in hand_scores.items():
        print('{0}: {1}%'.format(score[0], round(100 * score[1] / float(iterations), 1)))
