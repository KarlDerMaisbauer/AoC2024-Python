
def is_save(number_seq):
    first = number_seq[0]
    second = number_seq[1]
    if first < second:
        for i in range(1, len(number_seq), 1):
            item1 = number_seq[i-1]
            item2 = number_seq[i]
            diff = item2 - item1
            if diff < 1 or diff > 3:
                return False
    else:
        for i in range(1, len(number_seq), 1):
            item1 = number_seq[i-1]
            item2 = number_seq[i]
            diff = item1 - item2
            if diff < 1 or diff > 3:
                return False
    return True


with open("input.txt", 'r') as input:
    list1 = []
    safe_squences = 0
    length = 0
    for line in input:
        length += 1
        parts = line.strip().split()
        sequence = list(map(int, parts))
        if is_save(sequence):
            safe_squences += 1
    print(safe_squences)
    print(length)
