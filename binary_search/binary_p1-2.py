# 계수 정렬을 활용해서 해결
# 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용. 모든 범위를 담을 수 있는 리스트 선언해야 함.
'''
입력 예시
5
8 3 7 9 2
3
5 7 9
'''
# 입력 받기
n = int(input()) # 가게에 있는 부품 개수
stock_list = list(map(int, input().split()))
m = int(input()) # 손님이 구매하려는 부품 개수
buy_list = list(map(int, input().split()))
# 계수 정렬을 위한 리스트 만들기
array = [0] * 1000001
for i in stock_list:
    array[i] = 1 # 부품에 해당하는 리스트를 1로 변경
# 구매하려는 부품이 있는지 확인
for j in buy_list:
    if array[j] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')