PROCESS_INPUT_MARKER = "# process input"
CALCULATE_RESULT_MARKER = "# calculate result"
PRINT_RESULT_MARKER = "# print result"
SAME_INPUT_TEXT = "<p>Although it hasn't changed, you can still"
OPEN_FILE = ["code"]
PROCESSING_QUERY = "Would you like to copy over the previous part's input processing code? (y/n)\n"
OVERWRITE_QUERY = "Code for this problem already exists. Would you like to overwrite it? (y/n)\n"
YEAR = "2024"
TEMPLATE = """
def main(problem_input: str) -> None:
    {process_input_marker}
{{input_processing}}
    {calculate_result_marker}
    result = 0

    {print_result_marker}
    print(result)

if __name__ == "__main__":
    with open("{{input_file_name}}", "r") as f:
        main(f.read())
""".format(
    process_input_marker=PROCESS_INPUT_MARKER,
    calculate_result_marker=CALCULATE_RESULT_MARKER,
    print_result_marker=PRINT_RESULT_MARKER,
)

DEFAULT_INPUT_PROCESSING = """
    for line in problem_input.splitlines():
        pass

"""
