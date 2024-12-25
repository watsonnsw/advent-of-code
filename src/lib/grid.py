import math
from typing import Iterator, Self


class Loc(tuple):
    def __new__(cls, *args):
        try:
            if len(args) == 1:
                x, y = args[0][0], args[0][1]
            else:
                x, y = args[0], args[1]
            return super(Loc, cls).__new__(cls, (int(x), int(y)))
        except:
            print(f"Could not create Loc from args: {args}")
            raise

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

    def __gt__(self, other) -> bool:
        return self[0] > other[0] or self[1] > other[1]

    def __mul__(self, value: int) -> Self:
        return Loc(self[0] * value, self[1] * value)

    def __floordiv__(self, value: int) -> Self:
        return Loc(self[0] // value, self[1] // value)

    def __neg__(self) -> Self:
        return Loc(-self[0], -self[1])

    def __mod__(self, other) -> Self:
        return Loc(self[0] % other[0], self[1] % other[1])

    def manhattan_dist(self, other=(0, 0)) -> int:
        return abs(self[0] - other[0]) + abs(self[1] - other[1])

    def dist(self, other=(0, 0)) -> float:
        return math.sqrt((self[0] - other[0]) ** 2 + (self[1] - other[1]) ** 2)

    def dir_char(self) -> str:
        match self:
            case x, y if abs(x) >= abs(y) and x < 0:
                return "^"
            case x, y if abs(x) >= abs(y) and x > 0:
                return "v"
            case x, y if abs(y) > abs(x) and y < 0:
                return "<"
            case x, y if abs(y) >= abs(x) and y > 0:
                return ">"


class Dir:
    U = Loc(-1, 0)
    D = Loc(1, 0)
    R = Loc(0, 1)
    L = Loc(0, -1)
    ALL = [U, D, R, L]
    UL = Loc(-1, -1)
    UR = Loc(-1, 1)
    DL = Loc(1, -1)
    DR = Loc(1, 1)
    DIAG = [UL, UR, DL, DR]
    TOTAL = [U, D, R, L, UL, UR, DL, DR]


def get_dir(char: str) -> Loc:
    match char:
        case "^":
            return Dir.U
        case "v":
            return Dir.D
        case ">":
            return Dir.R
        case "<":
            return Dir.L
        case _:
            raise ValueError(f"Couldn't process direction: {char}")


class Grid(dict):
    def __init__(self, problem_input: str) -> None:
        self.m = len(problem_input)
        self.n = len(problem_input[0])
        for i, line in enumerate(problem_input):
            for j, c in enumerate(line.strip()):
                self[Loc(i, j)] = c

    @classmethod
    def blank_grid(cls, dimensions, value=".") -> Self:
        m, n = dimensions
        grid = [value * n for _ in range(m)]
        return cls(grid)

    def find(self, target_value: str) -> Loc:
        for key, value in self.items():
            if value == target_value:
                return key
        return None

    def findall(self, target_value) -> list[Loc]:
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

    def rows(self) -> Iterator[int]:
        return range(self.m)

    def cols(self) -> Iterator[int]:
        return range(self.n)

    def valueset(self) -> set[str]:
        result = set()
        for values in self.values():
            result |= set(values)
        return result

    def get_row(self, row: int) -> list[str]:
        return [self[Loc(row, col)] for col in self.cols()]

    def get_col(self, col: int) -> list[str]:
        return [self[Loc(row, col)] for row in self.rows()]
