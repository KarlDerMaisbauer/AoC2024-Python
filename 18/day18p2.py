from collections import deque
import re
pattern = r".*X([+-=]\w+),\s*Y([+-=]\w+)"

size = 70


class MemorySction:
    def __init__(self, size):
        self.memory_field = [
            ['.' for _ in range(size+1)] for _ in range(size+1)]

    def print_memory_field(self):
        for line in self.memory_field:
            print("".join(line))

    def corrupt_memory_arr(self, positions):
        for x, y in positions:
            self.memory_field[y][x] = '#'

    def corrupt_memory_singe(self, pos):
        x, y = pos
        self.memory_field[y][x] = '#'

    def get_neighbours(self, pos):
        neighbours = []
        x = pos[0]
        y = pos[1]
        if x > 0 and self.memory_field[y][x-1] != '#':
            neighbours.append((x-1, y))
        if x+1 < len(self.memory_field[0]) and self.memory_field[y][x+1] != '#':
            neighbours.append((x+1, y))
        if y > 0 and self.memory_field[y-1][x] != '#':
            neighbours.append((x, y-1))
        if y+1 < len(self.memory_field) and self.memory_field[y+1][x] != '#':
            neighbours.append((x, y+1))
        return neighbours

    def get_min_path(self):
        used_grid = [['.' for _ in range(size+1)] for _ in range(size+1)]
        used_grid[0][0] = 'X'
        queue = deque([(0, 0)])
        length = 0
        while len(queue) != 0:
            level_size = len(queue)
            # print(f"level size = {level_size}")
            # print(f"curr level {length}")
            while level_size != 0:
                level_size -= 1
                val = queue.popleft()
                if val == (size, size):
                    # for line in used_grid:
                    #     print("".join(line))
                    return length
                neighbours = self.get_neighbours(val)
                for n in neighbours:
                    if used_grid[n[1]][n[0]] == '.':
                        used_grid[n[1]][n[0]] = 'X'
                        queue.append(n)
            # print(queue)
            length += 1
        return -1


with open("input.txt", 'r') as input_file:
    corrupted_mem = []
    for line in input_file:
        coords_str = line.rstrip().split(",")
        corrupted_mem.append((int(coords_str[0]), int(coords_str[1])))
    # print(corrupted_mem)
    memory = MemorySction(size)
    # memory.print_memory_field()
    corr_valid = corrupted_mem[:1024]
    corr_rem = corrupted_mem[1024:]
    memory.corrupt_memory_arr(corr_valid)
    for pos in corr_rem:
        memory.corrupt_memory_singe(pos)
        if memory.get_min_path() == -1:
            print(f" fist invalid pos {pos}")
            break
    # memory.print_memory_field()
    print(memory.get_min_path())
