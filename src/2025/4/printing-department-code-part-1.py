
from lib import io, grid


def main(problem_input) -> None:
    # process input
    graph = grid.Grid(problem_input)
    # calculate result
    rolls: list[grid.Loc] = graph.findall("@")
    adjacent_rolls = [list(filter(lambda x: graph.get(x) == "@", roll.all_adjacents())) for roll in rolls]
    result = len([roll for roll in adjacent_rolls if len(roll) < 4])
    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/4/printing-department-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
