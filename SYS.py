# link do zadania
# https://pl.spoj.com/problems/SYS/
import sys

def count(x, y):
    answer = ''
    while x > 0:
        rest = x % y
        if rest == 10:
            answer = answer + 'A'
        elif rest == 11:
            answer = answer + 'B'
        elif rest == 12:
            answer = answer + 'C'
        elif rest == 13:
            answer = answer + 'D'
        elif rest == 14:
            answer = answer + 'E'
        elif rest == 15:
            answer = answer + 'F'
        else:
            answer = answer + str(rest)
        x = x // y
    return answer[::-1]

numberOfTests = int(sys.stdin.readline())
for i in range(numberOfTests):
    test = int(sys.stdin.readline())
    sys.stdout.write('%s %s \n' % (count(test, 16), count(test, 11)))
    