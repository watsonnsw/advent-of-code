
from lib import io
import re

from lib.grid import Loc

def main(problem_input) -> None:
    # process input
    pattern = r"""Button A: X\+(\d*), Y\+(\d*)
Button B: X\+(\d*), Y\+(\d*)
Prize: X\=(\d*), Y\=(\d*)"""
    games = io.intify(re.findall(pattern, problem_input))
    # calculate result
    result = 0
    for ax, ay, bx, by, px, py in games:
        a_press = Loc(ax, ay)
        b_press = Loc(bx, by)
        prize = Loc(px, py)
        a_presses = 0
        b_presses = 0
        cur = Loc(0, 0)
        cost = 0
        while cur < prize:
            a_presses += 1
            cur = cur + a_press
        if cur == prize:
            cost = 3 * a_presses
        while a_presses:
            a_presses -= 1
            cur = cur - a_press
            while cur < prize:
                b_presses += 1
                cur = cur + b_press
            if cur == prize:
                current_cost = 3 * a_presses + b_presses
                if cost:
                    cost = min(cost, current_cost)
                else:
                    cost = current_cost
        result += cost

    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2024/13/claw-contraption-input.txt", "r") as f:
        file_text = f.read()
        main(file_text)
