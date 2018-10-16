# link do zadania
# https://pl.spoj.com/problems/ROWNANIE/

import sys

for line in sys.stdin:
    factors = [float(x) for x in line.split(' ')]
    delta = factors[1]**2 - (4 * factors[0] * factors[2])
    if delta > 0:
        sys.stdout.write('2\n')
    elif delta == 0:
        sys.stdout.write('1\n')
    elif delta < 0:
        sys.stdout.write('0\n')
