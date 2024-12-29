from lib import io


def main(problem_input) -> None:
    # process input
    program = [2, 4, 1, 2, 7, 5, 1, 3, 4, 4, 5, 5, 0, 3, 3, 0]

    # calculate result
    def loop(current_result: int, index: int) -> int:
        if index == -1:
            return current_result
        for i in range(8):
            possible_result = (current_result << 3) + i
            B = i ^ 2
            C = (possible_result >> B) % 8
            if B ^ 3 ^ C == program[index]:
                looped_result = loop(possible_result, index - 1)
                if looped_result:
                    return looped_result
        return 0

    result = loop(0, len(program) - 1)
    # print result
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/17/chronospatial-computer-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
