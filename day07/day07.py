#! /usr/bin/env python3

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

def renumber(hand):
    hand = hand.replace('A','E')
    hand = hand.replace('K','D')
    hand = hand.replace('Q','C')
    hand = hand.replace('J','B')
    hand = hand.replace('T','A')
    return hand

def classify(hand, part=1):
    cards = [hand[i] for i in range(0,5)]
    cards.sort()
    parts = []
    n = 5
    if 2 == part:
        njokers = cards.count('B')
        while('B') in cards: cards.remove('B')
        n = 5 - njokers
    i = 0
    while i < n:
        x = cards.count(cards[i])
        parts.append(x)
        i = i + x   
    parts.sort(reverse=True)
    if 2 == part:
        if parts == [] : parts = [0]
        parts[0] = parts[0] + njokers
    score = ''
    for i in range(0, len(parts)):
        score = score + str(parts[i])
    score = score.ljust(5, '0')
    return score
        
hands = []
for line in lines:
    hand, bid = line.split()
    hand = renumber(hand)
    score1 = classify(hand, 1)
    score2 = classify(hand, 2)
    hand2 = hand
    hand2 = hand.replace('B','0')
    hands.append((int(bid), score1+hand, score2+hand2))

ranks = sorted(hands, key=lambda x: x[1])
score1 = 0
for i in range(0, len(ranks)):
    score1 = score1 + (i+1)*ranks[i][0]

print('Answer 1:', score1)

ranks = sorted(hands, key=lambda x: x[2])
score2 = 0
for i in range(0, len(ranks)):
    score2 = score2 + (i+1)*ranks[i][0]

print('Answer 2:', score2)
