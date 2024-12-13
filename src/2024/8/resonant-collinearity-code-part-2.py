from lib import io
from lib.grid import Grid


def main(problem_input) -> None:
    # process input
    grid = Grid(problem_input)

    # calculate result
    antinodes = set()
    for node_type in grid.valueset():
        if node_type == "." or node_type.isspace():
            continue
        node_locations = grid.findall(target_value=node_type)
        for index, loc1 in enumerate(node_locations):
            for loc2 in node_locations[index + 1 :]:
                dloc = loc2 - loc1
                cur = loc2
                while cur in grid:
                    antinodes.add(cur)
                    cur = cur + dloc
                cur = loc1
                while cur in grid:
                    antinodes.add(cur)
                    cur = cur - dloc
    result = len(antinodes)

    # print result
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/8/resonant-collinearity-input.txt", "r") as f:
        main(f.readlines())
