#! /usr/bin/env python3

import sys
sys.setrecursionlimit(100000)

filename = 'input.txt'

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

nrow = len(lines)
ncol = len(lines[0])
grid = {}
row = 0
for line in lines:
    col = 0
    for c in line:
        grid[(row,col)] = c
        if line[col] == 'S':
            start = (row,col)
        col = col + 1
    row = row + 1

def terminate(path):
    n = path[2]
    exit()

paths = {}

new_direction = {
    'N' : {
        '|' : 'N',
        '7' : 'W',
        'F' : 'E' },
    'E' : {
        '-' : 'E',
        '7' : 'S',
        'J' : 'N' },
    'S' : {
        '|' : 'S',
        'J' : 'W',
        'L' : 'E' },
    'W' : {
        '-' : 'W',
        'L' : 'N',
        'F' : 'S' }}

class path:
    def __init__(self, xy, d):
        self.row = xy[0]
        self.col = xy[1]
        self.d = d
        self.n = 0
        self.id = len(paths)
        self.loop = [(row,col)]
        paths[self.id] = self
        
    def limit_error(self):
        if ((self.d == 'N' and self.row == 0) or
            (self.d == 'E' and self.col == ncol-1) or 
            (self.d == 'S' and self.row == nrow-1) or
            (self.d == 'W' and self.col == 0)):
            limit_error = True
            #print('Limit error in path %d' % self.id)
        else:
            limit_error = False
        return limit_error            

    def terminate(self):
        # print('Terminating path %d at (%d,%d) [%c]' %
        #      (self.id, self.col, self.row, grid[(self.row,self.col)]))
        paths.pop(self.id)
        del self
        
    def go(self):
        if self.limit_error():
            self.terminate()
            return
        if self.d == 'N':
            self.row = self.row - 1
        elif self.d == 'E':
            self.col = self.col + 1
        elif self.d == 'S':
            self.row = self.row + 1
        elif self.d == 'W':
            self.col = self.col - 1
        self.loop.append((self.row,self.col))
        c = grid[(self.row,self.col)]
        if c == 'S':
            if self.n > 0:
                success(self)
                part2(self)
                exit()
        elif c in new_direction[self.d]:
            next_step = new_direction[self.d][c]
            #print('Path %d moved %c to (%d,%d) and found %c' % (self.id, self.d,self.row,self.col, c))
            
            #print('Path %d next step %c from %c at (%d,%d)' %(self.id, next_step,self.d,self.row,self.col))
            self.d = next_step
            self.n = self.n+1
        else:
            #print('Path %d next step %c not valid at (%d,%d) from %c' % (self.id, c, self.row, self.col, self.d))
            self.terminate()
            
def success(path):
    print(path)
    print('Found S. n = %d' % path.n)
    print('Answer 1:', int((path.n+1)/2))
    SUCCESS = True

pipes  = set()
points = set()

def print_grid():
    print()
    for row in range(0, nrow):
        s = ''
        for col in range(0, ncol):
            if (row,col) in pipes:
                s = s + grid[(row,col)]
            elif (row,col) in points:
                s = s + '.'
            else:
                s = s + ' '
        print(s)
    print()
        
def part2(path):
    #print(path.loop)
    rowtab = {}
    coltab = {}
    for row in range(0, nrow):
        rowtab[row] = []
        s = ''
        for col in range(0, ncol):
            if row == 0:
                coltab[col] = []
            if (row,col) in path.loop:
                s = s + 'X'
                c = grid[(row,col)]
                rowtab[row].append(col)
                coltab[col].append(row)
                pipes.add((row,col))
            else:
                s = s + '.'
        #print(s)
        
    for row in rowtab:
        rowtab[row].sort()
    for col in coltab:
        coltab[col].sort()

    #print('rowtab:', rowtab)
    #print('coltab:', coltab)
    #print( pipes)        

    for p in grid:
        if p not in pipes:
            points.add(p)
        
    for row in rowtab:
        if rowtab[row] == []:
            for col in range(0,ncol):
                if (row,col) in points:
                    points.remove((row,col))
        else:        
            for col in range(0,rowtab[row][0]):
                if (row,col) in points:
                    points.remove((row,col))
            for col in range(rowtab[row][-1]+1,nrow):
                if (row,col) in points:
                    points.remove((row,col))
    for col in coltab:
        if coltab[col] == []:
            for row in range(0,nrow):
                if (row,col) in points:
                    points.remove((row,col))
        else:                
            for row in range(0,coltab[col][0]):
                if (row,col) in points:
                    points.remove((row,col))
            for row in range(coltab[col][-1]+1,ncol):
                if (row,col) in points:
                    points.remove((row,col))

    #print_grid()    

    expanded_points = set()
    for p in points:
        expanded_points.add((2*p[0],2*p[1]))

    row = 0
    expanded_grid = {}
    for line in lines:    

        s = ''
        for col in range(0,len(line)):
            if (row/2,col) in pipes:
                s = s + line[col] + ' '
            elif (row/2,col) in points:
                s = s + '. '
            else:
                s = s + '  '
        maxcol = len(s)
            
        for i in [0,1]:
            s = s.replace('S -','S--')
            s = s.replace('S 7','S-7')
            s = s.replace('- S','--S')
            s = s.replace('F S','F-S')
            s = s.replace('L S','L-S')
            s = s.replace('S J','S-J')
            s = s.replace('- -','---')
            s = s.replace('L -','L--')
            s = s.replace('- J','--J')
            s = s.replace('F -','F--')
            s = s.replace('- 7','--7')
            s = s.replace('L J','L-J')
            s = s.replace('L 7','L-7')
            s = s.replace('F J','F-J')
            s = s.replace('F 7','F-7')
        # print(line, '\t', s)
        # print

        for col in range(0, len(s)):
            expanded_grid[(row,col)] = s[col]
            expanded_grid[(row+1,col)] = ' '
        row = row + 2
        maxrow = row
            
    for col in range(0,maxcol):
        s = ''
        for row in range(0,maxrow):
            s = s + expanded_grid[(row,col)]
        for i in [0,1]:
            s = s.replace('S |','S||')
            s = s.replace('S L','S|L')
            s = s.replace('S J','S|J')
            s = s.replace('| S','||S')
            s = s.replace('7 S','7|S')
            s = s.replace('F S','F|S')
            s = s.replace('| |','|||')
            s = s.replace('| J','||J')
            s = s.replace('| L','||L')
            s = s.replace('F |','F||')
            s = s.replace('F L','F|L')
            s = s.replace('F J','F|J')
            s = s.replace('7 |','7||')
            s = s.replace('7 J','7|J')
            s = s.replace('7 L','7|L')
        for row in range(0, maxrow):
            expanded_grid[(row,col)] = s[row]

    # new_grid = {}
    # for row in range(0,maxrow):
    #     s = ''
    #     for col in range(0,maxcol):
    #         s = s + expanded_grid[(row,col)]
    #     new_grid[row] = s
    #     print(s)

    diffused = set()
    def diffuse(p,n):
        #print('p:', p, n)
        if (p) not in expanded_grid:
            diffused.add(p)
            return
        elif (expanded_grid[p] == '.' or
              expanded_grid[p] == ' '):
            #print('Diffusing:', p, n)
            diffused.add(p)
        else:
            return
        if (p) in expanded_points:
            expanded_points.remove((p))
            #print('Removing:', p, n)
            print(len(expanded_points))
        neighbours = set()
        neighbours.add((p[0]+1,p[1]))
        neighbours.add((p[0]-1,p[1]))
        neighbours.add((p[0],p[1]+1))
        neighbours.add((p[0],p[1]-1))
        #print('neighbours:', neighbours)
        for (q) in neighbours:
            if ((q) in expanded_grid and
                (q) not in diffused):
                if (expanded_grid[(q)] == '.' or
                    expanded_grid[(q)] == ' '):
                    diffuse((q),n+1)
                    
    for row in [0,maxrow]:
        for col in [0,maxcol]:
            start = (row,col)
            if start in expanded_grid:
                if (expanded_grid[start] == '.' or
                    expanded_grid[start] == ' '):
                    diffuse(start,0)
                    
    print('Answer 2:', len(expanded_points))

                       
    
for d in ['N','E','S','W']:
    path(start, d)
SUCCESS = False
while not SUCCESS:
    pathlist = [path for path in paths] 
    for i in pathlist:
        if not SUCCESS:
            paths[i].go()
part2()

