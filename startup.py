import os
import subprocess
import sys
import shutil
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
        self._create_directory_if_nonexistent()

    def get_question_info(self) -> None:
        response = self.session.get(f"https://adventofcode.com/{YEAR}/day/{self.day}")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, features="lxml")
        title = soup.h2.contents[0]
        self.problem_name: str = title[title.find(":") + 2 : -4]
        self.problem_path_name = self.problem_name.lower().replace(" ", "-")
        self.part = len(soup.findAll("h2"))
        self.code_file_name = f"{YEAR}/{self.day}/{self.problem_path_name}-code-part-{self.part}.py"
        self.input_file_name = f"{YEAR}/{self.day}/{self.problem_path_name}-input"
        print(f"You are on part {self.part} of question {self.problem_name} ({YEAR} day {self.day})")

    def set_up_workspace(self) -> None:
        self.get_question_info()
        if self.part == 1:
            self.download_and_store_input()
        self.create_and_open_code_file()

    @property
    def prior_code_file_name(self) -> str:
        if self.part <= 1:
            raise ValueError("No previous part")
        return f"{YEAR}/{self.day}/{self.problem_path_name}-code-part-{self.part - 1}.py"

    def _create_directory_if_nonexistent(self) -> None:
        if not os.path.isdir(f"{YEAR}/{self.day}/"):
            print("Creating directory")
            os.makedirs(f"{YEAR}/{self.day}/")

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

        if self.part > 1:
            shutil.copy(src=self.prior_code_file_name, dst=self.code_file_name)
        else:
            with open(file=self.code_file_name, mode="w") as f:
                f.write(
                    TEMPLATE.format(
                        input_file_name=self.input_file_name,
                        input_processing=DEFAULT_INPUT_PROCESSING,
                    )
                )
        subprocess.run(OPEN_FILE + [self.code_file_name])


def main():
    startup = Startup()
    startup.set_up_workspace()


if __name__ == "__main__":
    main()
