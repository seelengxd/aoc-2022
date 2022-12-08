with open("day8.txt") as f:
    data = [line.strip() for line in f]


def visible(row):
    n = len(row)
    res = [0] * n
    res[0] = 1
    res[-1] = 1
    curr_max = row[0]
    for i in range(1, n):
        if row[i] > curr_max:
            res[i] = 1
            curr_max = row[i]

    curr_max = row[-1]
    for i in range(n - 2, -1, -1):
        if row[i] > curr_max:
            res[i] = 1
            curr_max = row[i]

    return res


result = [visible(row) for row in data]

n = len(data)
m = len(data[0])
for i in range(m):  # i is the column index
    column_res = visible([data[j][i] for j in range(n)])
    for j in range(n):
        result[j][i] = max(column_res[j], result[j][i])

print("Part 1:", sum(sum(row) for row in result))


def can_go(x, y, c):
    return 0 <= x < n and 0 <= y < m and data[x][y] < c


def score(i, j):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    res = 1
    for dx, dy in directions:
        cx, cy = i, j
        curr = 0
        while can_go(cx + dx, cy + dy, data[i][j]):
            cx += dx
            cy += dy
            curr += 1
        res *= curr + (0 <= cx + dx < n and 0 <= cy + dy < m)
    return res


print("Part 2:", max(score(i, j) for i in range(n) for j in range(m)))
