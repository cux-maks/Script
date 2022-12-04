import msvcrt
import random
import time
import copy
import os

grid = [[" " for _ in range(4)] for _ in range(4)]
dif = {"쉬움" : 0, "중간" : 1, "어려움" : 2, "극악" : 3}

now_x = 0
now_y = 0

def Create_Start(x = 0, y = 0) -> None:
    grid[x][y] = "★"

def Create_Goal(x = 3, y = 3) -> None:
    grid[3][3] = "◆"

def Create_Hole(difficult: int) -> None:
    hole_num = [2, 4, 6, 9]
    hole_cnt = 0
    while hole_cnt < hole_num[difficult]:
        x = random.randrange(4)
        y = random.randrange(4)
        if not grid[x][y] == "□" and not grid[x][y] == "◆" and not grid[x][y] == "★":
            grid[x][y] = "□"
            hole_cnt += 1

def Delete_Hole() -> None:
    for x in range(4):
        for y in range(4):
            if grid[x][y] == "□": grid[x][y] = " "

def find_root() -> bool:
    visited = []
    visited.append((0, 0))

    grid_test = copy.deepcopy(grid)

    while not len(visited) == 0:
        here = visited.pop()
        (x, y) = here
        if grid_test[x][y] == "◆": return True
        else:
            grid_test[x][y] = "★"
            if (x >= 0 and x < 4 and y - 1 >= 0 and y - 1 < 4) and (grid_test[x][y - 1] == " " or grid_test[x][y - 1] == "◆"): visited.append((x, y - 1))
            if (x - 1 >= 0 and x - 1 < 4 and y >= 0 and y < 4) and (grid_test[x - 1][y] == " " or grid_test[x - 1][y] == "◆"): visited.append((x - 1, y))
            if (x >= 0 and x < 4 and y + 1 >= 0 and y + 1 < 4) and (grid_test[x][y + 1] == " " or grid_test[x][y + 1] == "◆"): visited.append((x, y + 1))
            if (x + 1 >= 0 and x + 1 < 4 and y >= 0 and y < 4) and (grid_test[x + 1][y] == " " or grid_test[x + 1][y] == "◆"): visited.append((x + 1, y))

    return False

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

def change_position() -> str:
    global grid
    ret = "None"
    for x in range(4):
        for y in range(4):
            if grid[x][y] == "★": grid[x][y] = " "

    if grid[now_y][now_x] == "□":
        grid[now_y][now_x] = "☆"
        ret = "Game Over"
    elif grid[now_y][now_x] == "◆":
        grid[now_y][now_x] = "★"
        ret = "Game Clear"
    elif grid[now_y][now_x] == " ":
        grid[now_y][now_x] = "★"

    return ret

def print_grid(diff: str, gm: int) -> None:
    os.system("cls")
    gm_list = ["직접 플레이", "랜덤 입력"]
    print(f"난이도: {diff} / 게임모드: {gm_list[gm]}")
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    for x in grid:
        print("| ", end = "")
        for y in x:
            print(y, end = " | ")
        print()
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print("너: ★")
    print("함정: □")
    print("목표: ◆")

while True:

    os.system("cls")

    now_x = 0
    now_y = 0

    while True:
        print("난이도를 입력하시오. (쉬움, 중간, 어려움, 극악)")
        input_dif = str(input())

        if input_dif not in dif:
            print("다시 입력해 주세요")
            os.system("pause")
            os.system("cls")
        else:
            n = dif[input_dif]
            break

    print()

    Create_Start()
    Create_Goal()

    while True:
        Delete_Hole()
        Create_Hole(n)
        # print_grid(input_dif, 0)
        # time.sleep(0.2)
        if find_root(): break

    # print_grid()

    while True:

        print(f"게임 모드를 선택하시오. (번호 입력) (난이도: {input_dif})")
        print("1. 직접 플레이")
        print("2. 랜덤 입력")

        gameMode = int(input())

        if not gameMode == 1 and not gameMode == 2:
            print("다시 입력하세요.")
            os.system("pause")
            os.system("cls")
        else:
            break

    print()

    print("게임을 시작합니다....")
    time.sleep(3)
    os.system("cls")
    print_grid(input_dif, gameMode - 1)

    ret_val = None

    while True:
        if gameMode == 1:
            move(getKey())
        elif gameMode == 2:
            move(getKey_random())
            time.sleep(1)
        val = change_position()
        print_grid(input_dif, gameMode - 1)
        if val == "Game Over":
            print("Game Over....")
            print("다시 시작하시겠습니까? (Y/N)")
            re_val = str(input())
            break
        elif val == "Game Clear":
            print("Game Clear!!")
            print("새로운 게임을 시작하시겠습니까? (Y/N)")
            re_val = str(input())
            break
    
    if re_val == "N": break