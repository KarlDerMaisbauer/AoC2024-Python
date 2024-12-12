import re


def mul(x):
    return int(x[0]) * int(x[1])


def find_mul_patterns(input_string):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, input_string)
    return sum(list(map(mul, matches)))


with open("input.txt", 'r') as file:
    file_content = file.read()

    print(find_mul_patterns(file_content))
