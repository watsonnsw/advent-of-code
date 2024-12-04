from itertools import product


def main(problem_input: str) -> None:
    # process input
    board = problem_input.splitlines()
    m = len(board)
    n = len(board[0])

    # calculate result
    result = 0

    # ugly helper but what can you do
    def is_mas(i, j):
        # why is this a separate check when the rest is one giant line? idk
        if board[i + 1][j + 1] != "A":
            return False
        goal = ("M", "S")
        # using sorting here was the best I could come up with on short notice
        return (
            tuple(sorted([board[i][j], board[i + 2][j + 2]])) == goal
            and tuple(sorted([board[i + 2][j], board[i][j + 2]])) == goal
        )

    # we can do the boundary check more easily in this part by just setting our ranges lower
    for i, j in product(range(m - 2), range(n - 2)):
        if is_mas(i, j):
            result += 1

    # print result
    print(result)


if __name__ == "__main__":
    with open("2024/4/input/ceres-search-input-part-1.txt", "r") as f:
        main(f.read())
