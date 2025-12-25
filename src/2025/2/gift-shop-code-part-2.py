
from lib import io


def main(problem_input) -> None:
    # process input
    ranges = [r.split("-") for r in problem_input[0].split(",")]
    # calculate result
    result = 0
    for low, high in ranges:
        l, h = int(low), int(high)
        counted = set()
        for repeat in range(2, len(high) + 1):
            if len(low) % repeat:
                start = pow(10, len(low) // repeat)
            else:
                start = int(low[:len(low) // repeat])
            if len(high) % repeat:
                end = int("9" * (len(high) // repeat))
            else:
                end = int(high[:len(high) // repeat])
            for num in range(start, end + 1):
                full_num = int(str(num) * repeat)
                if full_num > h:
                    break
                if full_num >= l and full_num not in counted:
                    result += full_num
                    counted.add(full_num)
    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/2/gift-shop-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
