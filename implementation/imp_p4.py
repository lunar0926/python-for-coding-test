# 입력받기
n, m = map(int, input().split()) # n은 행, m은 열
character = list(map(int, input().split())) # 캐릭터의 행, 열, 방향을 리스트로 입력받기
maps = [] # 맵 생성
result = 0 # 이미 방문한 칸의 수
for i in range(n):
    maps.append(list(map(int, input().split())))
maps[character[0]][character[1]] = 2 # 캐릭터 시작 위치 2(방문)로 표시

def turn(): # 다음 번 회전 방향을 정하는 함수
    if character[2] == 0:
        character[2] == 3
    elif character[2] == 3 or character[2] == 2 or character[2] == 1:
        character[2] -= 1

# 캐릭터 이동 매뉴얼

while(True):

    if (maps[character[0]-1][character[1]] == 1 or maps[character[0]-1][character[1]] ==2) and (maps[character[0]][character[1]-1] == 1 or maps[character[0]][character[1]-1] == 2) and (maps[character[0]+1][character[1]] == 1 or maps[character[0]+1][character[1]] == 2) and (maps[character[0]][character[1]+1] == 1 or maps[character[0]][character[1]+1] == 2):
        if character[2] == 0 and maps[character[0]+1][character[1]] == 2:  # 회전한 방향이 북쪽일 때
            character[0] += 1

        elif character[2] == 3 and maps[character[0]][character[1] + 1] == 2:  # 회전한 방향이 서쪽일 때
            character[1] += 1

        elif character[2] == 2 and maps[character[0] - 1][character[1]] == 2:  # 회전한 방향이 남쪽일 때
            character[0] -= 1

        elif character[2] == 1 and maps[character[0]][character[1] - 1] == 2:  # 회전한 방향이 동쪽일 때
            character[1] -= 1
        else:
            break

    turn()
    if character[2] == 0 and maps[character[0]-1][character[1]] == 0: # 회전한 방향이 북쪽일 때
        character[0] -= 1
        maps[character[0]][character[1]] = 2
    elif character[2] == 3 and maps[character[0]][character[1]-1] == 0: # 회전한 방향이 서쪽일 때
        character[1] -= 1
        maps[character[0]][character[1]] = 2
    elif character[2] == 2 and maps[character[0]+1][character[1]] == 0: # 회전한 방향이 남쪽일 때
        character[0] += 1
        maps[character[0]][character[1]] = 2
    elif character[2] == 1 and maps[character[0]][character[1]+1] == 0: # 회전한 방향이 동쪽일 때
        character[1] += 1
        maps[character[0]][character[1]] = 2
    else:
        continue # 그 외의 경우에는 다시 turn()하기

for map in range(maps):
    if map.index(2):
        result += 1
print(result)







'''
입력 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''