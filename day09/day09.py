#! /usr/bin/env python3

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

def process(elements, part=1):
    if any(elements):
        nextline = []
        for i in range(0, len(elements)-1):
            nextline.append(elements[i+1]-elements[i])
        if 1 == part:
            extrapolation = elements[-1] + process(nextline, 1)
        elif 2 == part:
            extrapolation = elements[ 0] - process(nextline, 2)
    else:
        extrapolation = 0
    return extrapolation

answer1 = 0
answer2 = 0
for line in lines:
    elements = line.split()
    elements = [int(x) for x in elements]
    answer1 = answer1 + process(elements, 1)
    answer2 = answer2 + process(elements, 2)
print('Answer 1:', answer1)
print('Answer 2:', answer2)

