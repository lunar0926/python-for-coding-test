# 입력
x = int(input())
# x에 따른 최소 연산 횟수를 저장하는 리스트
d = [0] * 30001
d[1] = 0
for i in range(2, x+1):
    # -1 연산을 하는 경우
    d[i] = d[i-1] + 1
    # 5로 나누는 경우
    if i % 5 == 0:
        d[i] = min(d[i // 5] + 1, d[i])
    # 3으로 나누는 경우
    if i % 3 == 0:
        d[i] = min(d[i // 3] + 1, d[i])
    # 2로 나누는 경우
    if i % 2 == 0:
        d[i] = min(d[i // 2] + 1, d[i])
print(d[x])
