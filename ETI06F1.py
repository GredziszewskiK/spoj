# link do zadania
# https://pl.spoj.com/problems/ETI06F1/

from math import sqrt
from sys import stdin, stdout

test = stdin.readline().split(" ")
R = sqrt(float(test[0])**2 - ((1/2*float(test[1]))**2))
stdout.writelines(str(3.141592654*R**2))