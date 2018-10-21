# link do zadania
# https://pl.spoj.com/problems/VSR/
import sys

numberOfTests = int(sys.stdin.readline())
for i in range(numberOfTests):
    test = sys.stdin.readline().split(' ')
    v = (2*int(test[0]) * int(test[1])) // (int(test[0]) + int(test[1]))
    sys.stdout.write(str(v) + '\n')