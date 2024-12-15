import re
pattern = r".*X([+-=]\w+),\s*Y([+-=]\w+)"


class WareHouse:
    def __init__(self, boxes, robot, warehouse):
        self.boxes = boxes
        self.robot = robot
        self.warehouse = warehouse

    def print_field(self):
        for line in self.warehouse:
            print("".join(line))

    def is_free(self, pos):
        return self.warehouse[pos.y][pos.x] == '.'

    def is_blocked(self, pos):
        return self.warehouse[pos.y][pos.x] == '#'

    def has_box(self, pos):
        return self.warehouse[pos.y][pos.x] == 'O'

    def get_score(self):
        score = 0
        col_max = len(self.warehouse[0])
        for y in range(1, len(self.warehouse) - 1, 1):
            for x in range(1, col_max - 1, 1):
                if self.warehouse[y][x] == 'O':
                    score += 100 * y + x
        return score

    def move_robot(self, char):
        dir = (0, 0)
        if char == '^':
            dir = (0, -1)
        if char == 'v':
            dir = (0, 1)
        if char == '<':
            dir = (-1, 0)
        if char == '>':
            dir = (1, 0)
        new_robot_pos = Moveable(self.robot.x + dir[0], self.robot.y + dir[1])
        if self.is_free(new_robot_pos):
            self.warehouse[self.robot.y][self.robot.x] = '.'
            self.robot = new_robot_pos
            self.warehouse[self.robot.y][self.robot.x] = '@'
        elif self.has_box(new_robot_pos):
            next_pos = new_robot_pos
            while self.has_box(next_pos):
                next_pos = Moveable(next_pos.x + dir[0], next_pos.y + dir[1])
            if self.is_free(next_pos):
                self.warehouse[self.robot.y][self.robot.x] = '.'
                self.robot = new_robot_pos
                self.warehouse[self.robot.y][self.robot.x] = '@'
                self.warehouse[next_pos.y][next_pos.x] = 'O'


class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y


with open("inputs-field.txt", 'r') as input_file:
    field = []
    boxes = []
    robot = Moveable(0, 0)
    for y, line in enumerate(input_file):
        line = line.rstrip()
        line_list = []
        for x, char in enumerate(list(line)):
            if char == 'O':
                boxes.append(Moveable(x, y))
            if char == '@':
                robot = Moveable(x, y)
        field.append(list(line))
    warehouse = WareHouse(boxes, robot, field)
    warehouse.print_field()
    with open("inputs-moves.txt", 'r') as input_moves:
        for line in input_moves:
            for char in list(line.rstrip()):
                warehouse.move_robot(char)
                print(f"pos after {char} move")
                warehouse.print_field()
                user_input = input("Continue: ")
    warehouse.print_field()
    print(f"Warehouse score {warehouse.get_score()}")
