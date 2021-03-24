# 이진 탐색은 리스트 내에서 데이터를 매우 빠르게 탐색하는 것.
# 이진 탐색을 알아보기 전에 가장 기본 탐색 방법인 순차 탐색에 대해 먼저 이해할 필요가 있음.
# 순차 탐색은 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1 # i는 0부터 시작하고 찾았다면 +1

# 입력
n = int(input('리스트의 원소 개수를 입력하세요: '))
array = input("리스트의 원소들을 입력한 개수만큼 공백을 두고 입력하세요: ").split()
target = input("목표로 하는 단어를 입력하세요: ")
print(sequential_search(n, target, array))

# 순차 탐색은 데이터 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인해야 한다는 점이 특징.
# 데이터의 개수가 N개일 때, 최대 N번의 비교 연산이 필요하므로 순차 탐색의 최악의 경우 시간 복잡도는 O(N)이다.