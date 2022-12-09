import msvcrt

def getKey() -> str:
    buf = msvcrt.getch()
    print("test", list(buf))
    if list(buf) == [224]:
        a = list(msvcrt.getch())[0]
        if a == 72: return "up"
        elif a == 75: return "left"
        elif a == 77: return "right"
        elif a == 80: return "down"
    elif list(buf) == [13]:
        return "enter"

while True:
    print(getKey())