from collections import deque


class Area:
    def __init__(self, start, x_len, y_len, symbol):
        self.start = start
        self.members = []
        for _ in range(y_len):
            self.members.append([0] * x_len)
        self.members[start[1]][start[0]] = 1
        self.area = 0
        self.sides = 0
        self.x_len = x_len
        self.y_len = y_len
        self.symbol = symbol
        self.dir = (1, 0)

    def get_neighbours(self, point, arr):
        neighbours = []
        x = point[0]
        y = point[1]
        if x > 0 and arr[y][x - 1] == self.symbol and self.members[y][x-1] == 0:
            neighbours.append((x-1, y))
        if (x + 1 < len(arr[0])) and (arr[y][x+1] == self.symbol) and self.members[y][x+1] == 0:
            neighbours.append((x+1, y))
        if y > 0 and arr[y-1][x] == self.symbol and self.members[y-1][x] == 0:
            neighbours.append((x, y-1))
        if y + 1 < len(arr) and arr[y+1][x] == self.symbol and self.members[y+1][x] == 0:
            neighbours.append((x, y+1))

        return neighbours

    def get_conected_members(self, point, arr):
        neighbours = 0
        x = point[0]
        y = point[1]

        # and self.members[y][x-1] != 0:
        if x > 0 and arr[y][x - 1] == self.symbol:
            neighbours += 1
        # and self.members[y][x+1] != 0:
        if x + 1 < len(arr[0]) and arr[y][x+1] == self.symbol:
            neighbours += 1
        # and self.members[y-1][x] != 0:
        if y > 0 and arr[y-1][x] == self.symbol:
            neighbours += 1
        # and self.members[y+1][x] != 0:
        if y + 1 < len(arr) and arr[y+1][x] == self.symbol:
            neighbours += 1
        return neighbours

    def set_used(self, point):
        x = point[0]
        y = point[1]
        self.members[y][x] = 1

    def set_used_ext(self, point, arr_ext):
        x = point[0]
        y = point[1]
        arr_ext[y][x] = 1
        return arr_ext

    def get_used_val(self, point):
        x = point[0]
        y = point[1]
        return self.members[y][x]

    def is_edge(self, point, arr):
        return self.get_conected_members(point, arr) < 4

    def calc_areas(self, line):
        areas = []
        start = -1
        for i in range(len(line)):
            if line[i] == 1 and start == -1:
                start = i
            if line[i] == 0 and start != -1:
                areas.append((start, i-1))
                start = -1
        if start != -1:
            areas.append((start, len(line) - 1))
        return areas

    def overlaps(self, arr1, arr2):
        overlaps = 0
        for item in arr1:
            for item2 in arr2:
                if item[0] == item2[0] and item[1] == item2[1]:
                    overlaps += 4
                elif item[0] == item2[0]:
                    overlaps += 2
                elif item[1] == item2[1]:
                    overlaps += 2
        return overlaps

    def calc_sides_inner(self, start_idx):
        prev_areas = self.calc_areas(self.members[start_idx])
        self.sides = 4 * len(prev_areas)
        for i in range(start_idx+1, len(self.members), 1):
            if not (1 in self.members[i]):
                break
            areas = self.calc_areas(self.members[i])
            overlaps = self.overlaps(prev_areas, areas)
            self.sides += (4 * len(areas)) - overlaps
            prev_areas = areas

    def calc_sides(self):
        for i in range(len(self.members)):
            if 1 in self.members[i]:
                return self.calc_sides_inner(i)
        assert False, "ddd"

    def BFS(self, arr, used):
        queue = deque([self.start])
        while len(queue) != 0:
            point = queue.popleft()
            self.area += 1
            used = self.set_used_ext(point, used)
            self.set_used(point)
            neighbours = self.get_neighbours(point, arr)
            for n in neighbours:
                self.set_used_ext(n, used)
                self.set_used(n)
            queue.extend(neighbours)
        self.calc_sides()
        return used, self.area, self.sides


with open("input.txt", 'r') as input_file:
    field = []
    for line in input_file:
        field.append(list(line.rstrip()))
    x_len = len(field[0])
    y_len = len(field)
    used = []
    for _ in range(y_len):
        used.append([0] * x_len)
    cost = 0
    for y, row in enumerate(field):
        for x in range(x_len):
            if used[y][x] == 0:
                used, area, sides = Area(
                    (x, y), x_len, y_len, field[y][x]).BFS(field, used)
                cost += area * sides
                # print(f"Area: {field[y][x]}, area: {
                # area}, sides: {sides}, cost {area * sides}")
    print(f"uh des wird deier {cost}")
