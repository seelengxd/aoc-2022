import string

LETTERS = string.ascii_lowercase + string.ascii_uppercase

def priority(item):
    return LETTERS.index(item) + 1

def get_common(*parts):
    result = set(parts[0])
    for part in parts[1:]:
        result = result.intersection(set(part))
    return result.pop()

with open("day3.txt") as f:
    data = [line.strip() for line in f]

def solve():
    part_1 = 0
    for bag in data:
        length = len(bag)
        left, right = bag[:length // 2], bag[length // 2:]
        part_1 += priority(get_common(left, right))
    print(f"Part 1: {part_1}")

    iter_data = iter(data)
    part_2 = 0
    for first, second, third in zip(iter_data, iter_data, iter_data):
        part_2 += priority(get_common(first, second, third)) 
    print(f"Part 2: {part_2}")

solve()
    

