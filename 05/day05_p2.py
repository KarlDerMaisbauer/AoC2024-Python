import re


def get_dependency(line):
    pattern = r'(\d+)\|(\d+)'
    finds = re.findall(pattern, line)
    if len(finds) == 1:
        return int(finds[0][0]), int(finds[0][1])
    return -1, -1


def add_value(dependency_map, key, value):
    if key in dependency_map:
        dependency_map[key].append(value)
    else:
        dependency_map[key] = [value]


def correction_val(pages, dep_map):
    for idx1 in range(len(pages)):
        for idx2 in range(idx1+1, len(pages), 1):
            key = pages[idx1]
            if key in dep_map:
                if pages[idx2] in dep_map[key]:
                    pages[idx1], pages[idx2] = pages[idx2], pages[idx1]
                    return correction_val(pages, dep_map)
    middle = len(pages) // 2
    return pages[middle]


def protocol_value(protocol, dep_map):
    if protocol == "\n":
        return 0
    pages = list(map(int, protocol.split(",")))
    invalid_pages = set()
    for i in range(len(pages)-1, 0-1, -1):
        value = pages[i]
        if value in invalid_pages:
            return correction_val(pages, dep_map)
        elif value in dep_map:
            for v in dep_map[value]:
                invalid_pages.add(v)
    return 0


with open("dependencies.txt", 'r') as dependency_file:
    dep_map = {}
    # print(dependency_file.read())
    for line in dependency_file:
        key, value = get_dependency(line)
        if key > 0:
            add_value(dep_map, key, value)
    # print(dep_map)
    with open("protocols.txt") as protocal_file:
        counter = 0
        for protocol in protocal_file:
            counter += protocol_value(protocol, dep_map)
        print(counter)
