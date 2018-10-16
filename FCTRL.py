# link do zadania
# https://www.spoj.com/problems/FCTRL/

import sys
def zeros(x):
    zeros = 0
    y = 5
    while x >= y:
        zeros = zeros + int(x / y)
        y = y * 5
    return zeros 

answers = []
numberOfTests = int(sys.stdin.readline())
for i in range(numberOfTests):
    answers.append(zeros(int(sys.stdin.readline())))
  
for i, answer in enumerate(answers):
    sys.stdout.write(str(answer))
    if i < len(answers) - 1:
        sys.stdout.write('\n')

