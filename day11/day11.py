#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

PART = 2

if 1 == PART:
    EXPANSION = 1
elif 2 == PART:
    EXPANSION = 1000000-1

import re

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

galactic_rows = {}
galactic_cols = {}
for row in range(0,nrow): galactic_rows[row] = []
for col in range(0,nrow): galactic_cols[col] = []
    
galactic_list = []
class galaxy:
    def __init__(self, row, col):
        self.id = len(galactic_list)
        self.row = row
        self.col = col
        galactic_list.append(self)
        galactic_rows[row].append(col)
        galactic_cols[col].append(row)
        
    def expand_row(self, row):
        if self.row > row:
            self.row = self.row + EXPANSION

    def expand_col(self, col):
        if self.col > col:
            self.col = self.col + EXPANSION

def read_data():
    p = re.compile('#')
    row = 0
    for line in lines:
        for galaxies in p.finditer(line):
            col = galaxies.start()
            galaxy(row,col)
        row = row + 1

def expand_universe():
    empty_cols = []
    empty_rows = []

    for row in galactic_rows:
        if galactic_rows[row] == []:
            empty_rows.append(row)

    for col in galactic_cols:
        if galactic_cols[col] == []:
            empty_cols.append(col)

    # The reverse sort makes expansion easy
    empty_cols.sort(reverse=True)
    empty_rows.sort(reverse=True)

    for row in empty_rows:
        for galaxies in galactic_list:
            galaxies.expand_row(row)

    for col in empty_cols:
        for galaxies in galactic_list:
            galaxies.expand_col(col)
            
def calculate():
    answer = 0
    for i in range(0, len(galactic_list)):
        for j in range(i+1, len(galactic_list)):
            gi = galactic_list[i]
            gj = galactic_list[j]
            col_diff = abs(galactic_list[i].col-galactic_list[j].col)
            row_diff = abs(galactic_list[i].row-galactic_list[j].row)
            distance = col_diff + row_diff
            answer = answer + distance
    print('Answer:', answer)
            
read_data()
expand_universe()
calculate()
