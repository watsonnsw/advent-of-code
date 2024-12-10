
from lib.grid import Grid, Loc, Dir


def main(problem_input: str) -> None:
    # process input
    grid = Grid(problem_input)
    # calculate result
    cur = Loc(grid.find("^"))
    dir = Dir.U
    first_path = set()
    result = 0
    def get_next_location(current_location: Loc, direction: Loc) -> tuple[Loc, Loc]:
        while (new_location := current_location + direction) in grid and grid[new_location] == "#":
            direction = direction.rotate_clockwise()
        return new_location, direction
 
    while True:
        cur, dir = get_next_location(cur, dir)
        if cur in grid:
            first_path.add(cur)
        else:
            break

    for loc in first_path:
        grid[loc] = "#"
        seen = set()
        cur = Loc(grid.find("^"))
        dir = Dir.U
        while cur in grid:
            if (cur, dir) in seen:
                result += 1
                break
            seen.add((cur, dir))
            cur, dir = get_next_location(cur, dir)
        grid[loc] = "."

    # print result
    print(result)

if __name__ == "__main__":
    with open("2024/6/input/guard-gallivant-input-part-1.txt", "r") as f:
        main(f.read())
