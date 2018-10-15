# link do zadania
# https://pl.spoj.com/problems/EUCGAME/
import sys, math

def nwd(a, b):
    c = a % b
    a = b
    b = c
    if b == 0:
        return a
    else:
        return nwd(a, b)

answers = []
numberOfTests = int(sys.stdin.readline())
for i in range(numberOfTests):
    tokens = sys.stdin.readline().split(' ')
    a = int(tokens[0])
    b = int(tokens[1])
    answers.append(nwd(a, b)*2)

for answer in answers:
    sys.stdout.write(str(answer) + '\n')