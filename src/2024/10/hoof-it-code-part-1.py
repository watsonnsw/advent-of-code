from lib import io
from lib.grid import Dir, Grid


def main(problem_input) -> None:
    # process input
    grid = Grid(problem_input)
    # calculate result
    prev = {location: set([location]) for location in grid.findall("9")}
    for n in range(8, -1, -1):
        cur = {}
        for location in grid.findall(str(n)):
            score = set()
            for d in Dir.ALL:
                score |= prev.get(location + d, set())
            cur[location] = score
        prev = cur
    result = sum([len(s) for s in prev.values()])

    # print result
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/10/hoof-it-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
