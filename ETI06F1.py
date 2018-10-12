# link do zadania
# https://pl.spoj.com/problems/ETI06F1/


import math
import sys

pi = 3.141592654

test = sys.stdin.readline().split(" ")
R = math.sqrt(float(test[0])**2 - ((1/2*float(test[1]))**2))
sys.stdout.writelines(str(pi*R**2))