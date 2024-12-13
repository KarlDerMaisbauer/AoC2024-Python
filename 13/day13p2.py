import re
import numpy as np
pattern = r".*X([+-=]\w+),\s*Y([+-=]\w+)"


def calc_cost(a, b, p):
    a1, a2 = a
    b1, b2 = b
    p1, p2 = p

    det = a[0] * b[1] - a[1] * b[0]
    print(det)
    if det == 0:
        print("No Sollution")
        return 0

    numerator_ax = p1 * b2 - p2 * b1
    numerator_bx = a1 * p2 - a2 * p1

    if numerator_ax % det != 0 or numerator_bx % det != 0:
        print("No solution")
        return 0
    ax = numerator_ax // det
    bx = numerator_bx // det

    return 3*ax + bx


with open("input.txt", 'r') as input_file:
    inputs = []
    buffer = []
    for line in input_file:
        stripped_line = line.strip()
        if stripped_line:
            # print(stripped_line)
            match = re.search(pattern, stripped_line)
            if not match:
                assert False, "this should not happen"
            if len(buffer) == 2:
                buffer.append([10000000000000 + int(match.group(1).replace("=", "")),
                               10000000000000 + int(match.group(2).replace("=", ""))])
            else:

                buffer.append([int(match.group(1).replace("=", "")),
                               int(match.group(2).replace("=", ""))])
        if len(buffer) == 3:
            inputs.append(buffer)
            buffer = []
    tokens = 0
    for input in inputs:
        print(input)
        tokens += calc_cost(input[0], input[1], input[2])

    print(f"uh des wird deier {tokens}")

    # for l in field:
    #     print(''.join(l))
    #
    # for l in used:
    #     print(l)
