import down
import os
from collections import defaultdict

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().splitlines()

D_lenghts = {2: 1, 4: 4, 3: 7, 7: 8}
D1 = defaultdict(int)

for line in lines:
    output = line.split('|')[1].strip()
    for digit in output.split():
        digit_len = len(digit.strip())
        if digit_len in D_lenghts.keys():
            D1[digit_len] += 1

print(f'Part1: {sum(D1.values())}')

result = 0
for line in lines:
    temp_count = 0
    Combs = {}
    for l in line.split():
        if len(Combs) == 10:
            break
        if sorted(l) not in Combs.values():
            Combs[temp_count] = sorted(l)
            temp_count += 1

    values = Combs.values()

    one = list(filter(lambda x: len(x) == 2, values))[0]
    four = list(filter(lambda x: len(x) == 4, values))[0]
    seven = list(filter(lambda x: len(x) == 3, values))[0]
    eight = list(filter(lambda x: len(x) == 7, values))[0]

    for j in list(filter(lambda x: len(x) == 6, values)):
        if not all(x in j for x in one):
            if one[0] in j:
                down_right = one[0]
                up_right = one[1]
            else:
                down_right = one[1]
                up_right = one[0]

    for j in list(filter(lambda x: len(x) == 5, values)):
        if all(x in j for x in seven):
            three = j
            break

    up = [item for item in seven if item not in one][0]
    for j in four:
        if j not in three:
            up_left = j
    middle = [elem for elem in four if elem not in one + [up_left]][0]

    for j in list(filter(lambda x: len(x) == 6, values)):
        if middle not in j:
            zero = j

    for j in list(filter(lambda x: len(x) == 6, values)):
        if j != zero:
            if up_right not in j:
                six = j
            else:
                nine = j

    for j in list(filter(lambda x: len(x) == 5, values)):
        if j != three:
            if up_right not in j:
                five = j
            else:
                two = j

    D2 = {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}

    s = ''
    for elem in line.split('|')[1].split():
        r = [k for k, v in D2.items() if v == sorted(elem)][0]
        s += str(r)
    result += int(s)

print(f'Part2: {result}')


# print(f'Part1: {min(D1.values())}')

