# 입력 받기
x = int(input())
count = 0 # 연산 횟수
# 1이 될 때까지 연산 반복
while x > 1:
    # 먼저 1을 뺀 후에 나누어 떨어지는 수인지 확인
    if (x-1) % 5 == 0:
        x -= 1
        count += 1
    elif (x-1) % 3 == 0:
        x -= 1
        count += 1
    elif (x-1) % 2 == 0:
        x -= 1
        count += 1

    if x % 5 == 0:
        x //= 5
        count += 1
    elif x % 3 == 0:
        x //= 3
        count += 1
    elif x % 2 == 0:
        x //= 2
        count += 1
print(count)