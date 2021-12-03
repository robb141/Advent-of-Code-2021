import down
import os
from collections import Counter


def fill_elem(element):
    if len(element) < len(lines[0]):
        return [j for j in lines if j.startswith(element)][0]
    return element


with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().splitlines()

print(lines)

most = ''
least = ''
oxygen = ''
co2 = ''

for i in range(len(lines[0])):
    # Part 1
    zero = 0
    one = 0
    list_of_elems = [str(x)[i] for x in lines]
    count_elems = Counter(list_of_elems)
    most += '0' if count_elems['1'] > count_elems['0'] else '1'

    # Part 2
    list_of_oxy = [str(x)[i] for x in lines if x.startswith(oxygen)]
    if len(list_of_oxy) > 1:
        count_oxy = Counter(list_of_oxy)
        oxygen += '1' if count_oxy['1'] >= count_oxy['0'] else '0'

    list_of_co2 = [str(x)[i] for x in lines if x.startswith(co2)]
    if len(list_of_co2) > 1:
        count_co2 = Counter(list_of_co2)
        co2 += '0' if count_co2['0'] <= count_co2['1'] else '1'

least = most.replace('1', 'T').replace('0', '1').replace('T', '0')
print(f'Part1: {(int(most, 2)) * (int(least, 2))}')
print(f'Part2: {(int(fill_elem(oxygen), 2)) * (int(fill_elem(co2), 2))}')
