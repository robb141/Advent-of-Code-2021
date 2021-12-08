import down
import os

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    nums = f.read().split(',')

nums = [int(x) for x in nums]
print(nums)

D = dict((el, 0) for el in nums)


def calc_fish(days, start=None):
    if days <= 7:
        return 1
    r = 0
    r += 1
    range_from = 0 if start else 7
    days_left = days - start if start else days - 2
    for j in range(range_from, days_left, 7):
        r += calc_fish(days_left - j)
    return r


res1 = 0
day = 80
for i in nums:
    if not D[i]:
        D[i] = calc_fish(day, i)
    res1 += D[i]

print(f'Part 1: {res1}')


res2 = [0] * 9
for num in nums:
    res2[num] += 1

for day in range(256):
    new_fish = res2.pop(0)
    res2.append(new_fish)
    res2[6] += new_fish

print(f'Part 2: {sum(res2)}')



