import down
import os
from functools import reduce

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().splitlines()

lines = [list(x) for x in lines]
lines = [list(int(y) for y in x) for x in lines]


def compare(r, c):
    if r - 1 >= 0:
        if lines[r][c] >= lines[r-1][c]:
            return False
    if r + 1 < len(lines):
        if lines[r][c] >= lines[r+1][c]:
            return False
    if c - 1 >= 0:
        if lines[r][c] >= lines[r][c-1]:
            return False
    if c + 1 < len(lines[0]):
        if lines[r][c] >= lines[r][c+1]:
            return False
    return True


def compare2(r, c, seen):
    seen.add((r, c))
    if r - 1 >= 0:
        if lines[r][c] < lines[r - 1][c] != 9:
            seen = compare2(r-1, c, seen)
    if r + 1 < len(lines):
        if lines[r][c] < lines[r + 1][c] != 9:
            seen = compare2(r+1, c, seen)
    if c - 1 >= 0:
        if lines[r][c] < lines[r][c - 1] != 9:
            seen = compare2(r, c-1, seen)
    if c + 1 < len(lines[0]):
        if lines[r][c] < lines[r][c + 1] != 9:
            seen = compare2(r, c+1, seen)
    return seen


res1 = 0
res2 = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if compare(i, j):
            res1 += int(lines[i][j]) + 1
            res2.append(len(compare2(i, j, set())))

print(f'Part 1: {res1}')
print(f'Part 2: {reduce(lambda x, y: x*y, (sorted(res2)[-3:]))}')
