
from collections import deque
from typing import Self

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
                self[(i, j)] = c

    def find(self, target_value):
        for key, value in self.items():
            if value == target_value:
                return Loc(key)
        return None
    
    def findall(self, target_value):
        keys = []
        for key, value in self.items():
            if value == target_value:
                keys.append(Loc(key))
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


class GridDfs:
    def __init__(self, grid: Grid, start: Loc) -> None:
        self.grid = grid
        self.queue = deque()
        self.seen = set()
        self.queue.append((start, 0))

    def dfs(self): 
        while self.queue:
            location, distance = self.queue.popleft()
            if location not in self.grid:
                continue
            if location in self.seen:
                continue
            self.seen.add(location)
            item = self.grid[location]
            # edit logic here

            for dir in Dir.ALL:
                self.queue.append((location + dir, distance + 1))
