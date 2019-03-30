# link do zadania
# https://pl.spoj.com/problems/PP0602B/
from sys import stdout, stdin
from copy import deepcopy
import time


number_of_test = int(stdin.readline())
answers = []
for test in range(number_of_test):
    rows_index, column_index= [int(x) for x in stdin.readline().split(' ')]
    rows = []
    for i in range(rows_index):
        rows.append([int(x) for x in stdin.readline().split(' ')])    
    moved = deepcopy(rows)
    for index, row in enumerate(moved):
        if index == 0:
            moved[index] = row[1:] + [row[0]]
        if index < rows_index - 1:
            moved[index][column_index - 1] = rows[index + 1][column_index - 1]    
        if index == rows_index - 1:
            moved[index] = [row[-1]] + row[:-1]
        if index > 0:
            moved[index][0] = rows[index - 1][0]
    answers.append(moved)
for answer in answers:
    for row in answer:
        for element in row:
            stdout.write(str(element) + ' ')
        stdout.write('\n')