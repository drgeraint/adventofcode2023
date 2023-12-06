#! /usr/bin/env python3

import numpy as np

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

ts = lines[0].split(':')[1].split()
ds = lines[1].split(':')[1].split()
t = [int(x) for x in ts]
d = [int(x) for x in ds]
        
print(t)
print(d)

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


ts = lines[0].split(':')[1].replace(' ','')
ds = lines[1].split(':')[1].replace(' ','')
t = int(ts)
d = int(ds)

#print(t)
#print(d)

# d = (t-a)*a
# d = at - a^2
# a^2 - t.a + d = 0

a1 = (t + np.sqrt(t*t-4*1*d))/2
a2 = (t - np.sqrt(t*t-4*1*d))/2
#print(a1,a2)
answer2 = int(np.floor(a1-a2))

n = 0
for a in range(int(a2)-100, int(a1)+100):
    if (t-a)*a > d:
        n = n+1

print('Answer 2:', n)

