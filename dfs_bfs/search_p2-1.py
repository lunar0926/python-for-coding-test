from collections import deque
# 입력받기
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))
 
## 변수
x, y = 0, 0 # 동빈이의 위치 
endX = n - 1 # 출구의 좌표 
endY = m - 1 
result = 0 # 출력할 값. 최소 칸의 개수
queueX = deque() # 큐 자료구조 만들기
queueY = deque()
## 시작 위치 큐에 넣기
queueX.append(x)
queueY.append(y)

while(True):
    if maze[queueX.popleft()][queueY.popleft()] == 1:
        