#! /usr/bin/env python3

PART = '2'

import re

#with open('test'+PART+'.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

table = {'one':'1', 'two':'2', 'three':'3',
         'four':'4', 'five':'5','six':'6',
         'seven':'7', 'eight':'8', 'nine':'9'}

if '1' == PART:
    number = r'[\d]'
else:
    # ?= capturing group inside lookahead to get overlapping matches
    number = r'(?=([\d]|one|two|three|four|five|six|seven|eight|nine))'
p = re.compile(number)
n = 0
for line in lines:
    print(line)
    matches =  p.finditer(line)
    results = [match.group(1) for match in matches]
    for k,v in table.items():
        results = [v if item == k else item for item in results]
    x = results[0]+results[-1]
    x = int(x)
    n = n + x
print(n)
    
print('Answer:', n)
