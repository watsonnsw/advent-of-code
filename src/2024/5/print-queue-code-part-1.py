from collections import defaultdict


def main(problem_input: str) -> None:
    # process input
    graph = defaultdict(set)
    pages = []
    for line in problem_input.splitlines():
        if "|" in line:
            first, second = line.split("|")
            graph[second].add(first)
        elif "," in line:
            pages.append(line.split(","))

    # calculate result
    def is_sorted(page: list[str]) -> bool:
        unusable_vertices = set()
        for vertex in page:
            # if this vertex was supposed to appear earlier, we aren't sorted
            if vertex in unusable_vertices:
                return False
            # otherwise, add earlier vertices to our unusable list
            unusable_vertices |= graph[vertex]
        return True

    result = 0
    for page in pages:
        # if our page is sorted, add it to the result
        if is_sorted(page):
            result += int(page[len(page) // 2])

    # print result
    print(result)


if __name__ == "__main__":
    with open("2024/5/input/print-queue-input-part-1.txt", "r") as f:
        main(f.read())
