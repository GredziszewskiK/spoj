import sys
import math

output = []
number_of_tests = sys.stdin.readline()
for n in range(int(number_of_tests)):
    line = sys.stdin.readline()
    a = int(line[0:line.find(' ')])
    b = int(line[line.find(' '):])%4
    if b == 0:
        b=4    
    output.append(str(a**b)[-1])

for answer in output:
    sys.stdout.write(answer + '\n')