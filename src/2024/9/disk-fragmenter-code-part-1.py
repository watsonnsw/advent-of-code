from lib import io


def main(problem_input) -> None:
    # process input
    block_list = io.intify(list(problem_input))

    # calculate result
    result = 0
    files = block_list[::2]
    gaps = block_list[1::2]
    gaps.reverse()
    gaps.append(0)
    file_to_move = len(files) - 1
    file_skipped = 0
    overall_index = 0

    def get_score(start_index, fill_length):
        return sum(range(start_index, start_index + fill_length))

    while file_to_move > file_skipped:
        file_length = files[file_to_move]
        while file_length:
            gap = gaps.pop()
            filled = min(gap, file_length)
            result += file_to_move * get_score(overall_index, filled)
            overall_index += filled
            file_length -= filled
            if file_length:
                skipped_length = files[file_skipped]
                if file_skipped == file_to_move:
                    skipped_length = file_length
                result += file_skipped * get_score(overall_index, skipped_length)
                overall_index += skipped_length
                file_skipped += 1
                if file_skipped > file_to_move:
                    break
            else:
                gaps.append(gap - filled)
        file_to_move -= 1

    # print result
    io.copy_result(result)


if __name__ == "__main__":
    with open("2024/9/disk-fragmenter-input.txt", "r") as f:
        file_text = f.read()
        main(file_text)
