def main(problem_input: str) -> None:
    # process input
    l1, l2 = [], []
    for line in problem_input.splitlines():
        n1, n2 = line.split("   ")
        l1.append(int(n1))
        l2.append(int(n2))

    # calculate result
    result = sum([abs(n1 - n2) for n1, n2 in zip(sorted(l1), sorted(l2))])

    # print result
    print(result)


if __name__ == "__main__":
    with open("2024/1/input/historian-hysteria-input-part-1.txt", "r") as f:
        main(f.read())
