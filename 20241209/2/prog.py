import math
import sys
from collections import defaultdict

def interpret_assembly_program(program):
    variables = defaultdict(float)
    commands = []
    labels = {}

    for line_no, line in enumerate(program):
        line = line.strip()
        if not line:
            continue

        if ":" in line:
            label, *rest = line.split(":", 1)
            labels[label.strip()] = len(commands)
            if rest:
                line = rest[0].strip()
            else:
                continue

        if line:
            commands.append((line_no, line.split()))

    for _, command in commands:
        if command[0].startswith("if") and command[-1] not in labels:
            return

    pc = 0
    output = []
    while pc < len(commands):
        line_no, tokens = commands[pc]
        op = tokens[0]

        if op == "stop":
            break

        elif op == "store":
            if len(tokens) == 3:
                try:
                    value = float(tokens[1])
                except ValueError:
                    value = 0.0
                variables[tokens[2]] = value

        elif op in {"add", "sub", "mul", "div"}:
            if len(tokens) == 4:
                src = variables[tokens[1]]
                operand = variables[tokens[2]]
                try:
                    if op == "add":
                        result = src + operand
                    elif op == "sub":
                        result = src - operand
                    elif op == "mul":
                        result = src * operand
                    elif op == "div":
                        result = src / operand
                except ZeroDivisionError:
                    result = math.inf
                variables[tokens[3]] = result

        elif op.startswith("if"):
            if len(tokens) == 4:
                src = variables[tokens[1]]
                operand = variables[tokens[2]]
                condition = False
                if op == "ifeq":
                    condition = src == operand
                elif op == "ifne":
                    condition = src != operand
                elif op == "ifgt":
                    condition = src > operand
                elif op == "ifge":
                    condition = src >= operand
                elif op == "iflt":
                    condition = src < operand
                elif op == "ifle":
                    condition = src <= operand

                if condition:
                    pc = labels[tokens[3]]
                    continue

        elif op == "out":
            if len(tokens) == 2:
                output.append(variables[tokens[1]])

        pc += 1

    for value in output:
        print(value)

def main():
    program = sys.stdin.read().splitlines()
    interpret_assembly_program(program)

if __name__ == "__main__":
    main()
