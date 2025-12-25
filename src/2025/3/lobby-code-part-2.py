
from lib import io


def main(problem_input) -> None:
    batteries = [[int(digit) for digit in line] for line in problem_input]
    # calculate result
    result = 0
    for row in batteries:
        best = [0] * 13
        for battery in row:
            for i in range(12):
                best[i] = max(best[i + 1] * 10 + battery, best[i])
        result += best[0]

    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/3/lobby-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
