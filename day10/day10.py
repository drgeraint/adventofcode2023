#! /usr/bin/env python3

filename = 'test6.txt'
#filename = 'input.txt'

import re

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

# Part 1
grid      = {}
path_list = []
pipes     = set()
start	  = None
nrow      = len(lines)
ncol      = len(lines[0])

# Part 2
expanded_grid   = {}
points          = set()
diffused        = set()
expanded_points = set()

def read_data():
    row = 0
    for line in lines:
        col = 0
        for c in line:
            grid[(row,col)] = c
            if 'S' == c:
                start = (row,col)
            col = col + 1
        row = row + 1
    return start
    
turn_map = {
    'N': { '|': 'N', '7': 'W', 'F': 'E' },
    'E': { '-': 'E', '7': 'S', 'J': 'N' },
    'S': { '|': 'S', 'J': 'W', 'L': 'E' },
    'W': { '-': 'W', 'L': 'N', 'F': 'S' }}
    
class Path:
    def __init__(self, position, direction):
        self.posn = position
        self.dirn   = direction
        self.id  = len(path_list)
        path_list.append(self)
        self.loop = [position]

    def go(self):
        if   'N' == self.dirn:
            next_step = (self.posn[0]-1, self.posn[1]  )
        elif 'E' == self.dirn:
            next_step = (self.posn[0]  , self.posn[1]+1)
        elif 'S' == self.dirn:
            next_step = (self.posn[0]+1, self.posn[1]  )
        elif 'W' == self.dirn:
            next_step = (self.posn[0]  , self.posn[1]-1)

        if next_step not in grid:
            self.terminate()
        else:
            self.posn = next_step
            self.loop.append(self.posn)
            c = grid[self.posn]
            if 'S' == c:
                self.success()
            elif c in turn_map[self.dirn]:
                self.dirn = turn_map[self.dirn][c]
                self.go()
            else:
                self.terminate()

    def success(self):
        print('Found S. n = %d' % len(self.loop))
        print('Answer 1:', int(len(self.loop)+1)/2)
        for posn in self.loop: pipes.add(posn)
              
    def terminate(self):
        path_list.pop(self.id)

def follow_pipes():
    for direction in ['N', 'E', 'S', 'W']:
        Path(start, direction).go()
    for path in path_list:
        for position in path.loop: pipes.add(position)        

def tidy_grid():
    for position in grid:
        if position not in pipes:
            grid[position] = '.'
            points.add(position)
        
def expand_grid():
    for position in points:
        expanded_points.add((position[0]*2,position[1]*2))

    for row in range(0, nrow):
        for col in range(0, ncol):
            expanded_grid[(2*row,2*col)] = grid[(row,col)]

    old_rows = range(0, 2*nrow, 2)
    old_cols = range(0, 2*ncol, 2)
    new_rows = range(1, 2*(nrow-1), 2)
    new_cols = range(1, 2*(ncol-1), 2)
    # Do not expand horizontal links for 7F 7L JF JL
    # or vertical links for LF L7 J7 JF which leak
    for row in old_rows:
        for col in new_cols:
            l = expanded_grid[(row,col-1)]
            r = expanded_grid[(row,col+1)]
            if (l in ['S','-','F','L'] and
                r in ['S','-','7','J']):
                expanded_grid[(row,col)] = '-'
            else:
                expanded_grid[(row,col)] = ' '
    for col in old_cols:
        for row in new_rows:
            u = expanded_grid[(row-1,col)]
            d = expanded_grid[(row+1,col)]
            if (u in ['S','|','7','F'] and
                d in ['S','|','J','L']):
                expanded_grid[(row,col)] = '|'
            else:
                expanded_grid[(row,col)] = ' '
    for row in new_rows:
        for col in new_cols:
            expanded_grid[(row,col)] = ' '

def print_expanded_grid():
    for row in range(0, 2*nrow-1):
        s = ''
        for col in range(0, 2*ncol-1):
            s = s + expanded_grid[(row,col)]
        print(s)

def diffuse(position, level):
    #print('Diffusing', position, level, len(expanded_points))
    #print(expanded_points)
    if position not in expanded_grid:
        diffused.add(position)
        expanded_points.remove(position)
        return
    elif ('.' == expanded_grid[position] or
          ' ' == expanded_grid[position]):
        diffused.add(position)
        if position in expanded_points:
            expanded_points.remove(position)
        expanded_grid[position] = ' '
    else:
        return
    # Reached here from the edge so not contained
    adjacent = set(((position[0]+1,position[1]),
                    (position[0]-1,position[1]),
                    (position[0],position[1]+1),
                    (position[0],position[1]-1)))
    for node in adjacent:
        if (node in expanded_grid and
            node not in diffused):
            if ('.' == expanded_grid[node] or
                ' ' == expanded_grid[node]):
                diffuse(node, level+1)                                     

def diffuse_from_edges():
    for row in [0, 2*(nrow-1)]:
        for col in range(0, ncol*2-1):
            position = (row,col)
            if ('.' == expanded_grid[position] or
                ' ' == expanded_grid[position]):
                diffuse(position, 0)
    for col in [0, 2*(ncol-1)]:
        for row in range(0, nrow*2-1):
            position = (row,col)
            if ('.' == expanded_grid[position] or
                ' ' == expanded_grid[position]):
                diffuse(position, 0)
                
    print('Answer 2:', len(expanded_points))
                
# Part 1
start = read_data()
follow_pipes()

# Part 2
tidy_grid()
expand_grid()
if 'input.txt' != filename:
    print_expanded_grid()
diffuse_from_edges()
if 'input.txt' != filename:
    print_expanded_grid()

