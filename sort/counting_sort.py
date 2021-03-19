# 계수 정렬
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능 
# 가장 큰 데이터와 가장 작은 데이터의 차이가 너무 크다면 사용할 수 없음. 
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
min = min(array)
max = max(array)
n = max - min + 1
counting_array = [0 for _ in range(n)]
# array의 원소를 하나씩 확인하면서 counting_ array에서 해당하는 
# 원소의 인덱스값에 +1 해주기
for i in array:
    counting_array[i] += 1

# 출력하기  
for i in range(len(counting_array)):
    for j in range(counting_array[i]):
        print(i, end =' ')

# 모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 데이터 중 최대값의 크기를 K라고 할 때, 
# 계수 정렬의 시간 복잡도는 O(N + K)
# 시간 복잡도는 조건에 맞는다면 알고리즘 중 가장 빠른 축에 속하지만, 
# 때에 따라서 공간 복잡도는 비효울적으로 나타날 수 있음. 
# ex) 데이터가 0과 999999 단 2개만 있더라도 리스트 크기는 100만 개가 되도록 선언해야 함. 
# 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을수록 유리함. 
