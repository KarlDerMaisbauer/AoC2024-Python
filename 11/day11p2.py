

def stone_behaviour(stone):
    stone_list = list(str(stone))
    num_digits = len(stone_list)
    if stone == 0:
        return 1
    elif num_digits % 2 == 0:
        mid = num_digits // 2
        return [int(''.join(stone_list[:mid])), int(''.join(stone_list[mid:]))]
    else:
        return stone * 2024


res_map = {}


def blink_recursive(stone, blinks_rem):
    if blinks_rem == 0:
        return 1
    else:
        if (stone, blinks_rem) in res_map:
            return res_map[(stone, blinks_rem)]
        new = stone_behaviour(stone)
        if isinstance(new, int):
            res = blink_recursive(new, blinks_rem-1)
            res_map[(stone, blinks_rem)] = res
            return res
        else:
            res = blink_recursive(new[0], blinks_rem-1) + \
                blink_recursive(new[1], blinks_rem-1)
            res_map[(stone, blinks_rem)] = res
            return res


with open("input.txt", 'r') as input_file:
    stones_input = list(map(int, input_file.read().rstrip().split(" ")))
    stones = stones_input
    stone_count = 0
    for (i, stone) in enumerate(stones):

        stone_count += blink_recursive(stone, 75)
    print(f"part2 res: {stone_count}")
