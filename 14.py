import down
import os
from collections import Counter


def return_new_string(text):
    new = ''
    for t in range(len(text)-1):
        new += inp[t:t+1] + D[inp[t:t+2]]
    new += inp[-1]
    return new


with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().splitlines()

inp = lines[0]
D = {}
for i in lines[2:]:
    pair, searched = i.strip().split(' -> ')
    D[pair] = searched

for _ in range(10):
    inp = return_new_string(inp)

P1 = Counter(inp)
print(f'Part 1: {max(P1.values()) - min(P1.values())}')


inp = lines[0]
R = Counter()
for i in range(len(inp)-1):
    R[inp[i:i+2]] += 1

for _ in range(40):
    Temp = Counter()
    for k in R.keys():
        lookup = D[k]
        Temp[f'{k[0]}{lookup}'] += R[k]
        Temp[f'{lookup}{k[1]}'] += R[k]
    R = Temp

P2 = Counter()
for k in R:
    P2[k[0]] += R[k]
P2[inp[-1]] += 1

print(f'Part 2: {max(P2.values()) - min(P2.values())}')
