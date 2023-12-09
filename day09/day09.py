#! /usr/bin/env python3

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

def process(elements):
    if any(elements):
        nextline = []
        for i in range(0, len(elements)-1):
            nextline.append(elements[i+1]-elements[i])
        return elements[-1] + process(nextline)
    else:
        return 0

def process2(elements):
    if any(elements):
        nextline = []
        for i in range(0, len(elements)-1):
            nextline.append(elements[i+1]-elements[i])
        return elements[0] - process2(nextline)
    else:
        return 0
    
answer1 = 0
for line in lines:
    elements = line.split()
    elements = [int(x) for x in elements]
    answer1 = answer1 + process(elements)
print('Answer 1:', answer1)

answer2 = 0
for line in lines:
    elements = line.split()
    elements = [int(x) for x in elements]
    answer2 = answer2 + process2(elements)
print('Answer 2:', answer2)

