
from heapq import heapify, heappop, heappush
from lib import io


def main(problem_input) -> None:
    # process input
    queue = []
    for line in problem_input:
        if not line:
            continue
        if "-" in line:
            start, end = map(int, line.split("-"))
            queue.append((start, -1))
            queue.append((end, 1))
        else:
            queue.append((int(line), 0))
    queue.sort()
    # calculate result
    result = 0
    status = 0
    for _, event_type in queue:
        status -= event_type
        if event_type == 0 and status > 0:
            result += 1
    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2025/5/cafeteria-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
