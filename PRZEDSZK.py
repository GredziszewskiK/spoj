# link do zadania
# https://pl.spoj.com/problems/PRZEDSZK/
import sys

def nwd(a, b):
    c = a % b
    a = b
    b = c
    if b == 0:
        return a
    else:
        return nwd(a, b)

def nww(a, b):
    return int(a*b/nwd(a, b))

number_of_tests = sys.stdin.readline()

for n in range(int(number_of_tests)):
    test = sys.stdin.readline()
    sys.stdout.write('%s\n' % nww(int(test[:test.find(' ')]), int(test[test.find(' '):])))

