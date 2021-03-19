n = int(input())
array = []
for _ in range(n):
    '''
    a = int(input())
    array.append(a)
    '''
    # 더 간소하게 코드를 축약하기
    array.append(int(input()))
# 공백으로 구분해서 내림차순으로 출력하기. 
array.sort(reverse = True)
for i in array:
    print(i, end = ' ')

'''
입력 예시
3
15
27
12
'''