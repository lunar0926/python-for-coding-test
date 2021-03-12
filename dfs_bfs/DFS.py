# depth - first - search 깊이 우선 탐색
# 같은 그래프를 인접행렬방식과 인접리스트방식으로 나누어서 구현할 수 있음.
'''
# 인접 행렬 방식
INF = 999999999
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)
# 인접 리스트 방식
graph1 = [[] for _ in range(3)]
graph1[0].append((1, 7))
graph1[0].append((2, 5))
graph1[1].append((0, 7))
graph1[2].append((0, 5))
print(graph1)
'''
# DFS는 재귀함수로 구현하는게 적합하지만 정확한 이해를 위해 스택 자료구조로도 구현해보기
'''
# 스택 자료구조
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
stack = []
count = 0 # 방문하지 않은 인접 노드가 있을 때 방문 처리한 횟수
# 시작 노드 1
stack.append(1)
visited[1] = True
print(1, end=' ')
while(True):
    adjacent = False # 방문하지 않은 인접 노드가 있는지 체크. 여기서 초기화
    if len(stack) == 0: # 더 이상 방문하지 않은 노드가 없을 때 / 스택에 남아있는 노드가 없을 때
        break
    else:
        for i in graph[stack[-1]]:
            if visited[i] == False:
                stack.append(i)
                visited[i] = True
                print(i, end=' ')
                adjacent = True
                break
        if adjacent == False: # 방문하지 않은 인접 노드가 없을 때는 스택에서 꺼낸다.
            stack.pop() # pop함수의 쓰임을 잘 알기
'''
# 재귀함수 활용
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
def dfs(n):
    adjacent = False
    # 탐색 노드 방문 처리와 출력
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if visited[i] == False:
            adjacent = True
            dfs(i)
        # 여기서 만약 방문하지 않은 인접 노드가 없는 경우에는 연속해서 호출되는 함수 호출 스택에서 해당 함수는 종료가 되고 이전 함수를 호출하게 됨.
        # 이는 스택 자료구조에서 원소를 pop, 꺼내는 것과 같음.
# 정의된 dfs 함수 호출 
dfs(1)

