from collections import defaultdict
import argparse

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

    parser = argparse.ArgumentParser(description="get card odds for Texas Hold 'Em hands.")

    # get hands
    parser.add_argument('hands', metavar='PokerHand', type=str, nargs='+', help='enter up to 10 starting hands')

    # get optional community cards
    parser.add_argument('--comm', metavar='community_str', type=str, nargs=1, default='', help='enter up to 5 community cards')

    # read args
    args = parser.parse_args()

    # get shoe
    shoe = get_shoe(HoldEmShoe, HoldEmCard, PokerDeck).shuffle()

    # deal hands
    hands = [shoe.deal_hand_from_tuples(HoldEmHand, (hand[0:1], hand[1:2]), (hand[2:3], hand[3:])) for hand in args.hands]
    
    # deal community
    community_cards_str = [args.comm[0][i:i + 2] for i in range(0, len(args.comm[0]), 2)] if args.comm else []
    community_tuples = [(card[0:1], card[1:2]) for card in community_cards_str]
    community_start = shoe.deal_specific(*community_tuples)

    hand_scores = defaultdict(int)
    hand_scores['split'] = 0

    for hand in hands:
        hand_scores[hand.to_string()] = 0

    community = Community(*(community_start[:] + shoe.deal_random(5 - len(community_start))))

    calculator = HoldEmCalculator(hands, community, Community)

    iterations = 8000
    for index in range(0, iterations):
        winning_hand = calculator.winner(check_straight_and_flush, check_pairs)
        shoe.add_cards(*community.cards[len(community_start):])
        
        if winning_hand:
            hand_scores[winning_hand.to_string()] += 1
        else:
            hand_scores['split'] += 1
        
        community = Community(*(community_start[:] + shoe.deal_random(5 - len(community_start))))
        calculator.community = community

    for score in hand_scores.items():
        print('{0}: {1}%'.format(score[0], round(100 * score[1] / float(iterations), 1)))
