
def get_file_space(arr, idx):
    id = arr[idx]
    space = 0
    while arr[idx] == id:
        space += 1
        idx -= 1
    return space


def find_free_space(arr, space, id):
    i = 0
    space_start = 0
    free_space = 0
    while i < len(arr):
        if arr[i] == id:
            # print("no space found in range")
            return -1
        if arr[i] == -1:
            if free_space == 0:
                space_start = i
            free_space += 1
            # print(f"current free space = {free_space}")
            if free_space >= space:
                return space_start
        else:
            free_space = 0
            space_start = 0
        i += 1
    # print("end ogf loop this should no happen")
    return -1


with open("input.txt", 'r') as input_file:
    vals = list(map(int, list(input_file.read().rstrip())))
    # print(vals)
    id_array = []
    curr_id = 0
    for i, val in enumerate(vals):
        if i % 2 == 0:
            id_array.extend([curr_id] * val)
            curr_id += 1
        else:
            id_array.extend([-1] * val)
    file_idx = len(id_array) - 1
    id = 0
    # print(id_array)
    while id_array[file_idx] == -1:
        file_idx -= 1
    id = id_array[file_idx] + 1
    file_idx = len(id_array) - 1

    while file_idx > 0:
        if id_array[file_idx] == -1:
            file_idx -= 1
        elif id_array[file_idx] >= id:
            file_idx -= 1
        else:
            id = id_array[file_idx]
            print("")
            # print(f"file to reposotion {id}")
            file_space = get_file_space(id_array, file_idx)
            # print(f"file size = {file_space}")
            free_idx = find_free_space(id_array, file_space, id)
            # print(f"free space starting at {free_idx}")
            if free_idx != -1:
                for i in range(file_space):
                    id_array[free_idx + i] = id
                    id_array[file_idx - i] = -1
                file_idx -= file_space

    for i in range(len(id_array)):
        if id_array[i] == -1:
            id_array[i] = 0
    # print(id_array)
    print(sum([value * index for index, value in enumerate(id_array)]))
