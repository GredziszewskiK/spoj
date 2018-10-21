# link do zadania
# https://pl.spoj.com/problems/POL/
import sys

numberOfTests = int(sys.stdin.readline())
for i in range(numberOfTests):
    test = sys.stdin.readline()
    sys.stdout.write(test[:(len(test)//2)] + '\n')