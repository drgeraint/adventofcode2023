#! /usr/bin/env python3

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

answer1 = 0
for line in lines:
    card, data = line.split(':')
    winners = set()
    numbers = set()
    success = set()
    lhs, rhs = data.split('|')
    for n in lhs.split():
        winners.add(int(n))
    for n in rhs.split():
        n = int(n)
        numbers.add(n)
        if n in winners:
            success.add(n)
    if len(success) > 0:        
        score = pow(2, len(success)-1)
    else:
        score = 0
    answer1 = answer1 + score
    #print(card, winners, numbers, success, score)
print(answer1)
