# 입력받기
n = int(input())
# dp 테이블
d = [0] * 1001 # 입력값 n이 1000까지이므로

# 바텀업 방식으로 다이나믹 프로그래밍 구현
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2] * 2
result = d[n] % 796796
print(result)