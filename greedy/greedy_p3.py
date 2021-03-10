n, k = map(int, input().split())
result = 0
while(True):
    if n % k == 0: # 연산 2 나누어떨어지는 경우
        n /= k
        n = int(n)
    else: # 연산 1 그 외의 경우
        n -= 1
    result += 1 # 연산 횟수 1 더해주기


    # n이 1이 되는 경우
    if n == 1:
        break
print(result) # 결과 출력