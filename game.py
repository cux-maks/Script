import msvcrt
import random
import time
import copy
import os

grid = [["ㆍ" for _ in range(4)] for _ in range(4)]

now_x = 0
now_y = 0

def Create_Start(x = 0, y = 0) -> None:
    grid[x][y] = "☆"

def Create_Goal(x = 3, y = 3) -> None:
    grid[3][3] = "G"

def Create_Hole(difficult: int) -> None:
    hole_num = [2, 4, 6]
    hole_cnt = 0
    while hole_cnt < hole_num[difficult]:
        x = random.randrange(4)
        y = random.randrange(4)
        if not grid[x][y] == "H" and not grid[x][y] == "G" and not grid[x][y] == "☆":
            grid[x][y] = "H"
            hole_cnt += 1

def Delete_Hole() -> None:
    for x in range(4):
        for y in range(4):
            if grid[x][y] == "H": grid[x][y] = "ㆍ"

def find_root() -> bool:
    visited = []
    visited.append((0, 0))

    grid_test = copy.deepcopy(grid)

    while not len(visited) == 0:
        here = visited.pop()
        (x, y) = here
        if grid_test[x][y] == "G": return True
        else:
            grid_test[x][y] = "☆"
            if (x >= 0 and x < 4 and y - 1 >= 0 and y - 1 < 4) and (grid_test[x][y - 1] == "ㆍ" or grid_test[x][y - 1] == "G"): visited.append((x, y - 1))
            if (x - 1 >= 0 and x - 1 < 4 and y >= 0 and y < 4) and (grid_test[x - 1][y] == "ㆍ" or grid_test[x - 1][y] == "G"): visited.append((x - 1, y))
            if (x >= 0 and x < 4 and y + 1 >= 0 and y + 1 < 4) and (grid_test[x][y + 1] == "ㆍ" or grid_test[x][y + 1] == "G"): visited.append((x, y + 1))
            if (x + 1 >= 0 and x + 1 < 4 and y >= 0 and y < 4) and (grid_test[x + 1][y] == "ㆍ" or grid_test[x + 1][y] == "G"): visited.append((x + 1, y))

    return False

n = 1

Create_Start()
Create_Goal()

while True:
    Delete_Hole()
    Create_Hole(n)
    if find_root(): break

for x in grid:
    print(x)

def getKey() -> str:
    if list(msvcrt.getch()) == [224]:
        a = list(msvcrt.getch())[0]
        if a == 72: return "up"
        elif a == 75: return "left"
        elif a == 77: return "right"
        elif a == 80: return "down"

def getKey_random() -> str:
    retValue = ["up", "down", "left", "right"]
    return retValue[random.randrange(0, 4)]

def move(direction: str) -> None:
    global now_y
    global now_x
    if direction == "up":
        if now_y >= 1: now_y -= 1
    elif direction == "down":
        if now_y < 3: now_y += 1
    elif direction == "right":
        if now_x < 3: now_x += 1
    elif direction == "left":
        if now_x >= 1: now_x -= 1
    elif direction == None: pass
    change_position()

def change_position() -> None:
    for x in range(4):
        for y in range(4):
            if grid[x][y] == "☆": grid[x][y] = "ㆍ"
    grid[now_y][now_x] = "☆"

def print_grid() -> None:
    os.system("cls")
    for x in grid:
        print(x)

while True:
    move(getKey())
    print_grid()