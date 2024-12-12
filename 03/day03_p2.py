
import re


def mul(x):
    return int(x[0]) * int(x[1])


def find_mul_patterns(input_string):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, input_string)
    return sum(list(map(mul, matches)))


def remove_disabled_operations(input_string):
    # pattern = r"don't\(\).*?(do\(\)|$)"
    pattern = r"don't()"
    valid_sections = []
    first_split = input_string.split(pattern)
    # print(first_split)
    valid_sections.append(first_split[0])
    first_split = first_split[1:]
    # print(first_split)
    for s in first_split:
        second_split = s.split(r"do()")
        # print(second_split)
        if len(second_split) != 1:
            for line in second_split[1:]:
                valid_sections.append(line)
    # print(valid_sections)
    return "".join(valid_sections)


test_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
with open("input.txt", 'r') as file:
    file_content = file.read()
    # print(find_mul_patterns(remove_disabled_operations(test_str)))
    print(find_mul_patterns(remove_disabled_operations(file_content)))
