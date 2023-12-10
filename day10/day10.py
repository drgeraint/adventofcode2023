#! /usr/bin/env python3

maxcol = 0
maxrow = 0

# only need to look N, S, E, W
# recall direction when checking next
# traverse all paths one step at a time (avoid long detours)


#with open('test2.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
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
    #print('Answer 1:', n/2)
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
        #print('Terminating path %d at (%d,%d) [%c]' %
              #(self.id, self.col, self.row, grid[(self.row,self.col)]))
        paths.pop(self.id)
        
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
        c = grid[(self.row,self.col)]
        if c == 'S':
            if self.n > 0:
                success(self)
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
    paths = []
            
for d in ['N','E','S','W']:
    path(start, d)

#print(grid)
#for k,v in paths.items():
    #print(k, v.row, v.col, v.d)
SUCCESS = False
while not SUCCESS:
    pathlist = [path for path in paths] 
    for i in pathlist:
        if not SUCCESS:
            paths[i].go()
    #print(paths)
