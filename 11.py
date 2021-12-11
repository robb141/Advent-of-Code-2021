import down
import os

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as my_f:
    lines = my_f.read().splitlines()

lines = [list(x) for x in lines]
lines = [list(int(y) for y in x) for x in lines]

rows = len(lines)
cols = len(lines[0])
DR = [-1, -1, -1, 0, 1, 1, 1, 0]
DC = [-1, 0, 1, 1, 1, 0, -1, -1]
flashes = 0


def getNewGrid(row, col):
    for i in range(len(DR)):
        newR = row + DR[i]
        newC = col + DC[i]
        if 0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in SEEN:
            lines[newR][newC] += 1
    SEEN.append((row, col))
    lines[row][col] = 0


day = 1
while True:
    SEEN = []
    lines = [list(map(lambda x: x + 1, i)) for i in lines]
    while True:
        ok = True
        for r in range(rows):
            if any(True for c in lines[r] if c > 9):
                ok = False
                for c in range(cols):
                    if lines[r][c] > 9:
                        getNewGrid(r, c)
        if ok:
            break
    flashes += len(SEEN)
    if day == 100:
        print(f'Part 1: {flashes}')
    if len(SEEN) == rows * cols:
        print(f'Part 2: {day}')
        break
    day += 1
