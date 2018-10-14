# link do zadania
# https://pl.spoj.com/problems/PP0506A/

import sys, math

def sortByValue(elem):
    return elem[3]

numberOfTests = int(input())
answers = []
for i in range(numberOfTests):
    numberOfPoints = int(input())
    inputs = []
    for p in range(numberOfPoints):
        inputs.append(input().split(' '))  

    for point in inputs:
        point.append(
            math.sqrt(int(point[1])**2 + int(point[2])**2)
        )
    inputs.sort(key=sortByValue)
    answers.append(inputs)
    if i < numberOfTests - 1:
        input()

for answer in answers:
    for i, point in enumerate(answer):
        sys.stdout.write(point[0] + ' ' + point[1] + ' ' + point[2] + '\n')   
        if i < len(answer) - 1:
            sys.stdout.write('\n')
    