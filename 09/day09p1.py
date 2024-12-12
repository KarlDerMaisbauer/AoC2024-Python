
def can_reduce(arr):
    return -1 in arr


def reposition_last_block(arr):
    last = arr.pop()
    for i in range(len(arr)):
        if arr[i] == -1:
            arr[i] = last
            return arr
    assert False, "sdfsdf"


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
    while can_reduce(id_array):
        id_array = reposition_last_block(id_array)

    print(sum([value * index for index, value in enumerate(id_array)]))
