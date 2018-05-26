from cardclasses.Card import Card
from cardclasses.Deck import Deck
from cardclasses.Hand import Hand
from cardclasses.Hand import HoldEmHandFull

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

def compose_hands(hands, community):
    return [HoldEmHandFull(hand, *community.cards) for hand in hands]