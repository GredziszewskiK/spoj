# link do zadania
# https://pl.spoj.com/problems/PRIME_T/
from math import sqrt
from sys import stdout, stdin

def is_prime_number(number):
    x = int(number)
    y = sqrt(x)
    if x < 2:
        return 'NIE\n'
    for n in range(2, int(y)+1):
        if x % n == 0:
            return 'NIE\n'
    return 'TAK\n'

for i in range(int(stdin.readline())):
    stdout.write(is_prime_number(stdin.readline()))
