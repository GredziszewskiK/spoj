# link do zadania
# https://pl.spoj.com/problems/RNO_DOD/
import sys

for i in range(int(sys.stdin.readline())):
    number_of_elements = sys.stdin.readline()
    elements = input().split(' ')
    elements = [int(x) for x in elements]
    sys.stdout.write('%s\n' % sum(elements))
