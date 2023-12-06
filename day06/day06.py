#! /usr/bin/env python3

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

ts = lines[0].split(':')[1].split()
ds = lines[1].split(':')[1].split()

t = [int(x) for x in ts]
d = [int(x) for x in ds]

#print(t)
#print(d)

x = {}
n = []
for i in range(0, len(t)):
    x[i] = []
    for a in range(0, t[i]):    
        y = (t[i]-a) * a
        x[i].append(y)
    #print(x)
    n.append([y > d[i] for y in x[i]])
    #print(n)
answer1 = 1
for i in range(0, len(n)):
    answer1 = answer1 * n[i].count(True)
print('Answer 1:', answer1)
