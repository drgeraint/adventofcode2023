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
    cards1 = [hand[i] for i in range(0,5)]
    cards2 = [hand[i] for i in range(0,5)]
    cards1.sort()
    cards2.sort()
    part1 = []
    part2 = []
    njokers = cards2.count('B')
    while('B') in cards2: cards2.remove('B')
    i = 0
    while i < 5:
        x = cards1.count(cards1[i])
        part1.append(x)
        i = i + x   
    i = 0
    while i < 5-njokers:
        x = cards2.count(cards2[i])
        part2.append(x)
        i = i + x   
    part1.sort(reverse=True)
    part2.sort(reverse=True)
    if part2 == [] :
        part2 = [0]
    part2[0] = part2[0] + njokers
    score1 = ''
    score2 = ''
    for i in range(0, len(part1)):
        score1 = score1 + str(part1[i])
    for i in range(0, len(part2)):
        score2 = score2 + str(part2[i])
    score1 = score1.ljust(5, '0')
    score2 = score2.ljust(5, '0')
    #print(hand, score1, score2)
    return (score1, score2)
        
hands = []
for line in lines:
    hand1, bid = line.split()
    hand1 = renumber(hand1)
    score = classify(hand1)
    hand2 = hand1
    hand2 = hand2.replace('B','0')
    hands.append((int(bid), score[0]+hand1, score[1]+hand2))

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
