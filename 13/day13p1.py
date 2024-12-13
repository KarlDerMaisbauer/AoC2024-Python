import re
pattern = r".*X([+-=]\w+),\s*Y([+-=]\w+)"


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mul(self, scale):
        return Pos(self.x * scale, self.y * scale)

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def greater_eq(self, o):
        return self.x >= o.x and self.y >= o.y

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

    def add(self, o):
        return Pos(self.x + o.x, self.y+o.y)


def calc_min_tokens(input_arr):
    a = input_arr[0]
    b = input_arr[1]
    p = input_arr[2]
    curr_min_tokens = 0
    curr_tokens_a = 1
    # print(f"p: {p}")
    # print(f"pos: {a.mul(curr_tokens_a)}")
    while p.greater_eq(a.mul(curr_tokens_a)):
        # print(f"p: {p}")
        # print(f"pos: {a.mul(curr_tokens_a)}")
        if p == a.mul(curr_min_tokens):
            curr_min_tokens = 3 * curr_tokens_a
            # print("first")
            break
        curr_tokens_a += 1
    curr_a = a.mul(curr_tokens_a)
    while curr_tokens_a != -1:
        curr_tokens_b = 1
        while p.greater_eq(curr_a.add(b.mul(curr_tokens_b))):
            if p == curr_a.add(b.mul(curr_tokens_b)):
                curr_total_tokens = 3 * curr_tokens_a + curr_tokens_b
                if curr_min_tokens == 0 or curr_total_tokens < curr_min_tokens:
                    # print("found")
                    # print(f"tokens needed = {curr_total_tokens}")
                    curr_min_tokens = curr_total_tokens
                    break
            curr_tokens_b += 1
        curr_tokens_a -= 1
        curr_a = a.mul(curr_tokens_a)
    print(f"A: {str(a)}, B: {str(b)}, price: {str(p)}")
    return curr_min_tokens


with open("input.txt", 'r') as input_file:
    inputs = []
    buffer = []
    for line in input_file:
        stripped_line = line.strip()
        if stripped_line:
            print(stripped_line)
            match = re.search(pattern, stripped_line)
            if not match:
                assert False, "this should not happen"

            buffer.append(Pos(int(match.group(1).replace("=", "")),
                          int(match.group(2).replace("=", ""))))
        if len(buffer) == 3:
            inputs.append(buffer)
            buffer = []
    tokens = 0
    for input in inputs:
        # print(input)
        tokens += calc_min_tokens(input)

    print(f"uh des wird deier {tokens}")

    # for l in field:
    #     print(''.join(l))
    #
    # for l in used:
    #     print(l)
