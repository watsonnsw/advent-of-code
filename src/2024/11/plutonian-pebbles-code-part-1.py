from lib import io


def main(problem_input) -> None:
    # process input
    stones = io.intify(problem_input)

    # calculate result
    def rec(stone, steps):
        if steps == 0:
            return 1
        if stone == 0:
            return rec(1, steps - 1)
        s = str(stone)
        if len(s) % 2 == 0:
            halfway = len(s) // 2
            return rec(int(s[:halfway]), steps - 1) + rec(int(s[halfway:]), steps - 1)
        return rec(stone * 2024, steps - 1)

    result = sum([rec(stone, 25) for stone in stones])

    # print result
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/11/plutonian-pebbles-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.split())
