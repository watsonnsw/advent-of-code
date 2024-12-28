from math import prod
from typing import Counter
from lib import io
import re

from lib.grid import Dir, Loc, Grid


def main(problem_input) -> None:
    # process input
    dimensions = Loc(103, 101)

    class Robot:
        def __init__(self, p, v) -> None:
            self.position = Loc(p)
            self.velocity = Loc(v)

        def move(self) -> None:
            self.position = self.position + self.velocity
            self.position = self.position % dimensions

        def get_quadrant(self) -> int:
            x, y = self.position
            midx, midy = dimensions // 2
            if x == midx or y == midy:
                return -1
            return int(x > midx) + 2 * int(y > midy)

    robots: list[Robot] = []
    for line in problem_input:
        match = re.search(pattern="p=([-0-9]+),([-0-9]+) v=([-0-9]+),([-0-9]+)", string=line)
        px, py, vx, vy = [match[index] for index in range(1, 5)]
        robots.append(Robot((py, px), (vy, vx)))

    # calculate result
    grid = Grid.blank_grid(dimensions)
    result = 0
    steps = 0
    while not result:
        for robot in robots:
            robot.move()
        steps += 1

        positions = set([robot.position for robot in robots])
        for location in positions:
            surrounded = True
            for direction in Dir.TOTAL:
                if location + direction not in positions:
                    surrounded = False
                    break
            if surrounded:
                result = steps
                break

    # print result
    grid = Grid.blank_grid(dimensions)
    for location in positions:
        grid[location] = "#"
    print(grid)
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/14/restroom-redoubt-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())