# link do zadania
# https://pl.spoj.com/problems/STOS/
import sys
from collections import deque

stos = deque(maxlen = 10)
task = ''
for line in sys.stdin:
    line = line.replace('\n', '')
    if line == '+':
        task = line
    elif line == '-':
        if stos:
            sys.stdout.write(stos.pop() + '\n')
        else:
            sys.stdout.write(':(\n')
    else:
        if len(stos) != stos.maxlen:
            stos.append(line)
            sys.stdout.write(':)\n')
        else:
            sys.stdout.write(':(\n')
