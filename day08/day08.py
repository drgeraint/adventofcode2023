#! /usr/bin/env python3

import numpy as np

#with open('test2.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

line0 = lines[0].replace('L','0').replace('R','1')
directions = [int(x) for x in line0]

nodes = {}
for line in lines[2:]:
    line = line.replace('(', '')
    line = line.replace(')', '')
    line = line.replace(' ', '')
    lhs, rhs = line.split('=')
    r0, r1 = rhs.split(',')
    nodes[lhs] = (r0, r1)

l = len(directions)
n = 0
p = 'AAA'
while 'ZZZ' != p:
    i = np.mod(n,l)
    d = directions[i]
    p = nodes[p][d]
    n = n + 1
print(n)
