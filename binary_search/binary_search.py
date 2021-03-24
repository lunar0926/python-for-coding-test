# 순차 정렬은 데이터가 정렬되어 있지 않은 상태에서도 사용할 수 있다면, 이진 탐색은 이미 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
# 이진 탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는게 이진 탐색 과정. 원하는 데이터를 찾는 것!!!
# 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어들기 때문에 시간복잡도는 O(logN)
def binary_search(start, end, target, array):
    mid = (start + end) // 2
    # 찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간값이 목표값보다 크다면 오른쪽 절반은 버리고 왼쪽 확인
    elif array[mid] > target:
        return binary_search(start, mid - 1, target, array)
    # 중간값이 목표값보다 작다면 왼쪽 절반은 버리고 오른쪽 확인
    elif array[mid] < target:
        return binary_search(mid + 1, end, target, array)
n, target = map(int, input().split()) # n은 원소 개수이자, end 값을 알 수 있음.
array = list(map(int, input().split()))
# 이진 탐색 수행 결과 출력
result = binary_search(0, n-1, target, array)
print(result + 1)

'''
10 7
1 3 5 7 9 11 13 15 17 19
'''
'''
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1) # 몇 번째 인덱스인지를 나타내기 위해서 +1 하는 것
'''