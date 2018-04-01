from Card import HoldEmCard
from Hand import HoldEmHand, Community
from Deck import PokerDeck
from Shoe import HoldEmShoe
from Calculator import HoldEmCalculator
from classifiers import check_straight_and_flush

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
            [(2, 's'), (3, 's')]
        ]
    ]   

    print([hand.sort_by_pip().to_string() for hand in hands])

    # community = Community(*shoe.take_from_top(5))
    community = Community(*shoe.deal_specific(('Q', 'h'), ('K', 'h'), ('A', 'h'), (5, 'd'), (7, 'h')))

    print(community.to_string())

    calculator = HoldEmCalculator(hands, community)
    winning_hand = calculator.winner(check_straight_and_flush)

    print(winning_hand.to_string() if winning_hand else "no winner")
    # classifiers
