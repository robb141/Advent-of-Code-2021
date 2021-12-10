import down
import os
from collections import deque

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().splitlines()


def get_key(search):
    for k, v in D1.items():
        if search in v:
            return k


def calc_score(queue):
    result = 0
    for x in reversed(queue):
        result = result * 5 + D2[x]
    return result


D1 = {3: '()', 57: '[]', 1197: '{}', 25137: '<>'}
D2 = {'(': 1, '[': 2, '{': 3, '<': 4}
res1 = 0
res2 = []
for i in lines:
    d = deque()
    ok = True
    for j in i:
        if not len(d):
            if any([True for x in D1.values() if x[1] == j]):
                res1 += get_key(j)
                ok = False
                break
            d.append(j)
        else:
            if any([True for x in D1.values() if x[0] == j]):
                d.append(j)
            else:
                elem = d.pop()
                if get_key(elem) == get_key(j):
                    continue
                else:
                    res1 += get_key(j)
                    ok = False
                    break
    if ok:
        res2.append(calc_score(d))


print(f'Part 1: {res1}')
sorted_list = sorted(res2)
print(f'Part 2: {sorted_list[len(sorted_list)//2]}')
