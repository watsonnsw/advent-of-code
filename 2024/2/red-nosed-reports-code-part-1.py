def main(problem_input: str) -> None:
    # process input
    levels = []
    for line in problem_input.splitlines():
        levels.append(list(map(int, line.split(" "))))

    # calculate result
    result = 0
    for level in levels:
        sorted_level = sorted(level)
        # check monotonicity very lazily
        if level != sorted_level:
            sorted_level.reverse()
            if level != sorted_level:
                continue
        # check gaps very lazily
        if all([1 <= abs(n1 - n2) <= 3 for n1, n2 in zip(level, level[1:])]):
            result += 1

    # print result
    print(result)


if __name__ == "__main__":
    with open("2024/2/input/red-nosed-reports-input-part-1.txt", "r") as f:
        main(f.read())
