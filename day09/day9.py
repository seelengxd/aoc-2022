with open("day9.txt") as f:
    data = [line.strip() for line in f]

DIRECTION_MAP = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def update(head: list[int], tail: list[int]) -> bool:
    hx, hy = head
    tx, ty = tail

    # don't update if touching
    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
        return False

    if hx != tx and hy != ty:
        # diagonal movement
        tx += 1 if tx < hx else -1
        ty += 1 if ty < hy else -1

    elif hx == tx:
        ty += 1 if ty < hy else -1
    else:
        tx += 1 if tx < hx else -1

    tail[0] = tx
    tail[1] = ty
    return True


def solve(knots: int) -> int:
    coords = [[0, 0] for _ in range(knots + 1)]
    head = coords[0]
    visited = {(0, 0)}
    for line in data:
        d, n = line.split()
        n = int(n)
        dx, dy = DIRECTION_MAP[d]
        for i in range(n):
            # move the head
            head[0] += dx
            head[1] += dy
            for j in range(knots):
                # then update all subsequent knots
                updated = update(coords[j], coords[j + 1])
                # and add to visited if the last knot moved
                if j == knots - 1 and updated:
                    visited.add(tuple(coords[knots]))

    return len(visited)


print("Part 1:", solve(1))
print("Part 2:", solve(9))
