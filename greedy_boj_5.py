# 입력받기
n = int(input()) # 도시의 개수 
l = list(map(int, input().split())) # 도시의 길이 리스트
price = list(map(int, input().split())) # 리터당 가격 리스트
sum = 0 # 기름 총 비용
meter = 0 # 가야하는 총 거리
# 가야하는 총 거리 구하기
for km in l:
    meter += km

# 최소의 비용 구하기 
for i in range(n-1): # 각 도시마다 기름 넣기
    if meter == 0: # 남은 거리가 0이면 멈추기
        break
    sum += (price[i] * l[i])
    meter -= l[i]
    for j in range(i, n-2):
        if meter == 0: # 남은 거리가 0이면 멈추기
            break
        elif price[j] * l[j+1] < price[j+1] * l[j+1]: # 이전 도시에서 주유하는 것이 다음 도시보다 더 저렴하다면?
            sum += (price[j] * l[j+1]) # 이전 도시에서 다음 도시까지의 거리만큼 더 주유하기
            meter -= l[j+1]
print(sum) # 기름 총 비용 출력하기




