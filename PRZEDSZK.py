import sys

def nwd(a, b):
    c = a % b
    a = b
    b = c
    if b == 0:
        return a
    else:
        return nwd(a, b)

def nww(a, b):
    return int(a*b/nwd(a, b))

outputs = []
number_of_tests = sys.stdin.readline()

for n in range(int(number_of_tests)):
    test = sys.stdin.readline()
    outputs.append(nww(int(test[:test.find(' ')]), int(test[test.find(' '):])))

for answer in outputs:
    sys.stdout.write(str(answer) + '\n')

# print(outputs)
# print(nwd(12, 15))
# print(nww(12, 15))