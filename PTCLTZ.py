# link do zdania
# https://pl.spoj.com/problems/PTCLTZ/
import sys

def getX(xn):
    if xn%2 == 0:
        x = xn/2
    if xn%2 != 0:
        x = 3*xn+1
    return x

answers = []
numberOfTest = int(sys.stdin.readline()) 
for i in range(numberOfTest):
    x = int(sys.stdin.readline())
    n = 0
    while x != 1:
        n += 1
        x = getX(x)
    answers.append(n)

for answer in answers:
    sys.stdout.write(str(answer) + '\n')