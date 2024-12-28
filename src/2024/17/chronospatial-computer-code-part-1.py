
from lib import io


def main(problem_input) -> None:
    # process input
    register: dict[str, int] = {}
    for line in problem_input:
        if line:
            first, second = line.split(": ")
        if line.startswith("Register"):
            register[first[-1]] = int(second)
        elif line.startswith("Program"):
            program = io.intify(second.split(","))
    # calculate result
    result = []
    instruction_pointer = 0
    def combo(op: int) -> int:
        if 4 <= op <= 6:
            return register[chr(ord("A") + op - 4)]
        return op

    while instruction_pointer + 1 < len(program):
        opcode, operand = program[instruction_pointer], program[instruction_pointer + 1]
        match opcode:
            case 0:
                register["A"] //= (1 << combo(operand))
            case 1:
                register["B"] ^= operand
            case 2:
                register["B"] = combo(operand) % 8
            case 3:
                if register["A"]:
                    instruction_pointer = operand
                    continue
            case 4:
                register["B"] ^= register["C"]
            case 5:
                result.append(combo(operand) % 8)
            case 6:
                register["B"] = register["A"] // (1 << combo(operand))
            case 7:
                register["C"] = register["A"] // (1 << combo(operand))
        instruction_pointer += 2
    # print result
    print(register, result)
    io.copy_result(",".join([str(x) for x in result]))

if __name__ == "__main__":
    with open("2024/17/chronospatial-computer-input.txt", "r") as f:
        file_text = f.read()
        main(file_text.splitlines())
