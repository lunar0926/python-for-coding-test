# 2579번 같은 문제를 점화식을 세워서 풀어보기 
# 입력받기
n = int(input()) # 시작점을 제외한 계단 개수
steps = [0]
for _ in range(n):
    steps.append(int(input()))
# 도착한 계단까지의 점수 총합의 최댓값을 저장하는 dp 테이블
d = [0] * 301
d[1] = steps[1]
d[2] = steps[1] + steps[2]
# n이 3 이상일 때 
if n >= 3:
    for i in range(3, n+1):
        d[i] = max(steps[i] + d[n-2], steps[i] + steps[n-1] + d[n-3])
# n에서의 점수 합 최댓값 출력
print(d[n])
