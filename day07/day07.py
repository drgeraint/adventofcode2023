#! /usr/bin/env python3

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

cardmap = {'A':'E', 'K':'D', 'Q':'C', 'J':'B', 'T':'A'}

def classify(hand, part=1):
    cards = [hand[i] for i in range(0,5)]
    cards.sort()
    groups = []
    if 2 == part:
        njokers = cards.count('B')
        while('B') in cards: cards.remove('B')
    i = 0
    while i < len(cards):
        x = cards.count(cards[i])
        groups.append(x)
        i = i + x   
    groups.sort(reverse=True)
    if 2 == part:
        if [] == groups : groups = [0]
        groups[0] = groups[0] + njokers
    score = ''
    for i in range(0, len(groups)):
        score = score + str(groups[i])
    score = score.ljust(5, '0')
    return score
        
hands = []
for line in lines:
    hand, bid = line.split()
    for card in cardmap:
        hand = hand.replace(card, cardmap[card])
    score1 = classify(hand, 1)
    score2 = classify(hand, 2)
    hands.append((int(bid),
                  score1+hand,
                  score2+hand.replace('B','0')))
for part in (1,2):
    ranks = sorted(hands, key=lambda x: x[part])
    score = 0
    for i in range(0, len(ranks)):
        score = score + (i+1)*ranks[i][0]
    print('Answer', part, ':', score)

