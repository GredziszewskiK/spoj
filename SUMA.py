# link do zadania
# https://pl.spoj.com/problems/SUMA/
import sys

output = 0

for line in sys.stdin:
    output = output + int(line)
    print(output)