
from lib import io, grid


def main(problem_input) -> None:
    # process input
    graph = grid.Grid(problem_input)
    # calculate result
    initial_rolls = len(graph.findall("@"))
    while True:
        rolls: list[grid.Loc] = graph.findall("@")
        if not rolls:
            break
        adjacent_rolls = [(roll, list(filter(lambda x: graph.get(x) == "@", roll.all_adjacents()))) for roll in rolls]
        removeable_rolls = [roll for roll, adjacents in adjacent_rolls if len(adjacents) < 4]
        for roll in removeable_rolls:
            graph[roll] = "."
        if not removeable_rolls:
            break
    result = initial_rolls - len(graph.findall("@"))
    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/4/printing-department-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
