#! /usr/bin/env python3

max_red   = 12
max_green = 13
max_blue  = 14

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

answer1  = 0
answer2  = 0
results1 = {}
results2 = {}
for line in lines:
    game, samples = line.split(':')
    game = int(game.split()[1])
    n = {'red':0, 'green':0, 'blue':0}
    for sample in samples.split(';'):
        subsamples = sample.split(',')
        for subsample in subsamples:
            subsample = subsample.lstrip()
            number, colour = subsample.split()
            n[colour] = max(int(number), n[colour])
    print('Game:', game, 'n:', n, n['red']*n['green']*n['blue'])
    results1[game] = ((n['red']   <= max_red) and
                      (n['green'] <= max_green) and
                      (n['blue']  <= max_blue))
    results2[game] = n['red'] * n['green'] * n['blue']
    print('R2:', results2[game])
    if results1[game] is True:
        answer1 = answer1 + game
    answer2 = answer2 + results2[game]
    print('A2:', answer2)
print('Answer 1:', answer1)
print('Answer 2:', answer2)
