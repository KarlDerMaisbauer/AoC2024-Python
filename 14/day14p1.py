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


with open("input.txt", 'r') as input_file:
    # for y in range(rows):
        # arr.append(['*'] * cols)

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
            aft_pos = calc_robot_pos((pos[0], pos[1]), val, 100, cols, rows)
            print(f"{aft_pos}")
            safe1, safe2, safe3, safe4 = add_to_position(aft_pos, safe1, safe2, safe3, safe4, sepparator_x, sepparator_y)
    print(f"s1 {safe1}, s2 {safe2}, s3 {safe3}, s4 {safe4}")
    # for i in arr:
        # print("".join(i))
    print(safe1 * safe2 * safe3 * safe4)
