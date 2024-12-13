from collections import deque
from typing import Self, SupportsIndex


class Loc(tuple):
    def __new__(cls, *args):
        if len(args) == 1:
            return super(Loc, cls).__new__(cls, (args[0][0], args[0][1]))
        return super(Loc, cls).__new__(cls, (args[0], args[1]))

    def rotate_clockwise(self) -> Self:
        return Loc(self[1], -self[0])

    def rotate_counterclockwise(self) -> Self:
        return Loc(-self[1], self[0])

    def flip(self) -> Self:
        return Loc(-self[1], -self[0])

    def __add__(self, other) -> Self:
        return Loc(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other) -> Self:
        return Loc(self[0] - other[0], self[1] - other[1])
    
    def __ge__(self, other) -> bool:
        return self[0] >= other[0] or self[1] >= other[1]
    
    def __mul__(self, value: int) -> tuple:
        return Loc(self[0] * value, self[1] * value)


class Dir:
    U = Loc(-1, 0)
    D = Loc(1, 0)
    R = Loc(0, 1)
    L = Loc(0, -1)
    ALL = [U, D, R, L]


class Grid(dict):
    def __init__(self, problem_input: str) -> None:
        self.m = len(problem_input)
        self.n = len(problem_input[0])
        for i, line in enumerate(problem_input):
            for j, c in enumerate(line.strip()):
                self[Loc(i, j)] = c

    def find(self, target_value):
        for key, value in self.items():
            if value == target_value:
                return key
        return None

    def findall(self, target_value):
        keys = []
        for key, value in self.items():
            if value == target_value:
                keys.append(key)
        return keys

    def __str__(self) -> str:
        res = []
        for i in range(self.m):
            line = []
            for j in range(self.n):
                line.append(self[(i, j)])
            res.append("".join(line))
        return "\n".join(res)

    def rows(self):
        return range(self.m)

    def cols(self):
        return range(self.n)

    def valueset(self):
        result = set()
        for values in self.values():
            result |= set(values)
        return result

    def get_row(self, row: int):
        return [self[Loc(row, col)] for col in self.cols()]

    def get_col(self, col: int):
        return [self[Loc(row, col)] for row in self.rows()]
