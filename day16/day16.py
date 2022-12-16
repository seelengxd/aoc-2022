import re
with open("day16.txt") as f:
    data = [line.strip() for line in f]
    data = [re.findall(
        "Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line)[0] for line in data]


# Data parsing
# Index only relevant for non-zero pressure valves

flow = {}
adj = {}
index = {}

i = 0
for v, f, edges in data:
    flow[v] = int(f)
    adj[v] = edges.split(", ")
    if flow[v]:
        index[v] = i
        i += 1

nz = len([i for i, v in flow.items() if v])

# Store valve open state as integer
# Use bitwise operations to open/close valves


def open_valve(v: str, valves: int):
    i = index[v]
    valves |= 2 << i
    return valves


def close_valve(v: str, valves: int):
    i = index[v]
    mask = 2 << nz
    mask -= 2 << v
    valves &= mask
    return valves


def is_valve_open(v: str, valves: int):
    i = index[v]
    return valves & (2 << i) != 0


def solve(time, elephant):
    stack = [("AA", 0, 0, time)]
    m = {}
    visited = {}
    cm = 0
    while stack:
        valve, opened, ans, time_left = stack.pop()
        if visited.get((valve, opened, ans), -1) >= time_left:
            continue
        visited[(valve, opened, ans)] = time_left
        m[opened] = max(m.get(opened, 0), ans)
        if not time_left or opened == ((2 << nz) - 1):
            if ans > cm:
                cm = ans
            continue

        if flow[valve] and not is_valve_open(valve, opened):
            stack.append((valve, open_valve(valve, opened), ans +
                         flow[valve] * (time_left - 1), time_left - 1))

        for edge in adj[valve]:
            stack.append((edge, opened, ans, time_left - 1))

    if not elephant:
        return cm

    ans = 0
    for i in m:
        for j in m:
            if not i & j:
                ans = max(m[i] + m[j], ans)

    return ans


print("Part 1:", solve(30, False))
print("Part 2:", solve(26, True))
