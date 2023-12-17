#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

PART = 2

import functools
import re

full_lhs = {}
full_rhs = {}

regexp = {}

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

@functools.lru_cache(maxsize = None)
def check_pattern(row, candidate):
    if row in regexp:
        p = regexp[row]
    else:
        p = '^[.]*'
        for i in range(0, len(full_rhs[row])-1):
            p += '[#?]{%d}[.?]+?' % full_rhs[row][i]
        p += '[#?]{%d}[.?]*$' % full_rhs[row][-1]
        p = re.compile(p)
        regexp[row] = p
    q = p.match(candidate)
    if q is None:
        print('Fail:', row, candidate, full_rhs[row])
        return 0
    else:
        return 1
    
@functools.lru_cache(maxsize = None)
def N(row, lhs, rhs): #, candidate):
    if '#' == lhs[0]:
        return 0
    #candidate += '.'
    return evaluate(row, lhs[1:], rhs) #, candidate)

@functools.lru_cache(maxsize = None)
def Y(row, lhs, rhs): #, candidate):
    if '.' in lhs[0:rhs[0]]:
        return 0
    #candidate += '#'.rjust(rhs[0],'#')
    if 1 == len(rhs):
        if '#' in lhs[rhs[0]:]:
            return 0
        else:
            return 1 #check_pattern(row, candidate)
    else:
        return N(row, lhs[rhs[0]:], rhs[1:]) #, candidate) 
   
@functools.lru_cache(maxsize = None)
def evaluate(row, lhs, rhs): #, candidate=''):
    if len(lhs) < sum(rhs)+len(rhs)-1:
        return 0
    if '.' == lhs[0]:
        return N(row, lhs, rhs) #, candidate)
    elif '#' == lhs[0]:
        return Y(row, lhs, rhs) #, candidate)
    elif '?' == lhs[0]:
        return (N(row, lhs, rhs) + #, candidate) +
                Y(row, lhs, rhs)) #, candidate))    
answer1 = 0
row = 0
for line in lines:
    lhs, rhs = line.split()
    if 2 == PART:
        unfolded_lhs = lhs
        unfolded_rhs = rhs
        for i in range(0,4):
            unfolded_lhs += '?' + lhs
            unfolded_rhs += ',' + rhs
        lhs = unfolded_lhs
        rhs = unfolded_rhs
    rhs = rhs.split(',')
    rhs = [int(x) for x in rhs]
    print('Evaluating:', lhs, rhs)
    full_lhs[row] = lhs
    full_rhs[row] = rhs
    n = evaluate(row, lhs, tuple(rhs)) #, '')
    print(n, lhs, rhs)
    row += 1
    answer1 += n
print('Answer:', answer1)
