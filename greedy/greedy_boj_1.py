n, k = map(int, input().split())
result = 0 # 필요한 동전 개수
A = [] # 동전의 종류 리스트
# 둘째 줄부터 동전의 종류 입력받기
for i in range(n):
    a = int(input())
    A.append(a)
A.reverse() # 내림차순 정렬
# 반복문으로 필요한 동전의 개수 구하기
for i in range(n):
    if k >= A[i]:
        result += (k // A[i])
        k = (k % A[i])
    # k == 0 일때, 더 이상 동전이 필요하지 않을 때
    elif k == 0:
        break
print(result) # 필요한 동전의 개수 출력



