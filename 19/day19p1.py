from collections import deque
import re
pattern = r".*X([+-=]\w+),\s*Y([+-=]\w+)"


def valid(pattern, towels):
    starts = []
    for towel in towels:
        if towel[0] == pattern[0]:
            starts.append(towel)
    if len(starts) == 0:
        return 0
    else:
        return valid_inner(pattern, towels, starts, 0)


def get_towels(pattern, towels, index):
    starts = []
    for towel in towels:
        if towel[0] == pattern[index]:
            starts.append(towel)
    return starts


def valid_inner(pattern, towels, fitting_towels, index):
    for towel in fitting_towels:
        valid_subsection = True
        for i in range(len(towel)):
            if i + index == len(pattern) - 1 and towel[i] == pattern[i + index]:
                return 1
            if towel[i] != pattern[i + index]:
                valid_subsection = False
                break
        if valid_subsection:
            if index + len(towel) >= len(pattern):
                continue
            next_towels = get_towels(pattern, towels, index + len(towel))
            val = valid_inner(
                pattern, towels, next_towels, index + len(towel))
            if val == 1:
                return 1
    return 0


with open("input.txt", 'r') as input_file:
    combinations = []
    iter = iter(input_file)
    for line in iter:
        line_str = line.rstrip()
        if line_str == "":
            break
        towels = line_str.split(", ")
        combinations.extend(list(map(list, towels)))
    # print(f"combinations {combinations}")
    counter = 0
    for line in iter:
        val = valid(list(line.rstrip()), combinations)
        if val == 1:
            print(f"valid {line.rstrip()}")
        counter += val
    print(f"valid combinations {counter}")
