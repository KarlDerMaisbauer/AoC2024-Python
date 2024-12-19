from functools import cache


@cache
def valid(pattern, towels):
    if not pattern:
        return 1
    solutions = 0
    for towel in towels:
        if pattern.startswith(towel):
            solutions += valid(pattern.removeprefix(towel), towels)
    return solutions


with open("input.txt", 'r') as input_file:
    combinations = []
    iter = iter(input_file)
    for line in iter:
        line_str = line.rstrip()
        if line_str == "":
            break
        towels = line_str.split(", ")
        combinations.extend(towels)
    # print(f"combinations {combinations}")
    counter = 0
    for line in iter:
        # print("##################")
        print(f"check {line.rstrip()}")
        val = valid(line.rstrip(), tuple(combinations))
        print(f"= {val}")
        counter += val
    print(f"valid combinations {counter}")
