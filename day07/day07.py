#! /usr/bin/env python3

import re

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

def classify(hand):
    cards = [hand[i] for i in range(0,5)]
    cards.sort()
    parts = []
    i = 0
    while i < 5:
        x = cards.count(cards[i])
        parts.append(x)
        i = i + x   
    parts.sort(reverse=True)
    score = ''
    for i in range(0, len(parts)):
        score = score + str(parts[i])
    score = score.ljust(5, '0')
    score = score + hand
    return score
        
hands = []
for line in lines:
    hand, bid = line.split()
    hand = renumber(hand)
    score = classify(hand)
    hands.append((score, int(bid)))

ranks = sorted(hands, key=lambda x: x[0])
#print(ranks)
score = 0
for i in range(0, len(ranks)):
    score = score + (i+1)*ranks[i][1]

print('Answer 1:', score)
