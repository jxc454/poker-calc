from Card import HoldEmCard
from Hand import HoldEmHand
from Deck import PokerDeck
from Shoe import HoldEmShoe

if __name__ == '__main__':
    # shoe
    def get_shoe(shoe, card, deck, deck_count=1):
        decks = []
        for _ in list(range(deck_count)):
            decks.append(deck.fresh_deck(card))
        return shoe(*decks)

    shoe = get_shoe(HoldEmShoe, HoldEmCard, PokerDeck).shuffle()

    print([card.to_string() for card in shoe.take_from_top(2)])

    # classifiers


    # ranks


    # argument parser


    # client/orchestration