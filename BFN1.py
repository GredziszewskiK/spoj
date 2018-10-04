# link do zadania
# https://pl.spoj.com/problems/BFN1/

import sys

def palidron(string):
    if string == string[::-1]:
        return True
    return False


def make_palidron(string, x=0):
    if palidron(string):
        return string, x
    else:
        x += 1
        return make_palidron(str(int(string)+int(string[::-1])), x)

output = []
number_of_test = int(sys.stdin.readline())

for i in range(number_of_test):
    output.append(make_palidron(input()))

for answer in output:
    sys.stdout.write(str(answer[0]) + ' ' + str(answer[1]) + '\n')
