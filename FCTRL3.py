# link do zadania
# https://pl.spoj.com/problems/FCTRL3/
import sys
import math

output = []
number_of_test = sys.stdin.readline()


for i in range(int(number_of_test)):
    value = int(sys.stdin.readline())
    if value < 10 :
        y = math.factorial(value)
        output.append(str(y)[-2:-1] + ' ' + str(y)[-1:] if len(str(y))>1 else '0' + ' ' + str(y)[-1:] )
    else:
        output.append('0 0')

for answer in output:
    sys.stdout.write(answer + '\n')