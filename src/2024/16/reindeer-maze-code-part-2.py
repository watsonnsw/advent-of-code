from functools import cache
from lib import io
from heapq import heapify, heappop, heappush
from lib.grid import Dir, Grid, Loc


def main(problem_input) -> None:
    # process input
    grid = Grid(problem_input)

    # calculate result
    seen = {}
    paths = set()

    @cache
    def search(location, direction, score):
        nonlocal seen, paths, grid
        if grid[location] == "E":
            paths.add(location)
            return True
        if grid[location] == "#" or score > seen.get((location, direction), 66404):
            return False
        seen[(location, direction)] = score
        res = search(location + direction, direction, score + 1)
        for dir in (direction.rotate_clockwise(), direction.rotate_counterclockwise()):
            if search(location + dir, dir, score + 1001):
                res = True
        if res:
            paths.add(location)
        return res

    search(grid.find("S"), Dir.R, 0)
    result = len(paths)
    # print result
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/16/reindeer-maze-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
