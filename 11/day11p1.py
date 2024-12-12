

def stone_behaviour(stone):
    # print(f"curr stone {stone}")
    stone_list = list(str(stone))
    num_digits = len(stone_list)
    if stone == 0:
        return 1
    elif num_digits % 2 == 0:
        mid = num_digits // 2
        return [int(''.join(stone_list[:mid])), int(''.join(stone_list[mid:]))]
    else:
        return stone * 2024


def blink(stones):
    new_stones = []
    for elem in stones:
        new_elem = stone_behaviour(elem)
        # print(f" new_elem {new_elem}")
        if isinstance(new_elem, int):
            new_stones.append(new_elem)
        else:
            new_stones.extend(new_elem)
    return new_stones


with open("input-small.txt", 'r') as input_file:
    stones_input = list(map(int, input_file.read().rstrip().split(" ")))
    stones = stones_input
    for i in range(75):
        print(f"blink {i+1}")
        stones = blink(stones)
        # print(f"stones {stones}")
    print(f"part1 res: {len(stones)}")
    # stones = stones_input
    # for i in range(75):
    # print(f"blink {i+1}")
    # stones = blink(stones)
    # print(f"stones {stones}")
    # print(f"part2 res: {len(stones)}")
