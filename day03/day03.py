#! /usr/bin/env python3

import re

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

symgrid  = set()

p_number = re.compile(r'\d+')
p_symbol = re.compile(r'[^\d\.]')

row = 0
for line in lines:
    symbols = p_symbol.finditer(line)
    for symbol in symbols:
        symgrid.add((row,symbol.start()))
    n = p_number.finditer(line)
    row = row+1
    
answer1 = 0
row = 0
for line in lines:
    numbers = p_number.finditer(line)
    for number in numbers:
        flag = False
        for i in [row-1, row, row+1]:
            for j in range(number.start()-1, number.end()+1):
                if (i,j) in symgrid:
                    flag = True
        if flag:
            answer1 = answer1 + int(number.group())
    row = row+1
print(answer1)

                    
