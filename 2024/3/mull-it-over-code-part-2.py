import re


def main(problem_input: str) -> None:
    # calculate result
    result = 0
    # we don't even need regex to handle the dos and don'ts - just split
    for code_block in problem_input.split("do()"):
        # anything after the first don't is deactivated
        active_block = code_block.split("don't()")[0]
        # then the rest is the same as part 1
        matches = re.findall(pattern="mul\\(([0-9]+),([0-9]+)\\)", string=active_block)
        for match in matches:
            result += int(match[0]) * int(match[1])

    # print result
    print(result)


if __name__ == "__main__":
    with open("2024/3/input/mull-it-over-input-part-1.txt", "r") as f:
        main(f.read())
