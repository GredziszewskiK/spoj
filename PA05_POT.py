# link do zadania
# https://pl.spoj.com/problems/PA05_POT/
import sys
import math

number_of_tests = sys.stdin.readline()
for n in range(int(number_of_tests)):
    line = sys.stdin.readline()
    a = int(line[0:line.find(' ')])
    b = int(line[line.find(' '):])%4
    if b == 0:
        b=4    
    sys.stdout.write(str(a**b)[-1] + '\n')
