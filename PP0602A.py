# link do zadania
# https://pl.spoj.com/problems/PP0602A/
from sys import stdin, stdout

numberOfTests = int(stdin.readline())
for i in range(numberOfTests):
    test = stdin.readline().replace('\n', '').split(' ')[1:]
    stdout.writelines(' '.join(test[1::2]) + ' ' + ' '.join(test[::2]) + '\n')