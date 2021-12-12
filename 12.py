import down
import os
from collections import Counter
from copy import deepcopy

# small letter is Unicode number between 97 and 122 and big letter is between 65 and 90

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().splitlines()
lines = [i.split('-') for i in lines]


def valid_count_of_small_letter(elems, new_letter):
    new2 = deepcopy(elems)
    d = Counter(new2 + [new_letter])
    count_bigger_than_one = 0
    for k, v in d.items():
        if k != 'start' and 97 <= ord(k[0]) <= 122:
            if v > 1:
                count_bigger_than_one += 1
            if v > 2:
                return False
    if count_bigger_than_one > 1:
        return False
    return True


def get_paths(r):
    for i in new_paths:
        if r[-1] in i:
            next_point = list(filter(lambda x: r[-1] not in x, i))[0]
            if next_point == 'end':
                res.append(r)
            elif 97 <= ord(next_point[0]) <= 122 and next_point not in r:
                new = deepcopy(r)
                new.append(next_point)
                get_paths(new)
            elif 65 <= ord(next_point[0]) <= 90:
                new = deepcopy(r)
                new.append(next_point)
                get_paths(new)


def get_paths2(r):
    for i in new_paths:
        if r[-1] in i:
            next_point = list(filter(lambda x: r[-1] not in x, i))[0]
            if next_point == 'end':
                res2.append(r + [next_point])
            elif 97 <= ord(next_point[0]) <= 122 and valid_count_of_small_letter(r, next_point):
                new = deepcopy(r)
                new.append(next_point)
                get_paths2(new)
            elif 65 <= ord(next_point[0]) <= 90:
                new = deepcopy(r)
                new.append(next_point)
                get_paths2(new)


res = []
res2 = []
for line in range(len(lines)):
    if 'start' in lines[line]:
        temp = ['start', [elem for elem in lines[line] if elem != 'start'][0]]
        new_paths = list(filter(lambda x: 'start' not in x, lines))
        get_paths(temp)
        get_paths2(temp)

print(f'Part 1: {len(res)}')
print(f'Part 2: {len(res2)}')

