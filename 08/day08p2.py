from math import gcd

antennas = {}
antinodes = set()


def check_left(n1, x_diff, y_diff, maze, invalid_pos):
    canidate = (n1[0] - x_diff, n1[1] - y_diff)
    if canidate[0] < 0 or canidate[0] >= len(maze[0]) or canidate[1] < 0 or canidate[1] >= len(maze):
        return []
    if canidate in invalid_pos:
        return []
    return [canidate]


def is_valid(p, maze):
    return not (p[0] < 0 or p[0] >= len(maze[0]) or p[1] < 0 or p[1] >= len(maze))


def generate_points(p, x_diff, y_diff, maze):
    points = set()
    points.add(p)
    while True:
        p = (p[0] + x_diff, p[1] + y_diff)
        if not is_valid(p, maze):
            return points
        points.add(p)


def check_nodes(n1, n2, maze):
    if n1[0] > n2[0]:
        n1, n2 = n2, n1
    x_diff = (n2[0] - n1[0])
    y_diff = (n2[1] - n1[1])
    scale = gcd(x_diff, y_diff)
    x_diff = x_diff // scale
    y_diff = y_diff // scale
    start = (n1[0], n1[1])
    # print("dfggggggggggg")
    # print(start)
    # print(F"wut {is_valid(start, maze)}")
    while is_valid(start, maze):
        st_new = (start[0] - x_diff, start[1] - y_diff)
        if not is_valid(st_new, maze):
            break

        start = st_new
        # print(f"int {start}")
    # print(start)
    return generate_points(start, x_diff, y_diff, maze)


with open("input.txt", 'r') as input_file:
    maze = []
    for y, line in enumerate(input_file):
        line_arr = list(line.rstrip())
        for x in range(len(line_arr)):
            key = line_arr[x]
            if key != '.':
                if key in antennas:
                    antennas[key].append((x, y))
                else:
                    antennas[key] = [(x, y)]

        maze.append(line_arr)

    for key, value in antennas.items():
        for i in range(len(value)):
            for j in range(i+1, len(value), 1):
                # print(f"{key}: {i}, {j}")
                curr_antinodes = check_nodes(
                    value[i], value[j], maze)
                antinodes.update(curr_antinodes)
    for line in maze:
        print(''.join(line))
    for x, y in antinodes:
        if maze[y][x] == '.':
            maze[y][x] = '#'
    for line in maze:
        print(''.join(line))
    print(len(antinodes))
# print(invalid_poisitions)
