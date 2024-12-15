
from collections import Counter
from lib import io


def main(problem_input) -> None:
    # process input
    stones = io.intify(problem_input)
    # calculate result
    stone_counter = Counter(stones)
    for _ in range(75):
        next_stones = Counter()
        for stone, count in stone_counter.items():
            if stone == 0:
                next_stones[1] += count
                continue
            s = str(stone)
            halfway, odd = divmod(len(s), 2)
            if not odd:
                next_stones[int(s[:halfway])] += count
                next_stones[int(s[halfway:])] += count
                continue
            next_stones[stone * 2024] += count
        stone_counter = next_stones
    result = sum(stone_counter.values())

    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2024/11/plutonian-pebbles-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.split())
