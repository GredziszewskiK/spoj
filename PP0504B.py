# link do zadania
# https://pl.spoj.com/problems/PP0504B/

import sys

def string_merge(a, b):
    answer = ''
    x = len(a)
    if len(a) > len(b):
        x = len(b)
    for y in range(x):
        answer = answer + a[y] + b[y]
    return answer

answers = []
numberOfTests = int(sys.stdin.readline())
for i in range(numberOfTests):
    test = sys.stdin.readline().split(' ')
    answers.append(string_merge(test[0].strip(), test[1].strip()))

for answer in answers:
    sys.stdout.write(answer + '\n')