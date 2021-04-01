'''
# 입력 받기
n, m = map(int, input().split())
array = [] # 화폐 단위
for _ in range(n):
    coin = int(input())
    array.append(coin)
result = 0 # 사용한 화폐 개수

for i in range(n-1, 0, -1):
    if m == 0:
        break
    if m < array[i]: # 불가능한 경우 -1 출력
        print(-1)
        break
    result += m // array[i]
    m = m % array[-1] # 나머지, 남은 값

if m == 0:
    print(result)
'''
'''
입력 예시 
2 15
2 
3
이 문제는 그리디 알고리즘을 해결할 수 없음. 가장 큰 화폐부터 처리하지 않더라도 답이 나오는 경우가 있기 때문 
'''









