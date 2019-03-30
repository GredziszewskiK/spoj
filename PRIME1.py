# link do zadania
# https://www.spoj.com/problems/PRIME1/

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