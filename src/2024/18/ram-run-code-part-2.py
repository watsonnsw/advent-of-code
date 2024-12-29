
from collections import deque
from lib import io
from lib.grid import Dir, Grid, Loc


def main(problem_input) -> None:
    # process input
    locations = []
    grid = Grid.blank_grid(dimensions=(71, 71))
    for line in problem_input:
        locations.append(Loc(io.intify(line.split(","))))

    # calculate result
    for index in range(1024):
        grid[locations[index]] = "#"
    seen = set()
    def grid_search(start):
        nonlocal grid, seen
        queue = deque([start])
        while queue:
            location, steps = queue.popleft()
            if location not in grid or grid[location] == "#":
                continue
            if location in seen:
                continue
            if location == (70, 70):
                return steps
            seen.add(location)
            for direction in Dir.ALL:
                queue.append((location + direction, steps + 1))
        return -1
    for index in range(1024, len(locations)):
        grid[locations[index]] = "#"
        seen = set()
        steps = grid_search((Loc(0, 0), 0))
        if steps == -1:
            result = locations[index]
            break
    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2024/18/ram-run-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
