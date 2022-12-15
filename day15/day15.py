import re


def man(x1, x2, y1, y2):
    return abs(x2-x1) + abs(y2-y1)


with open("day15.txt") as f:
    data = [line.strip() for line in f]
    data = [list(map(int, re.findall(
        "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)[0])) for line in data]
    data = [(sx, sy, man(sx, bx, sy, by)) for sx, sy, bx, by in data]


def get_interval(sx, sy, d, y):
    side = d - abs(sy - y)
    if side < 0:
        return None, None
    return sx - side, sx + side


def get_merged_intervals(y):
    intervals = [get_interval(sx, sy, d, y) for sx, sy, d in data]
    intervals = [
        interval for interval in intervals if interval != (None, None)]
    intervals.sort()

    # merge intervals
    merged = []
    cs, ce = intervals[0]
    for s, e in intervals[1:]:
        if s > ce:
            merged.append((cs, ce))
            cs, ce = s, e
        else:
            ce = max(e, ce)
    merged.append((cs, ce))

    return merged


def part1():
    intervals = get_merged_intervals(2000000)
    # consider the one beacon with this y
    ans = -1  
    for a, b in intervals:
        ans += b - a + 1
    return ans


def part2():
    for y in range(4000001):
        merged = get_merged_intervals(y)
        filtered = [(max(0, s), min(e, 4000000))
                    for s, e in merged if s <= 4000000]
        if len(filtered) != 1 or filtered[0][0] != 0:
            x = filtered[0][1] + 1
            return x * 4000000 + y


print("Part 1:", part1())
print("Part 2:", part2())
