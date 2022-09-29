MAX_QSIZE = 8

map = [['1', '1', '1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '1', '1', '1', '0', 'x'],
       ['1', '1', '0', '1', '0', '1', '0', '1'],
       ['1', '1', '0', '1', '0', '1', '0', '1'],
       ['1', '0', '0', '0', '0', '0', '0', '1'],
       ['1', '1', '1', '1', '0', '1', '1', '1'],
       ['1', '0', '0', '0', '0', '0', '0', '1'],
       ['1', '1', '1', '1', '1', '1', '1', '1']]

class CircularQueue:
    # CircularQueue 생성자
    def __init__(self):
        # 큐의 전단 위치
        self.front = 0
        # 큐의 후단 위치
        self.rear = 0
        # 항목 저장용 리스트
        self.items = [None]*MAX_QSIZE
        
    # 공백 상태 검사
    def isEmpty(self):
        return self.front == self.rear
    # 포화 상태 검사
    def isFull(self):
        return self.front == (self.rear+1)%MAX_QSIZE
    # 초기화
    def clear(self):
        self.front = self.rear
        
    # 삽입
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    # 삭제
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    # peek
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    # 현재 큐에 저장된 항목의 개수
    def size(self):
        return (self.rear - self.front + MAX_QSIZE)%MAX_QSIZE
    
    # 출력
    def display(self):
        out = []
        if self.front < self.rear:
            # 슬라이싱
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
                + self.items[0:self.rear+1]
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 깊이우선탐색
# visited = [[False] * MAX_QSIZE] * MAX_QSIZE
visited = [[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False]]

# print(visited)

def DFS(x, y):    
    visited[x][y] = True
    here = x, y
    # print("here:", here, end='->\n')
    print(" ->", here, end='')
    
    if map[x][y] == 'x': 
        print(" --> 미로탐색 성공")
        return True
    else:        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print("next:", nx, ny)
            if (nx < 0 or nx >= MAX_QSIZE):
                # print('fail1:', nx, ny)
                continue
            if (ny < 0 or ny >= MAX_QSIZE):
                # print('fail2:', nx, ny)
                continue
            if visited[nx][ny] == True:
                # print('fail3:', nx, ny)
                # print(visited[nx][ny])
                continue
            if (map[nx][ny] == '0' or map[nx][ny] == 'x') and visited[nx][ny] == False:
                # visited[nx][ny] = True
                DFS(nx, ny)
                # visited[nx][ny] = False

print("DFS: ")
DFS(1, 0)