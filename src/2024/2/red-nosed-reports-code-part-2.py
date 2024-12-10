from functools import cache


def main(problem_input: str) -> None:
    # process input
    levels = []
    for line in problem_input.splitlines():
        levels.append(list(map(int, line.split(" "))))

    # calculate result
    result = 0
    for level in levels:
        # custom dp function for each level - O(n) possible states
        @cache
        def dp(index: int, prev: int, skippable: bool, direction: bool | None) -> bool:
            # if we reach the end without issues we're good
            if index == len(level):
                return True
            # if we can skip, try skipping first
            if skippable and dp(index=index + 1, prev=prev, skippable=False, direction=direction):
                return True
            # test our conditions - we can't test if we have no previous value
            cur = level[index]
            if prev:
                # test gap size
                if not 1 <= abs(cur - prev) <= 3:
                    return False
                # if we haven't found a direction, set one
                if direction is None:
                    direction = cur > prev
                # otherwise test it
                elif (cur > prev) != direction:
                    return False

            # once tests are passed, continue on
            return dp(index=index + 1, prev=cur, skippable=skippable, direction=direction)

        # run the test
        if dp(index=0, prev=0, skippable=True, direction=None):
            result += 1

    # print result
    print(result)


if __name__ == "__main__":
    with open("2024/2/input/red-nosed-reports-input-part-1.txt", "r") as f:
        main(f.read())
