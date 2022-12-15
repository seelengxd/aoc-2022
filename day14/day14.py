with open("day14.txt") as f:
    data = [line.strip() for line in f]

STARTING = (500, 0)


def parse_rocks():
    m = set()
    for line in data:
        coords = [list(map(int, coord.split(',')))
                  for coord in line.split(' -> ')]
        for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    m.add((i, j))
    return m


def solve1():
    def can_go(x, y):
        return (x, y) not in m
    m = parse_rocks()
    max_depth = max(m, key=lambda i: i[1])[1]
    sand = 0
    a, b = STARTING
    while True:
        if b == max_depth:
            break
        if can_go(a, b + 1):
            b = b + 1
        elif can_go(a - 1, b + 1):
            a = a - 1
            b = b + 1
        elif can_go(a + 1, b + 1):
            a = a + 1
            b = b + 1
        else:
            m.add((a, b))
            sand += 1
            a, b = 500, 0

    return sand


def solve2():
    def can_go(x, y):
        return (x, y) not in m and y != max_depth + 2
    m = parse_rocks()
    max_depth = max(m, key=lambda i: i[1])[1]
    sand = 0
    a, b = STARTING
    while True:
        if can_go(a, b + 1):
            b = b + 1
        elif can_go(a - 1, b + 1):
            a = a - 1
            b = b + 1
        elif can_go(a + 1, b + 1):
            a = a + 1
            b = b + 1
        else:
            m.add((a, b))
            sand += 1
            if ((a, b) == (500, 0)):
                break
            a, b = 500, 0

    return sand


print("Part 1:", solve1())
print("Part 2:", solve2())
