import down
import os

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()
    lines = list(map(lambda x: x.split(), lines))

print(lines)

res1 = 0
hor = 0
dep1 = 0
dep2 = 0
aim = 0
for coor in lines:
    if coor[0] == 'forward':
        hor += int(coor[1])
        dep2 += aim * int(coor[1])
    elif coor[0] == 'down':
        dep1 += int(coor[1])
        aim += int(coor[1])
    elif coor[0] == 'up':
        dep1 -= int(coor[1])
        aim -= int(coor[1])

res1 = hor * dep1
print(res1)

# res2 = 0
# hor = 0
# dep = 0
# aim = 0
# for coor in lines:
#     if coor[0] == 'forward':
#         hor += int(coor[1])
#     elif coor[0] == 'down':
#     elif coor[0] == 'up':

res2 = hor * dep2
print(res2)
