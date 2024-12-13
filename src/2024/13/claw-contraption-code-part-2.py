
from lib import io
import re


def main(problem_input) -> None:
    # process input
    pattern = r"""Button A: X\+(\d*), Y\+(\d*)
Button B: X\+(\d*), Y\+(\d*)
Prize: X\=(\d*), Y\=(\d*)"""
    games = io.intify(re.findall(pattern, problem_input))
    # calculate result
    result = 0
    for ax, ay, bx, by, px, py in games:
        px += 10000000000000
        py += 10000000000000
        def greedy_calc_presses(fx, fy, sx, sy):
            f_presses = min(px // fx, py // fy)
            rx, ry = px - fx * f_presses, py - fy * f_presses
            if rx == ry == 0:
                return f_presses, 0
            num = rx * sy - sx * ry
            denom = fy * sx - fx * sy
            if num % denom:
                return None
            undone = num // denom
            s_presses = (rx + fx * undone) // sx
            f_presses -= undone
            if f_presses * fx + s_presses * sx != px:
                return None
            return f_presses, s_presses
        cost = 0
        if max_a_cost := greedy_calc_presses(ax, ay, bx, by):
            a_presses, b_presses = max_a_cost
            cost = 3 * a_presses + b_presses
        if max_b_cost := greedy_calc_presses(bx, by, ax, ay):
            b_presses, a_presses = max_b_cost
            maybe_cost = 3 * a_presses + b_presses
            if not cost:
                cost = maybe_cost
            else:
                cost = min(cost, maybe_cost)
        result += cost

    # print result
    io.copy_result(result)

if __name__ == "__main__":
    with open("2024/13/claw-contraption-input.txt", "r") as f:
        file_text = f.read()
        main(file_text)
