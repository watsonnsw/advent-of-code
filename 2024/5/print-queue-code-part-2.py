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
    result = 0

    def is_sorted(page: list[str]) -> bool:
        unusable_vertices = set()
        for vertex in page:
            # if this vertex was supposed to appear earlier, we aren't sorted
            if vertex in unusable_vertices:
                return False
            # otherwise, add earlier vertices to our unusable list
            unusable_vertices |= graph[vertex]
        return True

    # lazy toposort taking advantage of no cycles and everything being fixed
    def toposort(page: list[str]) -> list[str]:
        sorted_list = []
        unsorted_vertices = set(page)
        # create a subgraph using only the vertices on the page
        subgraph = {v: {w for w in graph[v] if w in unsorted_vertices} for v in page}
        while unsorted_vertices:
            for v in unsorted_vertices:
                # if there are no remaining vertices that need to come before, we can add it
                if not subgraph[v]:
                    sorted_list.append(v)
                    # then we just have to clean it out of the remaining sets of the graph
                    unsorted_vertices.remove(v)
                    for unusable in subgraph.values():
                        unusable.discard(v)
                    # not sure if this is necessary but w/e
                    break
        return sorted_list

    for page in pages:
        if is_sorted(page):
            continue
        # sort the page and add the sorted page's middle to the result
        sorted_page = toposort(page)
        result += int(sorted_page[len(page) // 2])

    # print result
    print(result)


if __name__ == "__main__":
    with open("2024/5/input/print-queue-input-part-1.txt", "r") as f:
        main(f.read())
