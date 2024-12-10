
def main(problem_input: str) -> None:
    # process input
    equations = []
    for line in problem_input.splitlines():
        total, nums = line.split(":")
        equations.append((int(total), list(map(int, nums.split()))))


    # calculate result
    result = 0
    for total, nums in equations:
        def test(index, cum):
            if index == len(nums):
                return cum == total
            if cum > total:
                return False
            n = nums[index]
            return test(index + 1, cum * n) or test(index + 1, cum + n) or test(index + 1, int(str(cum) + str(n)))
        if test(1, nums[0]):
            result += total

    # print result
    print(result)

if __name__ == "__main__":
    with open("2024/7/bridge-repair-input", "r") as f:
        main(f.read())
