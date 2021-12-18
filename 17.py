import down
import os

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read()

# x_range could look like [20, 30]
x_range = [int(x) for x in lines.split('=')[1].split(',')[0].split('..')]
y_range = [int(x) for x in lines.split('=')[2].split('..')]

biggest = 0
initial_vel = 0
for i in range(1, 150):
    for j in range(-165, 1000):
        flag = False
        start = (0, 0)
        x_velocity = i
        y_velocity = j
        temp = y_velocity
        while True:
            start = (start[0] + x_velocity, start[1] + y_velocity)
            if x_range[0] <= start[0] <= x_range[1] and y_range[0] <= start[1] <= y_range[1]:
                flag = True
            x_velocity = x_velocity if x_velocity == 0 else x_velocity - 1
            y_velocity -= 1
            if y_velocity == 0:
                temp = start[1]
            if start[1] < y_range[0]:
                break
        if flag:
            initial_vel += 1
            biggest = max(biggest, temp)

print(f'Part 1 of this very ugly solution: {biggest}')
print(f'Part 2 of this very ugly solution: {initial_vel}')
