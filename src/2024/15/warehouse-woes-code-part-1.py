
from lib import io
from lib.grid import Grid, get_dir


def main(problem_input) -> None:
    # process input
    board, inputs = problem_input.split("\n\n")
    grid = Grid(problem_input=board.splitlines())
    # calculate result
    result = 0
    cur = grid.find("@")
    print(grid)
    for input in inputs:
        if input.isspace():
            continue
        direction = get_dir(input)
        next_loc = cur + direction
        if grid[next_loc] == "#":
            continue
        if grid[next_loc] == "O":
            box_loc = next_loc
            while grid[box_loc] == "O":
                box_loc = box_loc + direction
            if grid[box_loc] == "#":
                continue
            grid[box_loc] = "O"
        grid[cur] = "."
        grid[next_loc] = "@"
        cur = next_loc
    
    for i, j in grid.findall("O"):
        result += 100 * i + j

    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2024/15/warehouse-woes-input.txt", "r") as f:
        file_text = f.read()
        main(file_text)
