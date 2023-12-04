#! /usr/bin/env python3

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

cards = {}
answer1 = 0
for line in lines:
    card, data = line.split(':')
    card = int(card.split()[1])
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
        score1 = pow(2, len(success)-1)
        score2 = len(success)
    else:
        score1 = 0
        score2 = 0
    answer1 = answer1 + score1
    cards[card] = {'winners':winners, 'numbers':numbers, 'success':success,
                   'score1':score1, 'score2':score2}
    #print(card, winners, numbers, success, score1)
print('Answer 1:', answer1)

cardlist = [x for x in range(1, len(cards)+1)]

def getcard(cardnum):
    n = cards[cardnum]['score2']
    if n > 0:
        for i in range(cardnum+1, cardnum+n+1):
            cardlist.append(i)

#print(cardlist)
for card in cardlist:
    getcard(card)
#print(cardlist)
print('Answer 2:', len(cardlist))
