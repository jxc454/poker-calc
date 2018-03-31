"""poker calculator methods"""
import sys
from collections import OrderedDict
import argparse
from functools import reduce
import math

def new_deck():
    """ new 52 card deck"""
    deck = []
    for suit in ('h', 's', 'd', 'c'):
        for pip in ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'):
            deck.append(pip + suit)
    return deck

def validate_hand(cards, deck):
    """could this hand be made from this deck, return new deck"""

    # if length of the string is not even cards invalid
    if len(cards) % 2 != 0:
        return False

    # if length of cards > length of deck*2 then too many cards
    if len(cards) / 2 > len(deck):
        return False

    # split hand into cards, check each card
    for card in [cards[i:i+2] for i, x in enumerate(cards) if i % 2 == 0]:
        if card in deck:
            deck.remove(card)
        else:
            return False
    return deck

def deal_community(deck, cardCount):
    """choose cards randomly from deck"""
    from random import randint

    deckCopy = deck[:]
    dealt = []

    for i in range(cardCount):
        val = randint(0, len(deckCopy)-1)
        dealt.append(deckCopy[val])
        del deckCopy[val]
    return dealt


def check_straight(hand):
    """is there a straight in this hand"""

    # sort
    handOrdered = list(OrderedDict.fromkeys(sorted(hand)))

    # if there is an ace then add a 1
    if 14 in handOrdered:
        handOrdered.insert(0, 1)

    # if unique cards count is less than 5 then exit
    if len(handOrdered) < 5:
        return False

    for i in [x for x in range(len(handOrdered)-3, 1, -1)]:
        if handOrdered[i] + 1 == handOrdered[i+1]:
            if handOrdered[i] + 2 == handOrdered[i+2]:
                if handOrdered[i] - 1 == handOrdered[i-1]:
                    if handOrdered[i] - 2 == handOrdered[i-2]:
                        return 'e' + str(handOrdered[i+2]).zfill(2)
                    else: continue
                else: continue
            else: continue
        else: continue

    # return straight
    return False


def check_flush(hand):
    """is there a flush in this hand"""
    suit = ''
    switch = {'A': '14', 'T': '10', 'J': '11', 'Q': '12', 'K': '13', '2':'02', '3':'03', '4':'04', '5':'05', '6':'06', '7':'07', '8':'08', '9':'09'}
    kickers = []

    suits = {
        'h': 0,
        's': 0,
        'd': 0,
        'c': 0
    }

    for c in hand:
        pip = switch.get(c[0:1])
        suit = c[1:2]

        suits[suit] += 1

    for key in suits:
        if suits[key] >= 5:

            # we have a flush, so get pips for the flushed suit
            for c in hand:
                if c[1:2] == key:
                    kickers.append(switch.get(c[0:1]))

            return 'f' + ''.join(sorted(kickers, reverse=True))

    return False


def check_pairs(hand):
    """ is there a pairs hand (pair, two pair, trips, fullhouse, quads) """
    pairs = {'2': [], '3': [], '4': []}
    pips = set(hand)
    twoPair = []

    if len(pips) == 7:
        # no pairs
        return 'a' + ''.join([str(x).zfill(2) for x in sorted(pips, reverse=True)[0:5]]) 

    # get pairs, trips, quads
    for pip in pips:
        count = hand.count(pip)
        if count > 1:
            pairs[str(count)].append(pip)

    if len(pips) == 6:
        # 1 pair
        return 'b' + str(pairs['2'][0]).zfill(2) + ''.join([str(y).zfill(2) for y in sorted([x for x in pips if x != pairs['2'][0]], reverse=True)[0:3]])

    if len(pairs['4']) != 0:
        # 4 of a kind
        return 'h' + str(pairs['4'][0]).zfill(2) + str(max([x for x in pips if x != pairs['4'][0]])).zfill(2)

    if len(pairs['3']) == 0:
        # 2 pair
        twoPair = sorted(pairs['2'], reverse=True)[0:2]
        return 'c' + ''.join([str(x).zfill(2) for x in twoPair]) + str(max([x for x in pips if x not in twoPair])).zfill(2)

    if len(pairs['3']) == 1 and len(pairs['2']) == 0:
        # 3 of a kind        
        return 'd' + str(pairs['3'][0]).zfill(2) + ''.join([str(y).zfill(2) for y in sorted([x for x in pips if x != pairs['3'][0]], reverse=True)[0:2]])


    # fullhouse
    if len(pairs['2']) == 1:
        return 'g' + str(pairs['3'][0]).zfill(2) + str(pairs['2'][0]).zfill(2)

    if len(pairs['2']) == 0:
        return 'g' + ''.join([str(x).zfill(2) for x in sorted(pairs['3'], reverse=True)])

    # len(pairs['2']) must equal 2
    return 'g' + ''.join([str(x).zfill(2) for x in sorted(pairs['2'], reverse=True)])

def check_straight_flush(hand):
    suit = ''
    flushCards = ''
    handNumeric = []

    suits = {
        'h': 0,
        's': 0,
        'd': 0,
        'c': 0
    }

    # replace strings in hand with numbers for sorting
    switch = {'A': 14, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

    for c in hand:
        pip = switch.get(c[0:1])
        suit = c[1:2]

        suits[suit] += 1

    for key in suits:
        if suits[key] >= 5:
            # remove cards without this suit
            flushCards = [x for x in hand if x[1:2] == key]
            for card in flushCards:
                handNumeric.append(switch.get(card[0:1], card[0:1]))
            return check_straight(handNumeric)


def get_hand_value(handCheck):
    flush = False
    straight = False
    straightflush = False
    handNumeric = []

    # replace strings in hand with numbers for sorting
    switch = {'A': 14, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    for card in handCheck:
        handNumeric.append(switch.get(card[0:1], card[0:1]))

    straight = check_straight(handNumeric)
    flush = check_flush(handCheck)

    if straight != False and flush != False:
        straightflush = check_straight_flush(handCheck)

    if straightflush != False:
        handValue = 'i' + straightflush[1:3]
    elif flush:
        handValue = flush
    elif straight:
        handValue = straight
    else:
        handValue = check_pairs(handNumeric)

    return handValue


parser = argparse.ArgumentParser(description='calculate odds')

# get hands
parser.add_argument('hands', metavar='PokerHand', type=str, nargs='+', 
                    help='enter up to 10 starting hands')

# get optional community cards
parser.add_argument('--comm', metavar='community', type=str, nargs=1, default='',
                    help='enter up to 5 community cards')

args = parser.parse_args()

communityStart = args.comm[:] or []
community = []
Hands = args.hands[:]
deck = new_deck()
results = {}
wins = {'split': 0}
handValues = set()
bestHand = ''
winners = []
iterations = 10000

# Hands = ['AhAc','5c9c']
# communityStart = ['2c9h']

if len(communityStart) > 0:
    if len(communityStart[0]) > 10:
        print('too many community cards!  Choose 5 at most.')
        sys.exit()

    deck = validate_hand(communityStart[0], deck)
    if deck == False:
        print('problem with cards passed in, cannot use those hands')
        sys.exit()

    communityStart = [communityStart[0][i:i+2] for i, x in enumerate(communityStart[0]) if i % 2 == 0]

for h in Hands:
    deck = validate_hand(h, deck)
    if deck is False:
        print('problem with cards passed in, cannot use those hands')
        sys.exit()
    else:
        wins[h] = 0

# check remaining permutations
if len(communityStart) >= 4 and reduce((lambda x,y: x * y), [x for x in range(len(deck), len(deck) - (5 - len(communityStart)), -1)]) / math.factorial(5 - len(communityStart)) <= 10000:
    pass

for d in range(iterations):
    deck = deck[:]
    community = communityStart + deal_community(deck, 5 - len(communityStart))
    results = {}
    winners = []
    handValues.clear()

    for hand in Hands:
        results[hand] = get_hand_value([hand[0:2], hand[2:4]] + community)
        handValues.add(results[hand])

    bestHand = max(handValues)

    for key in results:
        if results[key] == bestHand:
            winners.append(key)

    if len(winners) == 1:
        wins[winners[0]] += 1
    else:
        wins['split'] += 1

print('\n')
print( [x + ': ' + str(round(wins[x]/iterations*100,1)) + '%' for x in wins])
print('\n')