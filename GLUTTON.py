# link do zadania
# https://pl.spoj.com/problems/GLUTTON/
import sys
import math

doba = 86400 

answers = []
numberOfTesrs = int(sys.stdin.readline())

for i in range(numberOfTesrs):
    nm = sys.stdin.readline().split(' ')
    cakes = 0
    for j in range(int(nm[0])):
        cakes = cakes + int(doba / int(sys.stdin.readline()))
    answers.append(int(math.ceil(cakes/int(nm[1]))))

for answer in answers:
    sys.stdout.write(str(answer) + '\n')