
from collections import deque
from lib import io
from lib.grid import Dir, Grid, GridDfs


def main(problem_input) -> None:
    # process input
    grid = Grid(problem_input)
    # calculate result
    result = 0
    def grid_bfs(start):
        nonlocal grid, seen
        queue = deque([(start, Dir.U)])
        area, perim, target = 0, set(), grid[start]
        while queue:
            location, direction = queue.popleft()
            if location not in grid or grid[location] != target:
                perim.add((location, direction))
                continue
            if location in seen:
                continue
            seen.add(location)
            area += 1
    
            for direction in Dir.ALL:
                queue.append((location + direction, direction))
        sides = 0
        seen_perim = set()
        for loc, d in perim:
            if (loc, d) in seen_perim:
                continue
            sides += 1
            forward = d.rotate_clockwise()
            back = d.rotate_counterclockwise()
            cur = loc
            while (cur, d) in perim:
                seen_perim.add((cur, d))
                cur = cur + forward
            curr = loc + back
            while (curr, d) in perim:
                seen_perim.add((curr, d))
                curr = curr + back
        return area * sides


    for value in grid.valueset():
        seen = set()
        for location in grid.findall(value):
            result += grid_bfs(start=location)

    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2024/12/garden-groups-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
