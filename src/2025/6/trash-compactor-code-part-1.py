
from math import prod
from lib import io


def main(problem_input: list[str]) -> None:
    # process input
    arrs = None
    for line in problem_input:
        nums = line.split()
        if arrs is None:
            arrs = [[] for _ in range(len(nums))]
        for i, num in enumerate(nums):
            arrs[i].append(num)
    # calculate result
    result = 0
    for arr in arrs:
        op = arr.pop()
        if op == "+":
            result += sum(map(int, arr))
        else:
            result += prod(map(int, arr))
    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/6/trash-compactor-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
