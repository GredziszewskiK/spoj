# link do zadania
# https://pl.spoj.com/problems/FANGEN/

import sys, math

def add_level(lista):
    n = len(lista)
    for row in lista: 
        row.insert(0, '?')         
        row.append('?')   
    row = ['*', '*']
    for i in range(n):
        row.insert(1, '?')   
    lista.insert(0, list(row))
    lista.append(list(row))
    return lista

def create(lista, direction):
    first = True
    char = []
    if direction == 'left':
        chars = ['*', '.']
    elif direction == 'right':
        chars = ['.', '*']
    n = int(len(lista)/2)
    m = len(lista) - 1
    for i, row in enumerate(lista):
        if first:
            first = False
            for j, char in enumerate(row):
                if j in range(n, m):
                    row[j] = chars[0]
                if j in range(1, n):
                    row[j] = chars[1]
        elif i == len(lista)-1:
            for k, char in enumerate(row):
                if k in range(n, m):
                    row[k] = chars[1]
                if k in range(1, n):
                    row[k] = chars[0]
        else:
            if i in range(n, m):
                row[0] = chars[1] 
                row[m] = chars[0]
            if i in range(1, n):   
                row[0] = chars[0]
                row[m] = chars[1] 
    return lista

def print_fan(lista):
    for row in lista:
        for point in row:
            sys.stdout.write(point)
        sys.stdout.write('\n')

answers = []
level = 1
while(level != 0):         
    lista = [['*','*'],['*','*']]
    level = int(sys.stdin.readline())
    if level == 0:
        break
    if level < 0:
        level = int(math.fabs(level))
        direction = 'right'
    elif level > 1:
        direction = 'left'
    if level != 1:
        for i in range(level-1):
            lista = add_level(lista)
            lista = create(lista, direction)
    answers.append(lista)

for answer in answers:
    print_fan(answer)