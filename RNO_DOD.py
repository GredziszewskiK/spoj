# link do zadania
# https://pl.spoj.com/problems/RNO_DOD/
import sys

outputs = []

number_of_test = input()
for i in range(int(number_of_test)):
    number_of_elements = sys.stdin.readline()
    elements = input().split(' ')
    elements = [int(x) for x in elements]
    outputs.append(sum(elements))

for answer in outputs:
    sys.stdout.write(str(answer) + '\n')
