# link do zadania
# https://pl.spoj.com/problems/CALC2/
import sys

rejestr = [None] * 10

for line in sys.stdin:
    operation = line.replace('\n', '').split(' ')
    if operation[0] == '+':
        sys.stdout.write(
            str(rejestr[int(operation[1])] + rejestr[int(operation[2])]) + '\n'
        )
    elif operation[0] == '-':
        sys.stdout.write(
            str(rejestr[int(operation[1])] - rejestr[int(operation[2])]) + '\n'
        )
    elif operation[0] == '*':
        sys.stdout.write(
            str(rejestr[int(operation[1])] * rejestr[int(operation[2])]) + '\n'
        )
    elif operation[0] == '/':
        sys.stdout.write(
            str(rejestr[int(operation[1])] // rejestr[int(operation[2])]) + '\n'
        )
    elif operation[0] == '%':
        sys.stdout.write(
            str(rejestr[int(operation[1])] % rejestr[int(operation[2])]) + '\n'
        )
    elif operation[0] == 'z':
        rejestr[int(operation[1])] = int(operation[2])
    