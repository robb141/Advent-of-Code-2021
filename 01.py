# import down
import os

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()
lines = [int(i) for i in lines]

res1 = 0
for i in range(len(lines) - 1):
    if lines[i+1] > lines[i]:
        res1 += 1
print(res1)

res2 = 0
for i in range(len(lines) - 3):
    if sum(lines[i+1:i+4]) > sum(lines[i:i+3]):
        res2 += 1
print(res2)
