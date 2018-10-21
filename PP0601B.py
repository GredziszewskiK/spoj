# link do zadania
# https://pl.spoj.com/problems/PP0601B/
import sys

def dividers(n, x, y):
    for i in range(1, n):
        if  i % x == 0 and i % y != 0:
            sys.stdout.write('%s ' % i)
    sys.stdout.write('\n')

numberOfTests = int(sys.stdin.readline())
for i in range(numberOfTests):
    test = sys.stdin.readline().split(' ')
    dividers(int(test[0]), int(test[1]), int(test[2]))