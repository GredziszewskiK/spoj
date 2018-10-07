#link do zadania
#https://pl.spoj.com/problems/PP0501A/

import sys

def nwd(a, b):
    c = a % b
    a = b
    b = c
    if b == 0:
        return a
    else:
        return nwd(a, b)

outputs = []
numberOfTests = input()

for i in range(int(numberOfTests)):
    test = input()
    outputs.append(nwd(int(test[:test.find(' ')]), int(test[test.find(' '):])))

for answer in outputs:
    sys.stdout.write(str(answer) + '\n')