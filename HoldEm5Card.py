from Card import HoldEmCard
from Hand import HoldEmHand
from Deck import PokerDeck
from Shoe import HoldEmShoe

if __name__ == '__main__':
    def get_shoe(shoe, card, deck, deck_count=1):
        decks = []
        for _ in list(range(deck_count)):
            decks.append(deck.fresh_deck(card))
        return shoe(*decks)

    shoe = get_shoe(HoldEmShoe, HoldEmCard, PokerDeck).shuffle()

    hands = [shoe.deal_hand_from_tuples(HoldEmHand, cards[0], cards[1]) for cards in \
        [
            [('A', 'h'), ('K', 'h')],
            [(6, 'd'), (6, 'c')],
            [(9, 's'), ('T', 's')]
        ]
    ]

    print([hand.to_string() for hand in hands])

    # classifiers


    # ranks


    # argument parser


    # client/orchestration