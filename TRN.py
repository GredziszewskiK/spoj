# link do zadania
# https://pl.spoj.com/problems/TRN/
import sys

rows = []
mn = sys.stdin.readline().split(' ')
for i in range(int(mn[0])):
    rows.append(sys.stdin.readline().replace('\n', '').split(' '))

for m in range(int(mn[1])):
    for n in range(int(mn[0])):
        sys.stdout.write(rows[n][m] + ' ')
    sys.stdout.write('\n')
