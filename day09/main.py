import time
import sys

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

# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
WIDTH = 1000
HEIGHT = 800
SCALE = 3
COLOUR_BROWN = (200, 120, 91)
COLOUR_WHITE = (255, 255, 255)
COLOUR_BLUE = (72, 209, 236)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
screen.fill(COLOUR_WHITE)

time.sleep(30)

knots = 9
coords = [[0, 0] for _ in range(knots + 1)]
visited = set()
head = coords[0]
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
            if j == knots - 1 and updated:
                visited.add(tuple(coords[-1]))

        screen.fill(COLOUR_WHITE)
        for x, y in visited:
            pygame.draw.circle(screen, COLOUR_BLUE, ((x + 25) * SCALE, (y + 150) * SCALE), 2)
        for x, y in coords:
            pygame.draw.circle(screen, COLOUR_BROWN, ((x + 25) * SCALE, (y + 150) * SCALE), 2)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(0.05)
        
    
pygame.quit()



