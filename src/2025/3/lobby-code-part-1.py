
from lib import io


def main(problem_input) -> None:
    batteries = [[int(digit) for digit in line] for line in problem_input]
    # calculate result
    result = 0
    for row in batteries:
        highest = 0
        best = 0
        for battery in row:
            best = max(best, highest * 10 + battery)
            highest = max(highest, battery)
        result += best

    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/3/lobby-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
