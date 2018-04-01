from Card import Card
from Deck import Deck
from Hand import Hand

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

def validate_callable_type(funcs=None):
    if funcs is not None:
        for func in funcs:
            if not callable(func):
                raise Exception

def validate_hand_type(*args):
    for hand in args:
        if hand is not None:
            if not isinstance(hand, Hand):
                raise Exception