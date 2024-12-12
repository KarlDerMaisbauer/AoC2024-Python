

class Pos:
    def __init__(self, x_pos, y_pos, x_dir, y_dir):
        self.x = x_pos
        self.y = y_pos
        self.x_dir = x_dir
        self.y_dir = y_dir

    def __eq__(self, o):
        return self. x == o.x and self.y == o.y and self.x_dir == o.x_dir and self.y_dir == o.y_dir

    def valid(self, maze):
        return self.x >= 0 and self.x < len(maze[0]) and self.y >= 0 and self.y < len(maze)

    def rotate(self):
        self.x_dir, self.y_dir = - self.y_dir, self.x_dir

    def next(self):
        return (self.x + self.x_dir, self.y + self.y_dir)

    def step(self, maze):
        next_x, next_y = self.next()
        while next_y < len(maze) and next_x < len(maze[0]) and maze[next_y][next_x] == '#':
            self.rotate()
            next_x, next_y = self.next()
        self.x, self.y = next_x, next_y

    def tupplify(self):
        return (self.x, self.y, self.x_dir, self.y_dir)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, x_dir: {self.x_dir}, y_dir: {self.y_dir}"

    def pos(self):
        return self.x, self.y


def extract_and_modify_subarray(array, x, y):
    rows, cols = len(array), len(array[0])  # Get array dimensions
    sub_size = 5
    half_size = sub_size // 2

    # Check if the 7x7 subarray fits within the boundaries
    if not (half_size <= x < cols - half_size and half_size <= y < rows - half_size):
        return "Subarray out of bounds"

    # Extract and modify the 7x7 subarray
    subarray = []
    for i in range(y - half_size, y + half_size + 1):
        row = []
        for j in range(x - half_size, x + half_size + 1):
            row.append(array[i][j])
        subarray.append(row)

    # Replace the center of the subarray with 'g'
    subarray[half_size][half_size] = 'g'

    return subarray


def print_maze(maze, guard):
    for i, row in enumerate(maze):
        row = ''.join(row)
        if guard.y == i:
            row = row + "sdffffff"
        print(row)


def run_maze(maze, guard, should_print):
    history = set()
    counter = 0
    while guard.valid(maze):
        if counter == 200:
            return 1
        # guard_old = copy.deepcopy(guard)
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        history.add(guard.tupplify())
        x, y = guard.x, guard.y
        guard.step(maze)
        # assert x != guard.x or y != guard.y, "dgrfshokjpfgdszhgsdfztoipjkh"
        assert (x == guard.x and (y == guard.y + 1 or y == guard.y-1) or y ==
                guard.y and (x == guard.x + 1 or x == guard.x-1)), "gggggggggggggg"
        if not guard.valid(maze):
            return 0
        g_tupple = guard.tupplify()
        # if not guard.valid(maze):
        # break
        if g_tupple in history:
            # print(f"loop step {g_tupple}")
            counter += 1
            # return 1
        # history.add(g_tupple)
        if should_print:
            print_maze(maze, guard)
    return 0


def run_maze_first(maze, guard, should_print):
    hard_edges = set()
    positions = set()
    while guard.valid(maze):
        # guard_old = copy.deepcopy(guard)
        x, y = guard.x, guard.y
        guard.step(maze)
        if not guard.valid(maze):
            break
        positions.add(guard.pos())
        assert x != guard.x or y != guard.y, "dgrfshokjpfgdszhgsdfztoipjkh"
        g_tupple = guard.tupplify()
        if not guard.valid(maze):
            break
        if g_tupple in hard_edges:
            # print(g_tupple)
            assert False, "fdfffffffffffffffffff"
            return 1
        # hard_edges.add(g_tupple)
        if should_print:
            print_maze(maze, guard)
    return positions


with open("input.txt", 'r') as input_file:
    maze = []
    for row_number, line in enumerate(input_file):
        row = list(line.rstrip())
        maze.append(row)

    positions = list(run_maze_first(maze, Pos(45, 86, 0, -1), False))
    mazes_checked = 0
    loops = 0
    for (x, y) in positions:
        # print(f"{x}, {y}")
        if mazes_checked % 1000 == 0:
            print(f"{mazes_checked} out of {len(positions)}")
        with open("input.txt", 'r') as input_file:
            maze_new = []
            for row_number, line in enumerate(input_file):
                row = list(line.rstrip())
                maze_new.append(row)
            maze_new[y][x] = '#'
            mazes_checked += 1
            loops += run_maze(maze_new, Pos(45, 86, 0, -1), False)
    print(loops)

    # for y in range(len(maze)):
    #     for x in range(len(maze[0])):
    #         pos = y*len(maze[0]) + x
    #         if mazes_checked % 100 == 0:
    #             print(f"{mazes_checked} out of 16094")
    #
    #         with open("input.txt", 'r') as input_file:
    #             maze_new = []
    #             for row_number, line in enumerate(input_file):
    #                 row = list(line.rstrip())
    #                 maze_new.append(row)
    #
    #             mazes_checked += 1
    #             maze_new[y][x] = '#'
    #             guard = Pos(45, 86, 0, -1)
    #             loops_old = loops
    #             loops += run_maze(maze_new, guard, False)
    #             assert (loops == loops_old or loops == loops_old+1)
    # print(f"num_loops {loops}")
    # print(f"mazes_checked {mazes_checked}")
