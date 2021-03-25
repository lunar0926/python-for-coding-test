'''
입력 예시
5
8 3 7 9 2
3
5 7 9
'''
# 부품 확인하는 함수
def check(x):
    if x in stock_list:
        print("yes", end=' ')
    else:
        print("no", end=' ')
# 입력 받기
n = int(input()) # 가게에 있는 부품 개수
stock_list = list(map(int, input().split()))
m = int(input()) # 손님이 구매하려는 부품 개수
buy_list = list(map(int, input().split()))
for i in buy_list:
    check(i)