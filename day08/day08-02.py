#! /usr/bin/env python3

import numpy as np

#with open('test2.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

line0 = lines[0].replace('L','0').replace('R','1')
directions = [int(x) for x in line0]

nodes = {}
p = set()
q = set()
for line in lines[2:]:
    line = line.replace('(', '')
    line = line.replace(')', '')
    line = line.replace(' ', '')
    lhs, rhs = line.split('=')
    r0, r1 = rhs.split(',')
    nodes[lhs] = (r0, r1)
    if 'A' == lhs[2]:
        p.add(lhs)
    if 'Z' == lhs[2]:
        q.add(lhs)

l = len(directions)
c = {}
for x in p:
    c[x] = set()
    y = x
    targets = q.copy()
    n = 0
    while len(targets) > 0:
        i = np.mod(n,l)
        d = directions[i]
        y = nodes[y][d]
        if y[2] == 'Z':
            c[x].add(n)
            if y in targets:
                targets.remove(y)
            elif n > 100000:
                break
        n = n+1

z = []
for x in c:
    d = sorted(c[x])
    period = d[2]-d[1]
    offset = d[0]
    y = [(i-offset)/period for i in d]
    y.sort()
    print(x, offset, period, y)
    z.append(period)

print(sorted(z))
## This doesn't work - don't know why, but different result each time
# print('Answer 2:', np.lcm.reduce(z))

#Answer obtained using Octave:

# lcm(12599, 13771, 15529, 17287, 17873, 21389)
# ans = 8245452805243
