from collections import deque
from lib import io
from lib.grid import Dir, Grid


def main(problem_input) -> None:
    # process input
    grid = Grid(problem_input)
    # calculate result
    result = 0

    def grid_bfs(start):
        nonlocal grid, seen
        queue = deque([start])
        target = grid[start]
        area, perim = 0, 0
        while queue:
            location = queue.popleft()
            if location not in grid or grid[location] != target:
                perim += 1
                continue
            if location in seen:
                continue
            seen.add(location)
            area += 1

            for direction in Dir.ALL:
                queue.append(location + direction)
        return area * perim

    for value in grid.valueset():
        seen = set()
        for location in grid.findall(value):
            result += grid_bfs(location)
    # print result
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/12/garden-groups-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
