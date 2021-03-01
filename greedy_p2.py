# n, m 입력받기
n , m = map(int, input().split())
card_list = [] # 카드를 놓는 리스트
# 각 줄의 값을 입력받기
for i in range(n):
    row = list(map(int, input().split()))
    row.sort() # 오름차순으로 정렬
    card_list.append(row)
# 각 행의 가장 작은 값끼리 비교하기
compare_list = [] # 각 행에서 가장 작은 값들끼리 비교하기 위한 리스트 만들기
for i in range(n):
    compare_list.append(card_list[i][0]) # 각 줄에서 가장 작은 값들을 비교 리스트에 넣기
compare_list.sort()
print(compare_list[-1]) # 비교 리스트에서 가장 큰 값이 출력할 값

