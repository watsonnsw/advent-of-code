
from lib import io
from lib.grid import Dir, Grid, get_dir


def main(problem_input) -> None:
    # process input
    board, inputs = problem_input.split("\n\n")
    board = board.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    grid = Grid(problem_input=board.splitlines())
    # calculate result
    result = 0
    def move_if_valid(locations, direction):
        if not locations:
            return True
        next_locations = [location + direction for location in locations]
        locations_to_check = set()
        for next_location in next_locations:
            if grid[next_location] == "#":
                return False
            if grid[next_location] in ["[", "]"]:
                locations_to_check.add(next_location)
                if direction in [Dir.U, Dir.D]:
                    if grid[next_location] == f"[":
                        locations_to_check.add(next_location + Dir.R)
                    else:
                        locations_to_check.add(next_location + Dir.L)
        if success := move_if_valid(locations_to_check, direction):
            for location in locations:
                grid[location + direction] = grid[location]
                grid[location] = "."
        return success

    cur = grid.find("@")
    for input in inputs:
        if input.isspace():
            continue
        direction = get_dir(input)
        if move_if_valid(set([cur]), direction):
            cur = cur + direction
        
    for i, j in grid.findall("["):
        result += 100 * i + j

    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2024/15/warehouse-woes-input.txt", "r") as f:
        file_text = f.read()
        main(file_text)
