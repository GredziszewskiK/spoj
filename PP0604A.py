# link do zadania
# https://pl.spoj.com/problems/PP0604A/

from sys import stdin, stdout
from math import fabs


t = int(stdin.readline())
answers = []
for x in range(t):
    test = [int(x) for x in stdin.readline().split(' ')]
    n = test[0]
    y = sum(test[1:])
    average = y / n
    absolutes = [fabs(x - average) for x in test[1:]]
    minimum = min(absolutes)
    answers.append(test[absolutes.index(minimum) + 1])

for answer in answers:
    stdout.write(str(answer) + '\n')