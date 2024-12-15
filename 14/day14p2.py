import re
pattern = r".*X([+-=]\w+),\s*Y([+-=]\w+)"

cols = 101
rows = 103


sepparator_x = (cols // 2)
sepparator_y = (rows // 2)

print(f"x {sepparator_x}")
print(f"y {sepparator_y}")

safe1 = 0
safe2 = 0
safe3 = 0
safe4 = 0

def calc_robot_pos(pos, velocity, sec, cols, rows):
    x = ((pos[0]) + (sec * velocity[0])) % cols
    y = ((pos[1]) + (sec * velocity[1])) % rows
    return (x, y)

def add_to_position(pos, s1, s2, s3, s4, sepp_x, sepp_y):
    x = pos[0]
    y = pos[1]

    if x < sepp_x and y > sepp_y:
        # print("s1")
        s1 += 1
    if x > sepp_x and y > sepp_y:
        # print("s2")
        s2 += 1
    if x < sepp_x and y < sepp_y:
        # print("s3")
        s3 += 1
    if x > sepp_x and y < sepp_y:
        # print("s4")
        s4 += 1
    return s1, s2, s3, s4


def get_max_row(line):
    curr_max = 0
    in_row = 0
    for item in line:
        if item == "O":
            in_row += 1
        else:
            if in_row > curr_max:
                curr_max = in_row
                in_row = 0
    return curr_max


with open("input.txt", 'r') as input_file:
    arr = []
    robots = []
    counter = 0
    for y in range(rows):
        arr.append([' '] * cols)

    for line in input_file:
        line = line.rstrip()
        if line:
            val= line.rstrip().split(" ")
            temp = val[0].replace("p=", "").split(",")
            pos = (int(temp[0]), int(temp[1]))
            # arr[pos[1]][pos[0]] = "O"    
            temp = val[1].replace("v=", "").split(",")
            # print(f"bef_pos {pos}")
            val = (int(temp[0]), int(temp[1]))
            robots.append([pos, val])
    while True:
        counter += 1
        for i in range(len(robots)):
            robot = robots[i]
            r_pos = robot[0]
            r_vel = robot[1]
            arr[r_pos[1]][r_pos[0]] = " "

            r_pos = calc_robot_pos(robot[0], robot[1], 1, cols, rows)

            robots[i] = [r_pos, r_vel]
            arr[r_pos[1]][r_pos[0]] = "O"
        # print("############################################################################")
        for l in arr:
            if get_max_row(l) > 15:
                for l in arr:
                    print("".join(l))

                print(f"curr_counter = {counter}")
                char = input("Press a key: ")
                if char and char[0] == "f":
                    break
        print(f"curr_counter {counter}")
        # print("############################################################################")


    print(f"s1 {safe1}, s2 {safe2}, s3 {safe3}, s4 {safe4}")
    # for i in arr:
        # print("".join(i))
    print(safe1 * safe2 * safe3 * safe4)
