# link do zadania
# https://pl.spoj.com/problems/FLAMASTE/
import sys
def get_char(last_char, curent_char, counter):
    if counter <= 2:
        r = ''
        for i in range(counter):
            r = r + last_char
        return r
    elif counter > 2:
        return last_char + str(counter)

def get_shortcut(verb):
    last_char = ''
    counter = 1
    output = ''
    for index, char in enumerate(verb):
        if last_char == char:
            counter = counter + 1
        else:
            output = output + get_char(last_char, char, counter)
            last_char = char
            counter = 1
        if index == len(verb)-1:
            output = output + get_char(last_char, char, counter)
    return output

output = []
number_of_tests = sys.stdin.readline()
for i in range(int(number_of_tests)):
    output.append(get_shortcut(sys.stdin.readline()))

for answer in output:
    sys.stdout.write(answer)