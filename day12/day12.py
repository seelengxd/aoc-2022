from collections import deque

with open("day12.txt") as f:
    data = [list(line.strip()) for line in f]
    n = len(data)
    m = len(data[0])


def can_go(i, j, current_ev):
    return 0 <= i < n and 0 <= j < m and ord(current_ev) + 1 >= ord(data[i][j])


def solve(starting_characters, data):
    start = []
    end = None
    queue = deque()
    memo = {}

    for i in range(n):
        for j in range(m):
            if data[i][j] in starting_characters:
                start.append((i, j))
                data[i][j] = 'a'
            elif data[i][j] == 'E':
                end = (i, j)
                data[i][j] = 'z'

    for s in start:
        queue.append((s, 0))

    while queue:
        coords, dist = queue.popleft()
        x, y = coords
        if coords == end:
            return dist
        if coords not in memo:
            memo[coords] = dist
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                if can_go(x + dx, y + dy, data[x][y]):
                    queue.append(((x + dx, y + dy), dist + 1))


print("Part 1:", solve(['S'], [row[:] for row in data]))
print("Part 2:", solve(['S', 'a'], [row[:] for row in data]))
