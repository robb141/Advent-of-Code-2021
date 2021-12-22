import down
import os
from functools import lru_cache

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().splitlines()


p1 = int(lines[0].split()[-1])
p2 = int(lines[1].split()[-1])
rolls = 0


def roll_dice(player, score):
    global rolls
    player = (player + sum(range(rolls+1, rolls + 4))) % 10 if (player + sum(range(rolls+1, rolls + 4))) % 10 != 0 else 10
    score += player
    rolls += 3
    return player, score


def end_rolls(s1, s2):
    global rolls
    if s1 >= 1000:
        print(f'Part 1: {s2*rolls}')
        return True


def play1(p1, p2):
    score1 = 0
    score2 = 0
    while True:
        p1, score1 = roll_dice(p1, score1)
        if end_rolls(score1, score2):
            break

        p2, score2 = roll_dice(p2, score2)
        if end_rolls(score2, score1):
            break


play1(p1, p2)

quantum_rolls = []
for die1 in range(1, 4):
    for die2 in range(1, 4):
        for die3 in range(1, 4):
            quantum_rolls.append(die1 + die2 + die3)
p1 -= 1
p2 -= 1


@lru_cache(maxsize=None)
def play2(my_pos, my_score, other_pos, other_score):
    if my_score >= 21:
        return 1, 0
    if other_score >= 21:
        return 0, 1

    my_wins = other_wins = 0

    for roll in quantum_rolls:
        new_pos = (my_pos + roll) % 10
        new_score = my_score + new_pos + 1

        ow, mw = play2(other_pos, other_score, new_pos, new_score)

        my_wins += mw
        other_wins += ow

    return my_wins, other_wins


wins = play2(p1, 0, p2, 0)
best = max(wins)

print(f'Part 2: {best}')


