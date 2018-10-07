#rozwiązanie zadania
#https://pl.spoj.com/problems/PP0502B/

import sys

output = []
numberOfTests = int(input())

for i in range(numberOfTests):
    output.append(input().split(' ')[:0:-1])

for answer in output:
    for number in answer:
        sys.stdout.write(str(number) + ' ')
    sys.stdout.write('\n')
