

with open("input.txt", 'r') as input:
    list1 = []
    list2 = []
    for line in input:
        parts = line.strip().split()
        if len(parts) == 2:
            list1.append(int(parts[0]))
            list2.append(int(parts[1]))
    list1.sort()
    list2.sort()
    dist = 0
    for val in list1:
        occurence = (list2.count(val))
        dist += (val * occurence)
    print(dist)
