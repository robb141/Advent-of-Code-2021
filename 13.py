import down
import os
from copy import deepcopy

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().split('\n\n')

points = [list(map(int, p.split(','))) for p in lines[0].splitlines()]
folds = lines[1].splitlines()
rows = cols = 0

for i in folds[:2]:
    if i.split('=')[0][-1] == 'x':
        rows = int(i.split('=')[1]) * 2
    else:
        cols = int(i.split('=')[1]) * 2

grid = [[False for j in range(rows+1)] for i in range(cols+1)]

for p in points:
    grid[p[1]][p[0]] = True

ans = 0
for inst in range(len(folds)):
    DR = len(grid)
    DC = len(grid[0])
    if folds[inst].split('=')[0][-1] == 'y':
        new_DR = DR//2
        new_DC = DC
        new_grid = [[grid[i][j] for j in range(new_DC)] for i in range(new_DR)]
        for r in range(new_DR):
            for c in range(new_DC):
                if grid[DR - r - 1][c]:
                    new_grid[r][c] = True
                if inst == 0 and new_grid[r][c]:
                    ans += 1
        grid = deepcopy(new_grid)
    else:
        new_DR = DR
        new_DC = DC//2
        new_grid = [[grid[i][j] for j in range(new_DC)] for i in range(new_DR)]
        for r in range(new_DR):
            for c in range(new_DC):
                if grid[r][DC - c - 1]:
                    new_grid[r][c] = True
                if inst == 0 and new_grid[r][c]:
                    ans += 1
        grid = deepcopy(new_grid)


for r in range(new_DR):
    for c in range(new_DC):
        if grid[r][c]:
            grid[r][c] = '#'
        else:
            grid[r][c] = ' '

print(f'Part 1: {ans}')
print(f'Part 2:')
for i in grid:
    print(' '.join(i))



