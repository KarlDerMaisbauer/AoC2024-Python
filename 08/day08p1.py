from math import gcd

antennas = {}
invalid_positions = set()
antinodes = set()


def check_left(n1, x_diff, y_diff, maze, invalid_pos):
    canidate = (n1[0] - x_diff, n1[1] - y_diff)
    if canidate[0] < 0 or canidate[0] >= len(maze[0]) or canidate[1] < 0 or canidate[1] >= len(maze):
        return []
    if canidate in invalid_pos:
        return []
    return [canidate]


def check_right(n2, x_diff, y_diff, maze, invalid_pos):
    canidate = (n2[0] + x_diff, n2[1] + y_diff)
    if canidate[0] < 0 or canidate[0] >= len(maze[0]) or canidate[1] < 0 or canidate[1] >= len(maze):
        return []
    if canidate in invalid_pos:
        return []
    return [canidate]


def check_middle(n1, n2, x_diff, y_diff, maze, invalid_pos):
    scale = gcd(x_diff, y_diff)
    if scale != 3:
        return []
    else:
        x_diff = x_diff // 3
        y_diff = y_diff // 3
        canidates = check_right(n1, x_diff, y_diff, maze, invalid_pos)
        canidates += check_left(n2, x_diff, y_diff, maze, invalid_pos)
        return canidates


def check_nodes(n1, n2, maze, invalid_pos):
    if n1[0] > n2[0]:
        n1, n2 = n2, n1
    x_diff = n2[0] - n1[0]
    y_diff = n2[1] - n1[1]
    canidates = check_left(n1, x_diff, y_diff, maze, invalid_pos)
    canidates += check_right(n2, x_diff, y_diff, maze, invalid_pos)
    canidates += check_middle(n1, n2, x_diff,
                              y_diff, maze, invalid_pos)
    return canidates


with open("input.txt", 'r') as input_file:
    maze = []
    for y, line in enumerate(input_file):
        line_arr = list(line.rstrip())
        for x in range(len(line_arr)):
            key = line_arr[x]
            if key != '.':
                invalid_positions.add((x, y))
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
                    value[i], value[j], maze, set())
                # print(curr_antinodes)
                for antinode in curr_antinodes:
                    # print(antinode)
                    antinodes.add(antinode)

    for x, y in antinodes:
        maze[y][x] = '#'
    for line in maze:
        print(''.join(line))
    print(len(antinodes))
# print(invalid_poisitions)
