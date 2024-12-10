import re


def main(problem_input: str) -> None:
    # process input
    regex_string = problem_input

    # calculate result
    result = 0
    # simple regex using groups to isolate ints
    matches = re.findall(pattern="mul\\(([0-9]+),([0-9]+)\\)", string=regex_string)
    for match in matches:
        result += int(match[0]) * int(match[1])

    # print result
    print(result)


if __name__ == "__main__":
    with open("2024/3/input/mull-it-over-input-part-1.txt", "r") as f:
        main(f.read())
