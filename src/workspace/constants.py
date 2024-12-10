PROCESS_INPUT_MARKER = "# process input"
CALCULATE_RESULT_MARKER = "# calculate result"
PRINT_RESULT_MARKER = "# print result"
OPEN_FILE = ["code"]
OVERWRITE_QUERY = "Code for this problem already exists. Would you like to overwrite it? (y/n)\n"
YEAR = "2024"
TEMPLATE = """
from lib import io


def main(problem_input) -> None:
    {process_input_marker}
{{input_processing}}
    {calculate_result_marker}
    result = 0

    {print_result_marker}
    io.copy_result(result)

if __name__ == "__main__":
    with open("{{input_file_name}}", "r") as f:
        main(f.readlines())
""".format(
    process_input_marker=PROCESS_INPUT_MARKER,
    calculate_result_marker=CALCULATE_RESULT_MARKER,
    print_result_marker=PRINT_RESULT_MARKER,
)

DEFAULT_INPUT_PROCESSING = ""
