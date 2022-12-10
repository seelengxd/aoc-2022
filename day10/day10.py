with open("day10.txt") as f:
    data = [line.strip() for line in f]

X = 1
cycle = 1
d = {}
for line in data:
    d[cycle] = X
    if line == "noop":
        cycle += 1
    else:
        _, num = line.split()
        num = int(num)
        d[cycle + 1] = X
        X += num
        cycle += 2

targets = [20, 60, 100, 140, 180, 220]
ans = 0

for target in targets:
    ans += d[target] * target
print("Part 1:", ans)

mat = [['.'] * 40 for _ in range(6)]
for i in range(240):
    pos = d[i + 1]
    if pos - 1 <= i % 40 <= pos + 1:
        mat[i // 40][i % 40] = '#'
    
print("Part 2:")
for row in mat:
    print(''.join(row))
