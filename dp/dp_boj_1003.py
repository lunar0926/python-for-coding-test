# 1003번 피보나치 함수
# 그대로 재귀를 활용해서 풀 수는 있지만 시간초과 or 메모리 초과 발생. 바텀업 방식의 다이나믹 프로그래밍 활용해서 해결하기
# 입력
t = int(input()) # 테스트 케이스의 개수
array = [] # 테스트 케이스의 리스트
for _ in range(t):
    array.append(int(input()))

# 테스트 케이스 결과를 저장하는 리스트(n은 40까지 )
d = [[0, 0] for _ in range(41)]

# 바텀업, 반복문으로 피보나치 구현하여 테스트 케이스의 0과 1 개수 저장
for i in range(0, 41):
    if i == 0:
        d[i][0] += 1
    elif i == 1:
        d[i][1] += 1
    else:
        d[i][0] = d[i-1][0] + d[i-2][0]
        d[i][1] = d[i-1][1] + d[i-2][1]

# 출력하기
for i in array:
    print(d[i][0], end=' ')
    print(d[i][1])

        