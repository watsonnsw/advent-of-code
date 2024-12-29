from lib import io
from heapq import heapify, heappop, heappush
from lib.grid import Dir, Grid, Loc


def main(problem_input) -> None:
    # process input
    grid = Grid(problem_input)

    # calculate result
    seen = set()

    def grid_search(start):
        nonlocal grid, seen
        queue: list[Loc, Loc, int] = [start]
        heapify(queue)
        while queue:
            score, location, direction = heappop(queue)
            if grid[location] == "E":
                return score
            if grid[location] == "#":
                continue
            if (location, direction) in seen:
                continue
            seen.add((location, direction))
            for dir in (direction.rotate_clockwise(), direction.rotate_counterclockwise()):
                heappush(queue, (score + 1001, location + dir, dir))
            heappush(queue, (score + 1, location + direction, direction))

    result = grid_search((0, grid.find("S"), Dir.R))
    # print result
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/16/reindeer-maze-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
