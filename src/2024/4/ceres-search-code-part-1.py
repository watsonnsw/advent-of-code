from itertools import product


def main(problem_input: str) -> None:
    # process input
    board = problem_input.splitlines()
    m = len(board)
    n = len(board[0])

    # calculate result
    def is_xmas(i, j, di, dj):
        # boundary check within the check function to be lazy
        if not 0 <= i + 3 * di < m or not 0 <= j + 3 * dj < n:
            return False
        for d in range(4):
            if board[i + d * di][j + d * dj] != "XMAS"[d]:
                return False
        return True

    result = 0
    # love using product for 2D array problems
    for di, dj in product([-1, 0, 1], [-1, 0, 1]):
        # skip the degenerate case
        if di == dj == 0:
            continue
        for i, j in product(list(range(m)), list(range(n))):
            if is_xmas(i, j, di, dj):
                result += 1

    # print result
    print(result)


if __name__ == "__main__":
    with open("2024/4/input/ceres-search-input-part-1.txt", "r") as f:
        main(f.read())
