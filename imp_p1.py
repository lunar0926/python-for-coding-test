n = int(input()) # 공간 크기 입력받기
A = [1, 1] # 여행자의 위치
route = input().split() # 이동 계획 # 문자열 split() 함수 사용하면 리스트로 return하는 것!
print(route)
# 이동하기
for i in route:
    if i == 'U' and A[0] != 1:
        A[0] -= 1
    elif i == 'D' and A[0] != n:
        A[0] += 1
    elif i == 'L' and A[1] != 1:
        A[1] -= 1
    elif i == 'R' and A[1] != n:
        A[1] += 1
# 조건문을 더 간략하게 사용할 수 있는데 나는 따로 함수를 만드려고 했음. 조건문의 쓰임을 잘 알고 쓸 수 있도록
print('%s %s'%(A[0], A[1]))

'''
5
R R R U D D
'''
