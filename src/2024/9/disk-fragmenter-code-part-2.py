from collections import defaultdict
from lib import io


def main(problem_input) -> None:
    # process input
    block_list = io.intify(list(problem_input.strip()))
    print(block_list)
    # calculate result
    result = 0
    files = []
    gaps = []
    overall_index = 0
    for index, block_size in enumerate(block_list):
        if index % 2:
            gaps.append([overall_index, block_size])
        else:
            files.append((overall_index, block_size))
        overall_index += block_size

    def get_score(start_index, fill_length):
        return sum(range(start_index, start_index + fill_length))

    for file_index in range(len(files) - 1, -1, -1):
        actual_index, file_size = files[file_index]
        for gap_index, (actual_gap_index, gap_size) in enumerate(gaps):
            if actual_gap_index > actual_index:
                result += get_score(actual_index, file_size) * file_index
                break
            if gap_size >= file_size:
                gaps[gap_index][0] += file_size
                gaps[gap_index][1] -= file_size
                result += get_score(actual_gap_index, file_size) * file_index
                break

    # print result
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/9/disk-fragmenter-input.txt", "r") as f:
        file_text = f.read()
        main(file_text)
