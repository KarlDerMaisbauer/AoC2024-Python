
def print_map(arr):
    for line in arr:
        print(''.join(map(str, line)))


def get_new_elems(arr, pos):
    x = pos[0]
    y = pos[1]
    pos_val = arr[y][x] + 1
    # print("#########################")
    # print(f"pos_val {pos_val}")
    # print(f"pos to check {pos}")
    new_pos = []
    if x > 0 and arr[y][x-1] == pos_val:
        new_pos.append((x-1, y))
    if x < len(arr[0]) - 1 and arr[y][x+1] == pos_val:
        new_pos.append((x+1, y))
    if y > 0 and arr[y-1][x] == pos_val:
        new_pos.append((x, y-1))
    if y < len(arr) - 1 and arr[y+1][x] == pos_val:
        new_pos.append((x, y+1))
    print(pos)
    print(len(new_pos))
    print(new_pos)
    for n_pos in new_pos:
        print(arr[n_pos[1]][n_pos[0]])
    # assert len(new_pos) <= 3
    # print(f"new pos {new_pos}")
    for n_pos in new_pos:
        assert arr[n_pos[1]][n_pos[0]] == arr[y][x] + 1, "dsddddd"
    return new_pos


def count_paths(map_int, positions):
    paths_found = 0
    while len(positions) > 0:
        # print("####################")
        # print(f"pos bef {positions}")
        curr_val = positions.pop()
        # print(f"pos aft {positions}")
        # print(f"curr pos {curr_val}")
        if map_int[curr_val[1]][curr_val[0]] == 9:
            # print(f"new path {map_int[curr_val[1]][curr_val[0]]}")
            # print("f")
            # print(f"set {paths_found}")
            paths_found += 1
            # paths_found.add(curr_val)
            # print(f"set {paths_found}")
        else:
            # print(f"bef extension {positions}")
            positions.extend(get_new_elems(map_int, curr_val))
            # print(f"aft extension {positions}")
    return paths_found


with open("input.txt", 'r') as input_file:
    topo_map = []
    starting_pos = []
    nines = 0
    for y, line in enumerate(input_file):
        line_int = list(map(int, list(line.rstrip())))
        for x, val in enumerate(line_int):
            if val == 0:
                starting_pos.append((x, y))
            if val == 9:
                nines += 1
        topo_map.append(line_int)
    for pos in starting_pos:
        print(topo_map[pos[1]][pos[0]])
    print(len(starting_pos))
    paths = 0
    for pos in starting_pos:
        p_new = count_paths(topo_map, [pos])
        # print(f"p_new {p_new}")

        paths += p_new
    print(paths)
    # print(starting_pos)
