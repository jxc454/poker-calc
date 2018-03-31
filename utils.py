from Card import Card
from Deck import Deck

def validate_cards_type(cards=None):
    if cards is not None:
        for card in cards:
            if not isinstance(card, Card):
                raise Exception

def validate_decks_type(decks=None):
    if decks is not None:
        for deck in decks:
            if not isinstance(deck, Deck):
                raise Exception