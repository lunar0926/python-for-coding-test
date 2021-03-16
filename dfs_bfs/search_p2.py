## 입력 받기
n, m = map(int, input().split()) # 미로 크기 
maze = [] # 미로
for _ in range(n):
    maze.append(list(map(int, input()))) # 2차원 리스트로 미로를 입력받기 
## 변수 선언
x, y = 0, 0 # 동빈이의 시작 위치 (1, 1)을 2차원 리스트에 맞게  
endX = n - 1 # 출구의 좌표
endY = m - 1
result = 1 # 밟은 칸 개수. 시작 위치 포함 
## 메인 코드 
while(True):
    # 동빈이가 출구를 방문하면 break 
    if x == endX and y == endY:
        break 
    if y + 1 <= m - 1 and maze[x][y+1] == 1: # 오른쪽 이동
        y += 1
        result += 1
        continue
    elif x + 1 <= n -1 and maze[x+1][y] == 1: # 아래쪽 이동
        x += 1
        result += 1
        continue
    elif y - 1 >= 0 and maze[x][y-1] == 1: # 왼쪽 이동
        y -= 1
        result += 1
        continue
    elif x - 1 >= 0 and maze[x-1][y] == 1: # 위쪽 이동
        x -= 1
        result += 1
        continue
     


print(result)

'''
5 6
101010
111111
000001
111111
111111
'''