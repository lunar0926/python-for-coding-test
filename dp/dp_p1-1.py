# 재귀적으로 구현(탑다운 방식)
# 입력 받기
x = int(input())
# 메모이제이션을 위한 리스트 초기화
d = [0] * 30001

# 재귀함수로 구현
def dy(x):
    # 종료 조건(d[1]에서는 0을 반환)
    if x == 1:
        return 0
    # 이미 연산 횟수를 구한 정수는 그대로 반환
    if d[x] != 0:
        return d[x]
    # 연산 횟수를 구하지 않았다면 경우에 따라서 나누고, 연산 횟수의 최솟값 찾기
    d[x] = d[dy(x-1)] + 1
    if x % 5 == 0:
        d[x] = min(d[dy(x//5)] + 1, d[x])
    if x % 3 == 0:
        d[x] = min(d[dy(x//3)] + 1, d[x])
    if x % 2 == 0:
        d[x] == min(d[dy(x//2)] + 1, d[x])
    return d[x]
# 출력
print(dy(x))