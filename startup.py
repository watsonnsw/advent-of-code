import os
import subprocess
import sys

import requests
from bs4 import BeautifulSoup

from constants import (
    CALCULATE_RESULT_MARKER,
    DEFAULT_INPUT_PROCESSING,
    OPEN_FILE,
    OVERWRITE_QUERY,
    PROCESS_INPUT_MARKER,
    PROCESSING_QUERY,
    SAME_INPUT_TEXT,
    TEMPLATE,
    YEAR,
)
from session_cookie import SESSION_COOKIE


class Startup:
    def __init__(self):
        self.day = sys.argv[1]
        self.session = requests.Session()
        self.session.cookies.set("session", SESSION_COOKIE)
        self._create_directories_if_nonexistent()

    def get_question_info(self) -> None:
        response = self.session.get(f"https://adventofcode.com/{YEAR}/day/{self.day}")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, features="lxml")
        title = soup.h2.contents[0]
        self.problem_name: str = title[title.find(":") + 2 : -4]
        self.problem_path_name = self.problem_name.lower().replace(" ", "-")
        self.part = len(soup.findAll("h2"))
        self.same_input = SAME_INPUT_TEXT in response.text
        self.code_file_name = f"{YEAR}/{self.day}/{self.problem_path_name}-code-part-{self.part}.py"
        print(f"You are on part {self.part} of question {self.problem_name} ({YEAR} day {self.day})")

    def set_up_workspace(self) -> None:
        self.get_question_info()
        if not self.same_input:
            self.download_and_store_input()
        self.create_and_open_code_file()

    @property
    def input_file_name(self) -> str:
        base_file_name = f"{YEAR}/{self.day}/input/{self.problem_path_name}-input-part-{{part}}.txt"
        if self.same_input:
            for part in range(self.part - 1, -1, -1):
                potential_input_file = base_file_name.format(part=part)
                if os.path.exists(potential_input_file):
                    return potential_input_file
            raise ValueError("No previous input file found")
        return base_file_name.format(part=self.part)

    @property
    def prior_code_file_name(self) -> str:
        if self.part <= 1:
            raise ValueError("No previous part")
        return f"{YEAR}/{self.day}/{self.problem_path_name}-code-part-{self.part - 1}.py"

    def _get_previous_input_processing_code(self) -> str:
        lines = []
        with open(file=self.prior_code_file_name, mode="r") as f:
            copy = False
            for line in f.readlines():
                if PROCESS_INPUT_MARKER in line:
                    copy = True
                elif CALCULATE_RESULT_MARKER in line:
                    break
                elif copy:
                    lines.append(line)
        return "".join(lines)

    def _create_directories_if_nonexistent(self) -> None:
        if not os.path.isdir(f"{YEAR}/{self.day}/input"):
            print("Creating directory")
            os.makedirs(f"{YEAR}/{self.day}/input")

    def download_and_store_input(self) -> None:
        response = self.session.get(f"https://adventofcode.com/{YEAR}/day/{self.day}/input")
        response.raise_for_status()
        with open(file=self.input_file_name, mode="w") as f:
            f.write(response.text)

    def create_and_open_code_file(self) -> None:
        if os.path.exists(self.code_file_name):
            decision = input(OVERWRITE_QUERY)
            if decision != "y":
                print("Exiting.")
                return

        if self.same_input or (self.part > 1 and input(PROCESSING_QUERY) == "y"):
            processing_code = self._get_previous_input_processing_code()
        else:
            processing_code = DEFAULT_INPUT_PROCESSING

        with open(file=self.code_file_name, mode="w") as f:
            f.write(
                TEMPLATE.format(
                    input_file_name=self.input_file_name,
                    input_processing=processing_code,
                )
            )
        subprocess.run(OPEN_FILE + [self.code_file_name])


def main():
    startup = Startup()
    startup.set_up_workspace()


if __name__ == "__main__":
    main()
