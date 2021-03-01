n, m, k = map(int, input().split())
list = list(map(int, input().split()))
list.sort() # 리스트 정렬
# 가장 큰 수와 두 번째로 큰 수 변수로 저장.(n의 값에 따라 가변적으로)
first = list[n-1]
second = list[n-2]
# 가장 큰 수가 몇 번 더해지는지, 두 번째로 큰 수는 몇 번 더해지는지를 구하기
count = 0
count += int(k * m / (k + 1)) # 나누기 연산을 하면 소수점자리까지 나오므로 int()를 하는 것
count += m % (k + 1)
sum = 0 # 총합
sum += first * count # 총합에 가장 큰 수 더하기
sum += second * (m-count) # 총합에 두 번째로 큰 수 더하기

print(sum) # 최종 답안 출력
