
from math import prod
from lib import io


def main(problem_input: list[str]) -> None:
    op = None
    result = 0
    problem = 0
    for i in range(len(problem_input[0])):
        num = 0
        for line in problem_input:
            c = line[i]
            match c:
                case " ":
                    continue
                case "+":
                    op = sum
                    problem = 0
                case "*":
                    op = prod
                    problem = 1
                case _:
                    num *= 10
                    num += int(c)
        if not num:
            result += problem
            problem = 0
        else:
            problem = op((problem, num))
    result += problem
    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/6/trash-compactor-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
