
y_pos = 0
x_pos = 0

y_dir = -1
x_dir = 0


def rotate(x_dir, y_dir):
    if y_dir == -1:
        return 0, 1
    if x_dir == 1:
        return 1, 0
    if y_dir == 1:
        return 0, -1
    else:
        return -1, 0


def valid_pos(maze, x_pos, y_pos):
    if x_pos < 0 or y_pos < 0:
        return False
    if y_pos >= len(maze):
        return False
    if x_pos >= len(maze[0]):
        return False
    return True


def step(maze, x_pos, y_pos, x_dir, y_dir):
    next_x = x_pos + x_dir
    next_y = y_pos + y_dir
    counter = 0
    if maze[next_y][next_x] == '#':
        y_dir, x_dir = rotate(x_dir, y_dir)
        next_x = x_pos + x_dir
        next_y = y_pos + y_dir
    if maze[next_y][next_x] != 'X':
        counter += 1
    maze[y_pos][x_pos] = 'X'
    return next_y, next_x, y_dir, x_dir, counter


with open("input.txt", 'r') as input_file:
    maze = []
    for row_number, line in enumerate(input_file):
        row = list(line.rstrip())
        maze.append(row)
        if '^' in line:
            y_pos = row_number
            x_pos = row.index('^')
    counter = 0
    while valid_pos(maze, x_pos, y_pos):
        y_pos, x_pos, y_dir, x_dir, counter_val = step(
            maze, x_pos, y_pos, x_dir, y_dir)
        counter += counter_val
    print(counter)
