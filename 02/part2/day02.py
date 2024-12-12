
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


def generate_missing_item_lists(original_list):
    return [original_list[:i] + original_list[i+1:] for i in range(len(original_list))]


with open("input.txt", 'r') as input:
    list1 = []
    safe_squences = 0
    length = 0
    for line in input:
        length += 1
        parts = line.strip().split()
        sequence = list(map(int, parts))
        sequences = generate_missing_item_lists(sequence)
        for s in sequences:
            if is_save(s):
                safe_squences += 1
                break

    print(safe_squences)
    print(length)
