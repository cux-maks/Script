import msvcrt
import random
import time
import copy
import os

grid = list() # 맵
map_size = {"작음" : 4, "중간" : 5, "큼" : 6, "짱큼" : 7} # 맵 크기 dict
dif = {"쉬움" : 0, "중간" : 1, "어려움" : 2, "극악" : 3} # 난이도 dict

now_x = 0 # 현재위치(시작위치) 초기화
now_y = 0 # 현재위치(시작위치) 초기화

def Create_grid(n: int) -> None: # 크기에 따른 맵 생성
    global grid
    grid = [[" " for _ in range(n)] for _ in range(n)]

def Create_Start(x = 0, y = 0) -> None: # 시작지점 설정
    global grid
    grid[x][y] = "me"

def Create_Goal(n) -> None: # 도착지점 설정
    global grid
    grid[n - 1][n - 1] = "goal"

def Create_Hole(difficult: int, s: int) -> None:
    hole_num = [0.2, 0.3, 0.4, 0.5]
    hole_cnt = 0
    while hole_cnt < int(s*s*hole_num[difficult]):
        x = random.randrange(s)
        y = random.randrange(s)
        if not grid[x][y] == "hole" and not grid[x][y] == "goal" and not grid[x][y] == "me":
            grid[x][y] = "hole"
            hole_cnt += 1

def Delete_Hole(n: int) -> None:
    for x in range(n):
        for y in range(n):
            if grid[x][y] == "hole": grid[x][y] = " "

def find_root(n: int) -> bool:
    visited = []
    visited.append((0, 0))

    grid_test = copy.deepcopy(grid)

    while not len(visited) == 0:
        here = visited.pop()
        (x, y) = here
        if grid_test[x][y] == "goal": return True
        else:
            grid_test[x][y] = "me"
            if (x >= 0 and x < n and y - 1 >= 0 and y - 1 < n) and (grid_test[x][y - 1] == " " or grid_test[x][y - 1] == "goal"): visited.append((x, y - 1))
            if (x - 1 >= 0 and x - 1 < n and y >= 0 and y < n) and (grid_test[x - 1][y] == " " or grid_test[x - 1][y] == "goal"): visited.append((x - 1, y))
            if (x >= 0 and x < n and y + 1 >= 0 and y + 1 < n) and (grid_test[x][y + 1] == " " or grid_test[x][y + 1] == "goal"): visited.append((x, y + 1))
            if (x + 1 >= 0 and x + 1 < n and y >= 0 and y < n) and (grid_test[x + 1][y] == " " or grid_test[x + 1][y] == "goal"): visited.append((x + 1, y))

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

def move(direction: str, n: int) -> None:
    global now_y
    global now_x
    if direction == "up":
        if now_y >= 1: now_y -= 1
    elif direction == "down":
        if now_y < n: now_y += 1
    elif direction == "right":
        if now_x < n: now_x += 1
    elif direction == "left":
        if now_x >= 1: now_x -= 1
    elif direction == None: pass

def change_position(n: int) -> str:
    global grid
    ret = "None"
    for x in range(n):
        for y in range(n):
            if grid[x][y] == "me": grid[x][y] = " "

    if grid[now_y][now_x] == "hole":
        grid[now_y][now_x] = "die"
        ret = "Game Over"
    elif grid[now_y][now_x] == "goal":
        grid[now_y][now_x] = "clear"
        ret = "Game Clear"
    elif grid[now_y][now_x] == " ":
        grid[now_y][now_x] = "me"

    return ret

def print_grid(diff: str, gm: int, grid_s: int) -> None:
    os.system("cls")
    gm_list = ["직접 플레이", "랜덤 입력"]
    print(f"난이도: {diff} / 게임모드: {gm_list[gm]} / 맵 크기 {grid_s} x {grid_s}")
    print()
    print("  " + "🧱" * (6 * grid_s + 1))
    for x in grid:
        print("  🧱  ", end = "")
        for item in x:
            if item == " ":
                print("      ", end = "")
            elif item == "hole":
                print("      ", end = "")
            elif item == "goal":
                print("      ", end = "")
            elif item == "me":
                print("      ", end = "")
            elif item == "die":
                print("      ", end = "")
            elif item == "clear":
                print("      ", end = "")
            print("  🧱  ", end = "")
        print()
        print("  🧱  ", end = "")
        for item in x:
            if item == " ":
                print("      ", end = "")
            elif item == "hole":
                print("☣    ☣", end = "")
            elif item == "goal":
                print("💊  💊", end = "")
            elif item == "me":
                print("  😷  ", end = "")
            elif item == "die":
                print("  😵  ", end = "")
            elif item == "clear":
                print("  😄  ", end = "")
            print("  🧱  ", end = "")
        print()
        print("  🧱  ", end = "")
        for item in x:
            if item == " ":
                print("      ", end = "")
            elif item == "hole":
                print("  🦠  ", end = "")
            elif item == "goal":
                print("  💉  ", end = "")
            elif item == "me":
                print("👋🥼🤜", end = "")
            elif item == "die":
                print("☠ 🥋 ☠", end = "")
            elif item == "clear":
                print("👋🥼🤳", end = "")
            print("  🧱  ", end = "")
        print()
        print("  🧱  ", end = "")
        for item in x:
            if item == " ":
                print("      ", end = "")
            elif item == "hole":
                print("☣    ☣", end = "")
            elif item == "goal":
                print("💊  💊", end = "")
            elif item == "me":
                print(" 👞👞 ", end = "")
            elif item == "die":
                print(" ☠  ☠ ", end = "")
            elif item == "clear":
                print(" 👞👞 ", end = "")
            print("  🧱  ", end = "")
        print()
        print("  🧱  ", end = "")
        for item in x:
            if item == " ":
                print("      ", end = "")
            elif item == "hole":
                print("      ", end = "")
            elif item == "goal":
                print("      ", end = "")
            elif item == "me":
                print("      ", end = "")
            elif item == "die":
                print("      ", end = "")
            elif item == "clear":
                print("      ", end = "")
            print("  🧱  ", end = "")
        print()
        print("  " + "🧱" * (6 * grid_s + 1))

while True:

    os.system("cls")

    now_x = 0
    now_y = 0

    while True:
        print("맵 크기를 입력하시오. (작음, 중간, 큼, 짱큼)")
        input_mapSize = str(input())

        if input_mapSize not in map_size:
            print("다시 입력해 주세요")
            os.system("pause")
            os.system("cls")
        else:
            Create_grid(map_size[input_mapSize])
            break

    print()

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
    Create_Goal(map_size[input_mapSize])

    while True:
        Delete_Hole(map_size[input_mapSize])
        Create_Hole(n, map_size[input_mapSize])
        if find_root(map_size[input_mapSize]): break

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
    time.sleep(1)
    os.system("cls")
    print_grid(input_dif, gameMode - 1, map_size[input_mapSize])

    ret_val = None

    while True:
        if gameMode == 1:
            move(getKey(), map_size[input_mapSize])
        elif gameMode == 2:
            move(getKey_random(), map_size[input_mapSize])
            time.sleep(0.5)
        val = change_position(map_size[input_mapSize])
        print_grid(input_dif, gameMode - 1, map_size[input_mapSize])
        if val == "Game Over":
            print("Game Over....")
            print("다시 시작하시겠습니까? (네/아니요)")
            re_val = str(input())
            break
        elif val == "Game Clear":
            print("Game Clear!!")
            print("새로운 게임을 시작하시겠습니까? (네/아니요)")
            re_val = str(input())
            break
    
    if re_val == "아니요": break