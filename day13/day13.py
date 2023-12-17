#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

puzzles = {}

blk = 0
row = 0
puzzles[0] = {'rows': {}}
for line in lines:
    if '' == line:
        blk += 1
        row  = 0
        puzzles[blk] = {'rows': {}}
    else:
        puzzles[blk]['rows'][row] = line
        row += 1

           
for blk in puzzles:
    ncol = len(puzzles[blk]['rows'][0])
    puzzles[blk]['cols'] = {}
    for col in range(0, ncol):
        puzzles[blk]['cols'][col] = ''
        for row in puzzles[blk]['rows']:
           c = puzzles[blk]['rows'][row][col]
           puzzles[blk]['cols'][col] += c

nrow = len(puzzles[0]['cols'][0])

repeated_cols = {}
repeated_rows = {}

for blk in puzzles:
    ncol = len(puzzles[blk]['rows'][0])
    nrow = len(puzzles[blk]['cols'][0])
    repeated_cols[blk] = set()
    repeated_rows[blk] = set()
    for col in range(0,ncol-1):
        if puzzles[blk]['cols'][col] == puzzles[blk]['cols'][col+1]:
            reflects = True
            for i in range(0,col+1):
                nl = col-i
                nr = col+i+1
                if nr not in puzzles[blk]['cols']:
                    pass
                else:
                    if puzzles[blk]['cols'][nl] != puzzles[blk]['cols'][nr]:
                        reflects = False
            if reflects:
                repeated_cols[blk].add(col)
    for row in range(0,nrow-1):
        if puzzles[blk]['rows'][row] == puzzles[blk]['rows'][row+1]:
            reflects = True
            for i in range(0, row+1):
                nu = row-i
                nd = row+i+1
                if nd not in puzzles[blk]['rows']:
                    pass
                else:
                    if puzzles[blk]['rows'][nu] != puzzles[blk]['rows'][nd]:
                        reflects = False
            if reflects:
                repeated_rows[blk].add(row)

answer1 = 0
for blk in puzzles:
    if len(repeated_cols[blk]) > 0:
        for col in repeated_cols[blk]:            
            answer1 += col+1
    if len(repeated_rows[blk]) > 0:
        for row in repeated_rows[blk]:            
            answer1 += 100*(row+1)
print(answer1)
      
