import re
pattern = r".*X([+-=]\w+),\s*Y([+-=]\w+)"


class WareHouse:
    def __init__(self, robot, warehouse):
        self.boxes = boxes
        self.robot = robot
        self.warehouse = warehouse

    def print_field(self):
        for line in self.warehouse:
            print("".join(line))

    def is_free(self, pos):
        print(f"value to check {self.get_value(pos)}, on pos {pos}")
        return self.get_value(pos) == '.'

    def has_box(self, pos):
        item = self.warehouse[pos.y][pos.x]
        return item == '[' or item == ']'

    def get_score(self):
        score = 0
        col_max = len(self.warehouse[0])
        for y in range(1, len(self.warehouse) - 1, 1):
            for x in range(1, col_max - 1, 1):
                if self.warehouse[y][x] == '[':
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
        print(f"bef robot pos {self.robot}")
        new_robot_pos = Moveable(self.robot.x + dir[0], self.robot.y + dir[1])

        if self.is_free(new_robot_pos):
            print("move freely")
            self.warehouse[self.robot.y][self.robot.x] = '.'
            self.robot = new_robot_pos
            self.warehouse[self.robot.y][self.robot.x] = '@'
        elif self.has_box(new_robot_pos):
            self.boxes = []
            if self.can_move_boxes(new_robot_pos, dir):
                print("move with boxes")
                self.move_boxes(dir)
                self.warehouse[self.robot.y][self.robot.x] = '.'
                self.robot = new_robot_pos
                self.warehouse[self.robot.y][self.robot.x] = '@'
            else:
                print(f"cannot move with boxes")
        else:
            print("cannot move")
        print(f"aft robot pos {self.robot}")

    def get_value(self, pos):
        return self.warehouse[pos.y][pos.x]

    def get_box_from_pos(self, pos):
        if self.get_value(pos) == '[':
            return Box(pos, Moveable(pos.x+1, pos.y))
        else:
            return Box(Moveable(pos.x-1, pos.y), pos)

    def can_move_boxes(self, robot_pos, dir):
        box = self.get_box_from_pos(robot_pos)
        box_n = box.move(dir)
        if self.is_free(box_n.pos1) and self.is_free(box_n.pos2):
            self.boxes.append(box)
            for lin in self.boxes:
                print(lin)
            print("free as fuck")
            return True
        elif self.is_blocked_box(box, dir):
            print("oh no")
            return False
        else:
            self.boxes = [box]
            boxes_to_check = self.create_boxes(box_n, dir)
            return self.can_move_boxes_inner(boxes_to_check, dir)

    def can_move_boxes_inner(self, boxes_to_check, dir):
        can_move = True
        while len(boxes_to_check) != 0:
            print(len(self.boxes))
            box = boxes_to_check.pop()
            box_n = box.move(dir)
            if self.is_blocked_box(box, dir):
                print(f"box {box} not moveable")
                can_move = False
                break
            elif self.is_free_box(box, dir):
                print("free")
                self.boxes.append(box)
            else:
                boxes = self.create_boxes(box_n, dir)
                self.boxes.append(box)
                can_move = self.can_move_boxes_inner(boxes, dir)

                if not can_move:
                    break
        print(f"ddddddd {len(self.boxes)}")

        for lin in self.boxes:
            print(f"################################{lin}")
        return can_move

    def create_boxes(self, box, dir):
        boxes = []
        if dir[0] == 0:
            if self.get_value(box.pos1) == '[' or self.get_value(box.pos1) == ']':
                boxes.append(self.get_box_from_pos(box.pos1))

            if self.get_value(box.pos2) == '[' or self.get_value(box.pos2) == ']':
                boxes.append(self.get_box_from_pos(box.pos2))
        elif dir[0] == 1:
            if self.get_value(box.pos2) == '[':
                boxes = [self.get_box_from_pos(box.pos2)]

        else:
            if self.get_value(box.pos1) == ']':
                boxes = [self.get_box_from_pos(box.pos1)]
        return boxes

    def is_free_box(self, box, dir):
        box_n = box.move(dir)
        if dir[0] == 0:
            return self.get_value(box_n.pos1) == '.' and self.get_value(box_n.pos2) == '.'
        elif dir[0] == 1:
            return self.get_value(box_n.pos2) == '.'
        else:
            return self.get_value(box_n.pos1) == '.'

    def is_blocked_box(self, box, dir):
        print(f"dir {dir}")
        print(f"box {box}")
        box_n = box.move(dir)
        print(f"new {box_n}")
        if dir[0] == 0:
            return self.get_value(box_n.pos1) == '#' or self.get_value(box_n.pos2) == '#'
        elif dir[0] == 1:
            return self.get_value(box_n.pos2) == '#'
        else:
            return self.get_value(box_n.pos1) == '#'

    def color_pos(self, pos, char):
        self.warehouse[pos.y][pos.x] = char

    def move_boxes(self, dir):
        print(f"moving {len(self.boxes)} boxes")
        self.boxes.reverse()
        for box in self.boxes:
            b_new = box.move(dir)
            print(f"move {box}")
            print(f"to   {b_new}")
            self.color_pos(box.pos1, '.')
            self.color_pos(box.pos2, '.')
            self.color_pos(b_new.pos1, '[')
            self.color_pos(b_new.pos2, ']')


class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dir):
        return Moveable(self.x + dir[0], self.y + dir[1])

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


class Box:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2

    def __str__(self):
        return f"start: {self.pos1}, end: {self.pos2}"

    def move(self, dir):
        pos1 = self.pos1.move(dir)
        pos2 = self.pos2.move(dir)
        return Box(pos1, pos2)

    def is_free(self, field, dir_ch):
        if dir_ch == '^' or dir_ch == 'v':
            i1 = field[self.pos1.y][self.pos1.x]
            i2 = field[self.pos2.y][self.pos2.x]
            return i1 == '.' and i2 == '.'
        elif dir_ch == '<':
            return i1 == '.'
        else:
            return i2 == '.'

    def is_blocked(self, field):
        i1 = field[self.pos1.y][self.pos1.y]
        i2 = field[self.pos2.y][self.pos2.y]
        return i1 == '#' or i2 == '#'

    def check_move(self, char, field):
        dir = (0, 0)
        if char == '^':
            dir = (0, -1)
        if char == 'v':
            dir = (0, 1)
        if char == '<':
            dir = (-1, 0)
        if char == '>':
            dir = (1, 0)
        new_pos = Box(Moveable(self.pos1).move(dir),
                      Moveable(self.pos2).move(dir))
        if new_pos.is_free(field, char):
            return True
        elif new_pos.is_blocked(field):
            return False
        else:
            new_boxes = new_pos.get_boxes(field)
            can_move = True
            for box in new_boxes:
                can_move &= box.check_move(char, field)

    def move_box(self, char, field):
        dir = (0, 0)
        if char == '^':
            dir = (0, -1)
        if char == 'v':
            dir = (0, 1)
        if char == '<':
            dir = (-1, 0)
        if char == '>':
            dir = (1, 0)
        new_pos = Box(Moveable(self.pos1).move(dir),
                      Moveable(self.pos2).move(dir))
        if new_pos.is_free(field, char):
            field[self.pos1.y][self.pos1.y] = '.'
            field[self.pos2.y][self.pos2.y] = '.'
            field[new_pos.pos1.y][new_pos.pos1.y] = '['
            field[new_pos.pos2.y][new_pos.pos2.y] = ']'
            return field
        elif new_pos.is_blocked(field):
            return field
        else:
            can_move = self.check_move(char, field)
            new_boxes = new_pos.get_boxes(field)
            if can_move:
                for box in new_boxes:
                    field = box.move_box()


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
                line_list.append('[')
                line_list.append(']')
            elif char == '@':
                robot = Moveable(len(line_list), y)
                line_list.append('@')
                line_list.append('.')
            elif char == '#':
                line_list.append('#')
                line_list.append('#')
            else:
                line_list.append('.')
                line_list.append('.')

        field.append(line_list)
    warehouse = WareHouse(robot, field)
    warehouse.print_field()
    with open("inputs-moves.txt", 'r') as input_moves:
        for line in input_moves:
            for char in list(line.rstrip()):
                # user_input = input("Continue: ")
                warehouse.move_robot(char)
                print(f"pos after {char} move")
                warehouse.print_field()
    warehouse.print_field()
    print(f"Warehouse score {warehouse.get_score()}")
