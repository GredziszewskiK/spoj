# link do zadania
# https://pl.spoj.com/problems/prime_t/
import math
import sys

def is_prime_number(number):
    x = int(number)
    y = math.sqrt(x)
    if x == 0 or x == 1:
        return 'NIE'
    for n in range(2, int(y)+1):
        if n > 0 and (x % n) == 0:
            return 'NIE'
    return 'TAK'

for i in range(int(sys.stdin.readline())):
    sys.stdout.write(is_prime_number(sys.stdin.readline()) + '\n')
