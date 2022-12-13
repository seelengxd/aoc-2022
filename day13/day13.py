from itertools import groupby, zip_longest

with open("day13.txt") as f:
    data = [line.strip() for line in f]
    stuff = [list(y) for x, y in groupby(data, key=lambda i: i == '') if not x]


def compare(left, right):
    # 1 means wrong 0 means same -1 means right
    if type(left) == int and type(right) == int:
        if left == right:
            return 0
        elif left < right:
            return -1
        else:
            return 1
    elif type(left) == int or type(right) == int:
        if type(right) == int:
            right = [right]
        if type(left) == int:
            left = [left]
        return compare(left, right)
    else:
        for i, j in zip_longest(left, right):
            if i == None:
                return -1
            elif j == None:
                return 1
            else:
                c = compare(i, j)
                if c:
                    return c
        return 0


ans = 0
for i, (a, b) in enumerate(stuff, 1):
    a = eval(a)
    b = eval(b)
    if compare(a, b) == -1:
        ans += i

print("Part 1:", ans)

# Part 2:
data2 = []
for line in data:
    if line:
        data2.append(eval(line))

data2.append([[2]])
data2.append([[6]])

for i in range(len(data2) - 1):
    for j in range(len(data2) - 1 - i):
        if compare(data2[j], data2[j + 1]) == 1:
            data2[j], data2[j + 1] = data2[j + 1], data2[j]

print("Part 2:", (data2.index([[2]]) + 1) * (data2.index([[6]]) + 1))
