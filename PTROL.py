# link do zadania
# https://pl.spoj.com/problems/PTROL/

import sys

answers = []
numberOfTests = int(sys.stdin.readline())
for i in range(numberOfTests):    
    liczby = input().split(' ')
    answer = []
    for i, liczba in enumerate(liczby):
        if i == 0:
            pass
        elif i < len(liczby) - 1:
            answer.append(liczby[i+1])
        elif i == len(liczby) - 1:
            answer.append(liczby[1])
    answers.append(answer)



for answer in answers:
    for i, liczba in enumerate(answer):
        if i < len(answer) - 1:
            sys.stdout.write(liczba + ' ')
        else:
            sys.stdout.write(liczba + '\n')
