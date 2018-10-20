# link do zadania
# https://pl.spoj.com/problems/CALC/
import sys

for line in sys.stdin:
    operation = line.replace('\n', '').split(' ')
    # print(operation)
    if operation[0] == '+':
        sys.stdout.write(str(int(operation[1]) + int(operation[2])) + '\n')
    elif operation[0] == '-':
        sys.stdout.write(str(int(operation[1]) - int(operation[2])) + '\n')
    elif operation[0] == '*':
        sys.stdout.write(str(int(operation[1]) * int(operation[2])) + '\n')
    elif operation[0] == '/':
        sys.stdout.write(str(int(operation[1]) // int(operation[2])) + '\n')
    elif operation[0] == '%':
        sys.stdout.write(str(int(operation[1]) % int(operation[2])) + '\n')
    