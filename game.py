import msvcrt
import random
import time

grid = [["ㆍ" for _ in range(4)] for _ in range(4)]

def Create_Goal() -> None:
    grid[3][3] = "G"

def Create_Hole(difficult: int) -> None:
    hole_num = [2, 4, 6]
    hole_cnt = 0
    while hole_cnt < hole_num[difficult]:
        x = random.randrange(4)
        y = random.randrange(4)
        if not grid[x][y] == "H" and not grid[x][y] == "G":
            grid[x][y] = "H"
            hole_cnt += 1

def find_root() -> bool:
    can_go_x = [0, 0, 1, -1]
    can_go_y = [-1, 1, 0, 0]

Create_Goal()
Create_Hole(1)
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



while True:
    pass