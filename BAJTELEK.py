# link do zadania
# https://pl.spoj.com/problems/BAJTELEK/

# rozwiązanie nie działa, lokalnie daje dobre wyniki
# błąd wykonania

from sys import stdin, stdout
from math import fabs

def countField(xs, ys):
    p = 0
    for index, x in enumerate(xs): 
        y1 = ys[index - 1]
        if index >= len(ys) - 1:
            y2 = ys[0]
        else:
            y2 = ys[index + 1]
        p = p + x*(y2-y1)
    p = fabs(p)
    return p / 2

def splitRows(rows):
    black = []
    grey = []
    firstX = rows[0]
    firstY = rows[1]
    for index, element in enumerate(rows[2::2]):
        if element == firstX:
            if rows[3 + (index * 2)] == firstY:
                black = rows[:4 + (index * 2)]
                grey = rows[4 + (index * 2):]
                break
    return black, grey

n = int(stdin.readline())
answers = []
for test in range(n):
    # read impput
    rows = stdin.readline()
    rows = rows + stdin.readline()
    rows = list(filter(('').__ne__, rows.replace('\n', ' ').strip().split(' ')))
    rows = [int(x) for x in rows]
    black, grey = splitRows(rows)
    # podziałna x i y czarnego pola
    blackXs = black[:-2:2]
    blackYs = black[1:-2:2]
    # obliczanie czarnego pola
    blackField = countField(blackXs, blackYs)
    # podział na x i y szarego pola
    greyXs = grey[:-2:2]
    greyYs = grey[1:-2:2]
    # obliczanie szarego pola
    greyField = countField(greyXs, greyYs)

    # obliczanie tuszu
    if blackField > greyField:
        answer = int((blackField  - greyField) * 6 + greyField * 10)
    else:
        answer = int((greyField  - blackField) * 6 + blackField * 10)
    answers.append(answer)
    stdin.readline()

for answer in answers:
    stdout.write(str(answer) + '\n')


# 2
# 1 2 2 1 2 2 1 2
# 0 2 3 0 2 3 0 2

# 2 3 5 2 3 3 5 4 2 3
# 1 5 1 3 5 0 3 2 5 1 6 2 4 3 6 3 6 4 7 4 7 1 6 1 6 0 8 0 8 5 1 5

# 6
# 5 3 4 5 5 4 6 5 5 3
# 8 8 6 4 8 0 5 3 2 0 4 4 2 8 5 5 8 8

# -1 1 0 0 1 1 0 -1 -1 1
# -3 4 0 1 3 4 1 0 3 -4 0 -1 -3 -4 -1 0 -3 4

# 50000 30000 40000 50000 50000 40000 60000 50000 50000 30000
# 80000 80000 60000 40000 80000 0 50000 30000 20000 0 40000 40000 20000 80000 50000 50000 80000 80000

# -10000 10000 0 0 10000 10000 0 -10000 -10000 10000
# -30000 40000 0 10000 30000 40000 10000 0 30000 -40000 0 -10000 -30000 -40000 -10000 0 -30000 40000

# 8 8 6 4 8 0 5 3 2 0 4 4 2 8 5 5 8 8
# 5 3 4 5 5 4 6 5 5 3

# -3 4 0 1 3 4 1 0 3 -4 0 -1 -3 -4 -1 0 -3 4
# -1 1 0 0 1 1 0 -1 -1 1


# 88
# 88
# 8800000000
# 8800000000
# 88
# 88