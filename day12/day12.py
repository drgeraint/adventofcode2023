#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

import re

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

def check_pattern(full_lhs, full_rhs, candidate):
    p = '^[.]*'
    for i in range(0, len(full_rhs)-1):
        p += '[#?]{%d}[.?]+?' % full_rhs[i]
    p += '[#?]{%d}[.?]*$' % full_rhs[-1]
    p = re.compile(p)
    q = p.match(candidate)
    r = p.match(full_lhs)
    if q is None:
        print('Fail q:', candidate)
        return 0
    else:
        print(candidate, 'matches')
        return 1
    
def N(lhs, rhs, full_lhs, full_rhs, candidate):
    if '#' == lhs[0]:
        return 0
    candidate += '.'
    return evaluate(lhs[1:], rhs, full_lhs, full_rhs, candidate)

def Y(lhs, rhs, full_lhs, full_rhs, candidate):
    if '.' in lhs[0:rhs[0]]:
        return 0
    candidate += '#'.rjust(rhs[0],'#')
    if 1 == len(rhs):
        if '#' in lhs[rhs[0]:]:
            return 0
        else:
            return check_pattern(full_lhs, full_rhs, candidate)
    else:
        return N(lhs[rhs[0]:], rhs[1:], full_lhs, full_rhs, candidate)
    
def evaluate(lhs, rhs, full_lhs, full_rhs, candidate=''):
    if len(lhs) < sum(rhs)+len(rhs)-1:
        return 0
    if '.' == lhs[0]:
        return N(lhs, rhs, full_lhs, full_rhs, candidate)
    elif '#' == lhs[0]:
        return Y(lhs, rhs, full_lhs, full_rhs, candidate)
    elif '?' == lhs[0]:
        return (N(lhs, rhs, full_lhs, full_rhs, candidate) +
                Y(lhs, rhs, full_lhs, full_rhs, candidate))    
answer1 = 0
for line in lines:
    lhs, rhs = line.split()
    rhs = rhs.split(',')
    rhs = [int(x) for x in rhs]
    print('Evaluating:', lhs, rhs)
    n = evaluate(lhs, rhs, lhs, rhs, '')
    print(n, lhs, rhs) 
    answer1 += n
print('Answer 1:', answer1)
