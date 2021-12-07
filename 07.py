import down
import os
from collections import defaultdict

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().split(',')

lines = sorted([int(x) for x in lines])

D1 = defaultdict(int)
D2 = defaultdict(int)

for i in lines:
    if not D1[i]:
        temp = 0
        for j, x in enumerate(lines):
            temp += abs(x-i)
        D1[i] = temp

print(f'Part1: {min(D1.values())}')

# Little bit of cheating here:
for i in range(lines[0], lines[-1]+1):
    if not D2[i]:
        r = 0
        step = 1
        for j in lines:
            r += (abs(i-j)/2)*(abs(i-j)+1)  # Gauss formula
        D2[i] = r

print(f'Part2: {int(min(D2.values()))}')
