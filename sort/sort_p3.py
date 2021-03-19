# 입력 받기
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# 배열 A의 가장 작은 값과 배열 B의 가장 큰 값을 바꿔주다보면 배열 A의 모든 원소의 합이 최대가 되게 만들 수 있음.
# A 리스트 오름차순 정렬
A.sort()
# B 리스트 내림차순 정렬
B.sort(reverse=True)
# k번 반복
for i in range(k):
    if A[i] < B[i]: # A에서의 값이 B에서의 값보다 작을 때만 바꿔주는 의미가 있음. 
        A[i], B[i] = B[i], A[i] # 해당 인덱스의 값을 바꿔주기 
    else: # 불필요한 연산을 줄이기 위해서 A값이 B값보다 커지는 시점에는 반복문 탈출 
        break
# A 배열의 모든 원소의 합이 최대일 때 출력
print(sum(A))

'''
입력 예시
5 3
1 2 5 4 3
5 5 6 6 5
'''
        