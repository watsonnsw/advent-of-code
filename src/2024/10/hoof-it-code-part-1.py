from lib import io
from lib.grid import Grid, GridDfs


def main(problem_input) -> None:
    # process input
    grid = Grid(problem_input)
    print(grid)
    # calculate result
    dfs = GridDfs(grid)
    result = dfs.search()
    # print result
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/10/hoof-it-input.txt", "r") as f:
        file_text = f.read()
        file_text = """AAAA
BBCD
BBCC
EEEC"""
        main(file_text.splitlines())
