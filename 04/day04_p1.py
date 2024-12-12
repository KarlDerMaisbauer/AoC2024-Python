
def check_rows(sub_matrix):
    counter = 0
    for row in sub_matrix:
        if row[0] == 'X' and row[1] == 'M' and row[2] == 'A' and row[3] == 'S':
            print(f"row1 {row}")
            counter += 1
        elif row[3] == 'X' and row[2] == 'M' and row[1] == 'A' and row[0] == 'S':
            print(f"row2 {row}")
            counter += 1
    return counter


def check_cols(sub_matrix):
    counter = 0
    for col_idx in range(4):
        if sub_matrix[0][col_idx] == 'X' and sub_matrix[1][col_idx] == 'M' and sub_matrix[2][col_idx] == 'A' and sub_matrix[3][col_idx] == 'S':
            print(f"col1 {col_idx}")
            print(f"[{sub_matrix[0][col_idx]},{sub_matrix[1][col_idx]},{
                  sub_matrix[2][col_idx]},{sub_matrix[3][col_idx]},]")
            counter += 1
        elif sub_matrix[3][col_idx] == 'X' and sub_matrix[2][col_idx] == 'M' and sub_matrix[1][col_idx] == 'A' and sub_matrix[0][col_idx] == 'S':
            print(f"col2 {col_idx}")
            counter += 1
    return counter


def check_array(arr):
    assert (len(arr) == 4)
    counter = 0
    if arr[0] == 'X' and arr[1] == 'M' and arr[2] == 'A' and arr[3] == 'S':
        counter += 1
    if arr[3] == 'X' and arr[2] == 'M' and arr[1] == 'A' and arr[0] == 'S':
        counter += 1
    return counter


def check_diagonals(sub_matrix):
    counter = 0
    if sub_matrix[0][0] == 'X' and sub_matrix[1][1] == 'M' and sub_matrix[2][2] == 'A' and sub_matrix[3][3] == 'S':
        print("diag1")
        counter += 1
    if sub_matrix[3][3] == 'X' and sub_matrix[2][2] == 'M' and sub_matrix[1][1] == 'A' and sub_matrix[0][0] == 'S':
        print("diag2")
        counter += 1
    if sub_matrix[0][3] == 'X' and sub_matrix[1][2] == 'M' and sub_matrix[2][1] == 'A' and sub_matrix[3][0] == 'S':
        print("diag3")
        counter += 1
    if sub_matrix[3][0] == 'X' and sub_matrix[2][1] == 'M' and sub_matrix[1][2] == 'A' and sub_matrix[0][3] == 'S':
        print("diag4")
        counter += 1
    return counter


def check_sub_matrix(sub_matrix):
    assert (len(sub_matrix) == 4)
    assert (len(sub_matrix[0]) == 4)
    # print("fdsgfdfddfgdf")
    # for r in sub_matrix:
    # print(r)

    counter = 0
    counter += check_rows(sub_matrix)
    counter += check_cols(sub_matrix)
    counter += check_diagonals(sub_matrix)
    # print(counter)
    return counter


with open("input.txt", 'r') as file:
    matrix = []
    for line in file:
        chars = list(line)
        chars.pop()
        matrix.append(chars)
    # print(matrix)
    counter = 0
    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            # print(f"col: {col} {len(matrix)}, row: {row} {len(matrix[0])}")
            # counter += check_sub_matrix([row[col:col+4]
            # for row in matrix[row:row+4]])
            if col < len(matrix) - 3:
                counter += check_array(matrix[row][col:col+4])
            if row < len(matrix[0])-3:
                counter += check_array([rown[col]
                                       for rown in matrix[row:row+4]])
            if col < len(matrix) - 3 and row < len(matrix[0])-3:
                counter += check_diagonals([row[col:col+4]
                                            for row in matrix[row:row+4]])

            # print(f"sub = \n {[row[col:col+4] for row in matrix[row:row+4]]}")
            # print(f"sub row = \n {matrix[row][col:col+4]}")
            # print(f"col row = \n {[rown[col] for rown in matrix[row:row+4]]}")
            # counter += check_array()

    print(counter)
