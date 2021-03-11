# 왼쪽 회전 함수
def turn_left():
    global direction # 전역함수로 만들어주기
    if direction == 0:
        direction = 3
    else:
        direction -= 1

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
# 맵 생성
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))
# 캐릭터가 가본 곳 체크하는 지도(못 가본 곳: 0, 가본 곳: 1)
check_map = [[0] * m for _ in range(n)]
check_map[x][y] = 1 # 시작 지점은 가본 곳으로 체크
count = 1 # 가본 칸 개수 세기(출력)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
turn_count = 0
while(True):
    turn_left()
    x = x + dx[direction]
    y = y + dy[direction]
    if check_map[x][y] == 0 and game_map[x][y] == 0: # 가보지 않은 곳이 있고 그 곳이 육지라면?
        check_map[x][y] = 1 #  가본 곳으로 체크
        count += 1
        turn_count = 0 # 다시 초기화
    else: # 가본 곳이거나 바다인 경우
        turn_count += 1
        # 미리 간 것 다시 돌아오기
        x = x - dx[direction]
        y = y - dy[direction]

    # 만약 네 방향 모두 이미 가본 칸이거나 바다인 경우
    if turn_count == 4:
        # 방향 유지한 채로 한 칸 뒤로
        x = x - dx[direction]
        y = y - dy[direction]
        if game_map[x][y] == 1: # 한 칸 뒤가 바다인 경우
            # 뒤로 못 돌아가고 움직임을 멈춤
            x = x + dx[direction]
            y = y + dy[direction]
            break
        else:
            turn_count = 0 # 회전 수 초기화
            continue

print(count)

'''
입력 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''