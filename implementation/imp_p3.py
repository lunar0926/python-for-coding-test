n = input() # 나이트가 있는 열과 행 입력받기
column = n[0] # 나이트가 있는 열
row = int(n[1]) # 나이트가 있는 행
# 행과 열 만들기
rows = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8}
columns = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5,'f':6,'g':7,'h':8}
count = 0 # 가능한 경우의 수

# 이동 가능한 경우의 수 구하기
if row + 1 >= 1 and row + 1 <= 8 and columns[column] + 2 >= 1 and columns[column] + 2 <= 8:
    count += 1
if row - 1 >= 1 and row - 1 <= 8 and columns[column] + 2 >= 1 and columns[column] + 2 <= 8:
    count += 1
if row + 1 >= 1 and row + 1 <= 8 and columns[column] - 2 >= 1 and columns[column] - 2 <= 8:
    count += 1
if row - 1 >= 1 and row - 1 <= 8 and columns[column] + 2 >= 1 and columns[column] + 2 <= 8:
    count += 1
if row - 2 >= 1 and row - 2 <= 8 and columns[column] - 1 >= 1 and columns[column] - 1 <= 8:
    count += 1
if row - 2 >= 1 and row - 2 <= 8 and columns[column] + 1 >= 1 and columns[column] + 1 <= 8:
    count += 1
if row + 2 >= 1 and row + 2 <= 8 and columns[column] - 1 >= 1 and columns[column] - 1 <= 8:
    count += 1
if row + 2 >= 1 and row + 2 <= 8 and columns[column] + 1 >= 1 and columns[column] + 1 <= 8:
    count += 1

print(count)
'''
# 문제 해설에서 제시한 코드 
# 나는 가능한 경우의 수를 조건문으로 하나하나 만들었지만 여기서는 steps = [] 리스트를 만들어서 반복문으로 조건 확인 
steps = [[1, 2], [-1, 2], [1, -2], [-1, 2], [-2,-1], [-2, 1], [2, -1], [2, 1]]
for step in steps:
    next_row = row + step[0]
    next_column = columns[column] + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1 
print(count)
'''