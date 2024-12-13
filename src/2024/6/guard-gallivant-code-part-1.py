from lib.grid import Grid, Loc, Dir


def main(problem_input: str) -> None:
    # process input
    grid = Grid(problem_input)
    # calculate result
    cur = Loc(grid.find("^"))  # find the starting position
    dir = Dir.U  # start facing upward
    seen = set()
    while cur in grid:
        seen.add(cur)
        # rotate as long as we hit an obstacle
        while (new_loc := cur + dir) in grid and grid[new_loc] == "#":
            dir = dir.rotate_clockwise()
        cur = new_loc
    result = len(seen)

    # print result
    print(result)


if __name__ == "__main__":
    with open("2024/6/input/guard-gallivant-input-part-1.txt", "r") as f:
        main(f.read())
