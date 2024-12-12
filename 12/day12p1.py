from collections import deque


class Area:
    def __init__(self, start, x_len, y_len, symbol):
        self.start = start
        self.members = []
        for _ in range(y_len):
            self.members.append([0] * x_len)
        self.members[start[1]][start[0]] = 1
        self.area = 0
        self.perimeter = 0
        self.x_len = x_len
        self.y_len = y_len
        self.symbol = symbol

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

    def BFS(self, arr, used):
        queue = deque([self.start])
        while len(queue) != 0:
            point = queue.popleft()
            self.area += 1
            self.perimeter += 4 - self.get_conected_members(point, arr)
            used = self.set_used_ext(point, used)
            # self.set_used(point)
            neighbours = self.get_neighbours(point, arr)
            for n in neighbours:
                self.set_used_ext(n, used)
                self.set_used(n)
            # print(self.get_neighbours(point, arr))
            queue.extend(neighbours)

        return used, self.area, self.perimeter


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
                used, area, perimeter = Area(
                    (x, y), x_len, y_len, field[y][x]).BFS(field, used)
                cost += area * perimeter
    # used, area, perimeter = Area(
    #     (0, 0), x_len, y_len, field[0][0]).BFS(field, used)
    # print(f"area: {area}")
    # print(f"peri: {perimeter}")
    # cost += area * perimeter

    print(f"uh des wird deier {cost}")

    # for l in field:
    #     print(''.join(l))
    #
    # for l in used:
    #     print(l)
