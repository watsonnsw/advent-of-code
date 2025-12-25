
from lib import io


def main(problem_input) -> None:
    # process input
    ranges = [r.split("-") for r in problem_input[0].split(",")]
    # calculate result
    result = 0
    for low, high in ranges:
        if len(low) % 2:
            start = pow(10, len(low) // 2)
            lower_bound = 0
        else:
            start = int(low[:len(low) // 2])
            lower_bound = int(low[len(low) // 2:])
        if len(high) % 2:
            end = int("9" * (len(high) // 2))
            upper_bound = int("9" * (len(high) // 2))
        else:
            end = int(high[:len(high) // 2])
            upper_bound = int(high[len(high) // 2:])
        for num in range(start, end + 1):
            if (num > start or num >= lower_bound) and (num < end or num <= upper_bound):
                result += int(str(num) * 2)
    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/2/gift-shop-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
