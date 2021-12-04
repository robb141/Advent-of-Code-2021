import down
import os
from collections import defaultdict

with open(f'{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    lines = f.read().splitlines()


nums = list(map(int, lines[0].split(',')))
boards = [lines[x+2:x+2+5] for x in range(0, len(lines[2:]), 6)]

# Make list (boards) of lists (board) of lists (rows of board) of integers
for i in range(len(boards)):
    boards[i] = [k.split() for k in boards[i]]
    for b in range(len(boards[i])):
        boards[i][b] = list(map(int, boards[i][b]))


class Board:
    def __init__(self, board):
        self.board = board
        self.marked = []
        self.row_dict = defaultdict(int)
        self.col_dict = defaultdict(int)

    def add_num(self, num):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == num:
                    self.marked.append((row, col))
                    self.row_dict[row] += 1
                    self.col_dict[col] += 1
                    return self.check_win()
        return False

    def show_marked(self):
        return self.marked

    def show_board(self):
        return self.board

    def check_win(self):
        if len(self.marked) > 4:
            if max(self.row_dict.values()) == 5:
                return True
            elif max(self.col_dict.values()) == 5:
                return True
        return False

    def calculate_win(self, num):
        total = 0
        for g in range(len(self.board)):
            for h in range(len(self.board)):
                total += self.board[g][h] if (g, h) not in self.marked else 0
        return total * num


objs = [Board(i) for i in boards]
win_obj = []

for n in nums:
    for obj in objs:
        if obj not in win_obj and obj.add_num(n):
            win_obj.append(obj)

            if len(win_obj) == 1:
                print(f'Part1: {obj.calculate_win(n)}')

            if len(objs) == len(win_obj):
                print(f'Part2: {obj.calculate_win(n)}')
                break
    else:
        continue
    break
