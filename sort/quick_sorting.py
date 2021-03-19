# 퀵정렬 
# 피벗 pivot을 기준으로 삼고 리스트 왼쪽부터 피벗보다 큰 값을 찾는 i, 오른쪽부터 작은 값을 찾는 j를 두고 각각
# 조건에 맞는 값을 찾았을 때는 해당 i,j 인덱스의 값을 스왑. 교차되는 경우에는 작은 값 j와 피벗의 위치를 바꾸고 
# 피벗을 기준으로 파티션을 나누게 됨. 각각의 파티션에서도 똑같이 수행. 이 과정은 재귀함수와 동작원리가 같음. 
# 퀵정렬의 시간 복잡도는 O(NlogN)
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우
        return # 함수 종료
    # start, end, left, right는 인덱스를 나타내는 변수. 
    pivot = start 
    left = start + 1
    right = end 
    while left <= right: # 교차되기 전까지 반복 
        # 피벗보다 큰 데이터를 찾기 직전까지 반복
        while left <= end and array[left] <= array[pivot]: 
            left += 1
        # 피벗보다 작은 데이터를 찾기 직전까지 반복 
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체. 
        # 이 조건문이 실행되면 그 다음에 외부 while문 종료되는 것
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행. 이전에 right 위치에 pivot값이 들어가는 것.  
    quick_sort(array, start, right-1)
    quick_sort(array, right, end)