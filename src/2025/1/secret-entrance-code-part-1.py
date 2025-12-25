
from lib import io


def main(problem_input) -> None:
    result = 0
    ring_size = 100
    location = 50
    for line in problem_input:
        steps = int(line[1:])
        if line[0] == "L":
            steps *= -1
        location += steps
        location %= ring_size
        if location == 0:
            result += 1
    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/1/secret-entrance-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
