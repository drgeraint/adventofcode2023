#! /usr/bin/env python3

import re

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

sym_set  = set()
gears    = {}

p_number = re.compile(r'\d+')
p_symbol = re.compile(r'[^\d\.]')
p_astrsk = re.compile(r'\*')

row = 0
for line in lines:
    symbols = p_symbol.finditer(line)
    for symbol in symbols:
        sym_set.add((row,symbol.start()))    
    asterisks = p_astrsk.finditer(line)
    for asterisk in asterisks:
        gears[(row,asterisk.start())] = set()
    row = row+1
    
answer1 = 0
row = 0
for line in lines:
    numbers = p_number.finditer(line)
    for number in numbers:
        flag = False
        for i in [row-1, row, row+1]:
            for j in range(number.start()-1, number.end()+1):
                if (i,j) in sym_set:
                    flag = True
                if (i,j) in gears:
                    gears[(i,j)].add(int(number.group()))
        if flag:
            answer1 = answer1 + int(number.group())        
    row = row+1
print('Answer 1:', answer1)

answer2 = 0
for k,v in gears.items():
    if 2 == len(v):
        x = 1
        for i in v:
            x = x*i
        answer2 = answer2 + x
print('Answer 2:', answer2)

                    
