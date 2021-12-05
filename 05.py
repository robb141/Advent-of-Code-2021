import down
from collections import defaultdict
import os


def countValuesInDict(obj, base_value=1):
    return len(list(filter(lambda x: x > base_value, obj.values())))


with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().replace(' ', '').splitlines()

coor_range = [line.split('->') for line in lines]
for k in range(len(coor_range)):
    coor_range[k][0] = tuple(int(x) for x in coor_range[k][0].split(','))
    coor_range[k][1] = tuple(int(x) for x in coor_range[k][1].split(','))

D1 = defaultdict(int)
D2 = defaultdict(int)
for line in coor_range:
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    if x1 == y1 and x2 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            D2[(i, i)] += 1
    elif x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            D1[(x1, i)] += 1
            D2[(x1, i)] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            D1[(i, y1)] += 1
            D2[(i, y1)] += 1
    else:  # 8,0 -> 0,8  or  6,4 -> 2,0
        if x1 > x2:
            for i, v in enumerate(range(x2, x1+1), 0):
                if y1 > y2:
                    D2[(v, y2 + i)] += 1
                else:
                    D2[(v, y2 - i)] += 1
        else:
            for i, v in enumerate(range(x1, x2+1), 0):
                if y1 > y2:
                    D2[(v, y1 - i)] += 1
                else:
                    D2[(v, y1 + i)] += 1


print(f'Part1: {countValuesInDict(D1)}')
print(f'Part2: {countValuesInDict(D2)}')
