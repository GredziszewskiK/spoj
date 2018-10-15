# link do zdania
# https://pl.spoj.com/problems/SKARBFI/
import sys, math

# point[0] - współrzędna y
# point[1] - współrzędna x 
def getPoint(direction, steps, point):
    if direction == 0:
        point[0] = point[0] + steps
    elif direction == 1:
        point[0] = point[0] - steps
    elif direction == 2:
        point[1] = point[1] - steps
    elif direction == 3:
        point[1] = point[1] + steps
    return point

numberOfTest = int(sys.stdin.readline())
points = []
answers = []

for i in range(numberOfTest):
    mapSteps = int(sys.stdin.readline())
    point = [0, 0]
    for x in range(mapSteps):
        step = sys.stdin.readline().split(' ')
        point = getPoint(int(step[0]), int(step[1]), point)
    points.append(point)

for point in points:
    if point[0] == point[1] == 0:
        answers.append('studnia')
    else:
        if point[0] != 0:
            if point[0] > 0:
                answers.append("0 " + str(int(math.fabs(point[0]))))
            if point[0] < 0:
                answers.append("1 " + str(int(math.fabs(point[0]))))
        if point[1] != 0:
            if point[1] > 0:
                answers.append("3 " + str(int(math.fabs(point[1]))))
            if point[1] < 0:
                answers.append("2 " + str(int(math.fabs(point[1]))))

for answer in answers:
    sys.stdout.write(answer + '\n') 