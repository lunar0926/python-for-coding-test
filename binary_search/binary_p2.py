'''
입력 예시
4 6
19 15 10 17
'''
# 주어진 입력 리스트를 오름차순으로 정렬했을 때 사이 값들 중 하나가 정답이라는 생각을 하니까 이진탐색을 써야겠다는 발상!
# 그리고 입력받는 데이터의 크기가 커서(20억) 이진 탐색을 써야겠다는 생각도 함.
# 입력받기
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort() # 이진 탐색을 위해 정렬하기
start = array[0]
end = array[n-1]
def binary_search(array, start, end, m): # start, end는 인덱스가 아닌 떡의 길이값
    if start > end:
        return None # 손님이 요청한 길이를 만들 수 없음.
    mid = (start + end) // 2
    sum = 0  # 떡을 자른 길이의 합
    for i in array:
        if i - mid >= 0:
            sum += (i - mid)
    if sum == m:
        return mid
    if sum > m:
        return binary_search(array, mid+1, end, m)
    elif sum < m:
        return binary_search(array, start, mid-1, m)
# 결과 출력
result = binary_search(array, start, end, m)
print(result)
