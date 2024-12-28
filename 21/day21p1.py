

class Decoder:
    def __init__(self, field):
        self.keypad = field
        self.curr_pos = (2, 3)
        for y in range(len(self.keypad)):
            for x in range(len(self.keypad[0])):
                if self.keypad[y][x] == 'A':
                    self.curr_pos = (x, y)
        assert self.curr_pos[0] != -1
        assert self.curr_pos[1] != -1
        # [['7', '8', '9'], ['4', '5', '6'],
        # ['1', '2', '3'], ['X', '0', 'A']]
        self.decoded = []

    def get_val(self, coords):
        return self.keypad[coords[1]][coords[0]]

    def get_dist(self, coords1, coords2, symbol):
        baddiefier = 0
        if len(self.decoded) != 0:
            baddiefier = 0 if self.decoded[len(
                self.decoded) - 1] == symbol else 1
        return 1
        # emptyfier = 1 if symbol == '^' or symbol == else 0
        # return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1]) + baddiefier - emptyfier

    def make_step_towards(self, pos):
        possible_new_pos = []
        x = self.curr_pos[0]
        y = self.curr_pos[1]
        last_symbol = '^'
        if len(self.decoded) != 0:
            last_symbol = self.decoded[len(self.decoded) - 1]
        if last_symbol == '^' or last_symbol == 'v' or 'X' in self.keypad[y]:
            if y != pos[1]:
                if y < pos[1]:
                    self.curr_pos = (x, y+1)
                    self.decoded.append('v')
                else:
                    self.curr_pos = (x, y-1)
                    self.decoded.append('^')
            else:
                if x < pos[0]:
                    self.curr_pos = (x+1, y)
                    self.decoded.append('>')
                else:
                    self.curr_pos = (x-1, y)
                    self.decoded.append('<')
        else:

            if x != pos[0]:
                if x < pos[0]:
                    self.curr_pos = (x+1, y)
                    self.decoded.append('>')
                else:
                    self.curr_pos = (x-1, y)
                    self.decoded.append('<')
            else:
                if y < pos[1]:
                    self.curr_pos = (x, y+1)
                    self.decoded.append('v')
                else:
                    self.curr_pos = (x, y-1)
                    self.decoded.append('^')

        # if x > 0 and self.keypad[y][x-1] != 'X':
            # possible_new_pos.append((x-1, y, '<'))
        # if x < len(self.keypad[0]) - 1 and self.keypad[y][x+1] != 'X':
            # possible_new_pos.append((x+1, y, '>'))
        # if y > 0 and self.keypad[y-1][x] != 'X':
            # possible_new_pos.append((x, y-1, '^'))
        # if y < len(self.keypad) - 1 and self.keypad[y+1][x] != 'X':
            # possible_new_pos.append((x, y+1, 'v'))

        # new_pos = sorted(possible_new_pos,
                # key=lambda x: self.get_dist(pos, x, x[2]))[0]
        # print(new_pos)
        # self.curr_pos = (new_pos[0], new_pos[1])
        # self.decoded.append(new_pos[2])

    def decode_y(self, dist):
        symbol = 'v' if dist > 0 else '^'
        self.decoded.extend([symbol] * abs(dist))

    def decode_x(self, dist):
        symbol = '>' if dist > 0 else '<'
        self.decoded.extend([symbol] * abs(dist))

    def decode_dist_tuple(self, dist):
        # if 'X' in self.keypad[self.curr_pos[1]]:
        # self.decode_y(dist[1])
        # self.decode_x(dist[0])
        col = []
        for i in range(len(self.keypad)):
            col.append(self.keypad[i][dist[0]])
        # print(col)
        # print('X' in col)
        if 'X' in col:
            self.decode_x(dist[0])
            self.decode_y(dist[1])
        else:
            self.decode_y(dist[1])
            self.decode_x(dist[0])

    def go_to(self, pos):
        # while self.curr_pos != pos:
        # self.make_step_towards(pos)
        # print('A')
        if self.curr_pos != pos:
            distances = (pos[0] - self.curr_pos[0], pos[1] - self.curr_pos[1])
            print("#############")
            print(f"curr {self.curr_pos}")
            print(f"end  {pos}")
            print(f"dist {distances}")
            self.decode_dist_tuple(distances)
            self.curr_pos = pos
        self.decoded.append('A')

    def get_pos(self, char):
        for y in range(len(self.keypad)):
            for x in range(len(self.keypad[0])):
                if self.keypad[y][x] == char:
                    return (x, y)
        return (-1, -1)

    def decode(self, code):
        code_parts = list(code)
        for part in code_parts:
            key_pos = self.get_pos(part)
            assert key_pos[0] != -1 and key_pos[1] != -1, "d"
            self.go_to(key_pos)
        return "".join(self.decoded)


class RobotDecoder:
    def __init__(self):
        self.keypad = [['X', '^', 'A'], ['<', 'v', '>']]
        self.curr_pos = (2, 0)
        self.decoded = []


with open("input-small.txt", 'r') as input_file:
    cost = 0
    for line in input_file:
        print("#################")
        # print(line.rstrip())
        p = Decoder([['7', '8', '9'], ['4', '5', '6'],
                    ['1', '2', '3'], ['X', '0', 'A']])
        code1 = p.decode(line.rstrip())
        print(code1)
        code2 = Decoder([['X', '^', 'A'], ['<', 'v', '>']]).decode(code1)
        print(code2)
        code3 = Decoder([['X', '^', 'A'], ['<', 'v', '>']]).decode(code2)
        print(code3)

        print(f"len code {len(list(code3))}, value {int(line.rstrip()[:-1])}")
        cost += len(list(code3)) * int(line.rstrip()[:-1])
    print(f"cost {cost}")


#    258330 too high
