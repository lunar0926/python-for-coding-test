# 9184번 신나는 함수 실행
# 재귀함수를 그대로 구현하면 시간 초과 -> 바텀업 방식으로 구현해라는 것.

# 입력
array = []
while(True):
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    array.append([a, b, c])

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b and b < c:
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

# dp테이블을 이용하려 했는데 변수가 3개인 경우는 어떻게 저장하고 인덱스를 확인할 것인가?
# 변수가 3개이기 때문에 바텀업 방식으로 저장하다보면 삼중for문을 써야하는 것 아닌가??
# 바텀업으로 해결하는 것이 아니라 재귀함수에서 다른 방법을 추가하는 것인지??