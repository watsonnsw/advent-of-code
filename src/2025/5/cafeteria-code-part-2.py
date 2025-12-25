
from heapq import heapify, heappop, heappush
from lib import io


def main(problem_input) -> None:
    # process input
    queue = []
    for line in problem_input:
        if "-" in line:
            start, end = map(int, line.split("-"))
            queue.append((start, -1))
            queue.append((end, 1))
    queue.sort()
    # calculate result
    result = 0
    status = 0
    first_ingredient = 0
    for ingredient, event_type in queue:
        if status == 0:
            first_ingredient = ingredient
        status -= event_type
        if status == 0:
            result += ingredient - first_ingredient + 1
    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/5/cafeteria-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
