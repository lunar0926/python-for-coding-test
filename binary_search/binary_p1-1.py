'''
입력 예시
5
8 3 7 9 2
3
5 7 9
'''
# 내가 적은 코드로 문제를 맞추긴 했지만 교재에 있는 예시대로 이진 탐색, 계수 정렬, 집합 자료형을 이용해서 해결해보기.
# 이진 탐색 활용(재귀함수)
# 함수 정의
def check(array, start, end, target): # target에는 구매하려는 제품 종류를 변수로 넣어야 함.
    # target을 못 찾았을 때
    if start > end:
        print("no", end=' ')
    # 중간값
    mid = (start + end) // 2
    if array[mid] == target:
        print("yes", end=' ')
    if array[mid] > target:
        return check(array, start, mid-1, target)
    elif array[mid] < target:
        return check(array, mid+1, end, target)

# 입력 받기
n = int(input()) # 가게에 있는 부품 개수
stock_list = list(map(int, input().split()))
stock_list.sort() # 이진 탐색을 하기 위해서 정렬해주어야 함.
m = int(input()) # 손님이 구매하려는 부품 개수
buy_list = list(map(int, input().split()))
# 구매하려는 부품 재고 확인하기
for i in buy_list:
    check(stock_list, 0, n-1, i)