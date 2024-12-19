from re import findall

A = 0
B = 1
C = 2


def adv(register_a, combo_operand):
    return register_a >> combo_operand


def bxl(register_b, literal_operand):
    return register_b ^ literal_operand


def bst(combo_operand):
    return combo_operand % 8


def jnz(register_a, instruction_pointer, literal_operand):
    if not register_a:
        return instruction_pointer + 2
    return literal_operand


def bxc(register_b, register_c, operand=0):
    return register_b ^ register_c


def out(combo_operand):
    return combo_operand % 8


def bdv(register_a, combo_operand):
    return adv(register_a, combo_operand)


def cdv(register_a, combo_operand):
    return adv(register_a, combo_operand)


def combo_operand(registers, idx):
    if idx in [0, 1, 2, 3]:
        return idx
    return {4: registers[0], 5: registers[1], 6: registers[2]}[idx]


def run(registers, program):
    instruction_pointer = 0
    output = []
    while instruction_pointer < len(program):
        instruction = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        match instruction:
            case 0:
                registers[A] = adv(registers[A], combo_operand(registers, operand))
            case 1:
                registers[B] = bxl(registers[B], operand)
            case 2:
                registers[B] = bst(combo_operand(registers, operand))
            case 3:
                instruction_pointer = jnz(registers[A], instruction_pointer, operand)
                print(instruction_pointer)
                continue
            case 4:
                registers[B] = bxc(registers[B], registers[C])
            case 5:
                output.append(out(combo_operand(registers, operand)))
            case 6:
                registers[B] = bdv(registers[A], combo_operand(registers, operand))
            case 7:
                registers[C] = cdv(registers[A], combo_operand(registers, operand))
            case _:
                raise ValueError("invalid index")
        instruction_pointer += 2
    return ",".join([str(n) for n in output])


print("---- Day 17 ----")
with open("input/day17.txt", encoding="utf-8", mode="r") as file:
    registers, program = [
        [*map(int, findall(r"\d+", line))] for line in file.read().split("\n\n")
    ]
    p1 = run(registers, program)
    print(p1)
    # print(f"\tPart 1: {p1}")
    # print(f"\tPart 2: {p2}")
