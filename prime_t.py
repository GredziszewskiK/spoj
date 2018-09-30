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

output = []
number_of_tests = sys.stdin.readline()
for i in range(int(number_of_tests)):
    output.append(is_prime_number(sys.stdin.readline()))

for answer in output:
    sys.stdout.write(answer + '\n')
