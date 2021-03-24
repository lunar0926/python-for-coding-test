from collections import deque
## 입력받기
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))
endX, endY = n-1, m-1 # 출구
# 위 오른쪽 아래 왼쪽 순으로 탐색
moveX = [-1, 0, 1, 0]
moveY = [0, 1, 0, -1]

x, y = 0, 0 # 동빈이의 시작 위치
queue = deque()
queue.append((x, y)) # 시작 위치를 큐에 삽입
# 큐가 빌 때까지 반복
while(queue):
    x, y = queue.popleft()
    for i in range(4):
        nx = x + moveX[i]
        ny = y + moveY[i]
        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1: # 범위를 벗어난 경우
            continue
        if maze[nx][ny] == 0: # 괴물이 있어서 이동 불가
            continue
        if maze[nx][ny] == 1: # 처음 가는 칸이고 이동 가능
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))
## 출력
print(maze[endX][endY])
'''
입력 예시
5 6 
101010
111111
000001
111111
111111
'''