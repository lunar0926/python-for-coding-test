# BFS breadth first search
from collections import deque
# deque '덱'이라고 읽음

# 그래프
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
visited = [False] * 9 # 방문 처리
queue = deque() # deque 라이브러리 사용

# 시작 노드
queue.append(1) # 삽입
visited[1] = True # 방문 처리
# BFS 탐색
while(True):
    if len(list(queue)) == 0: # 큐에 남은 요소가 없을 때
        break
    v = queue.popleft()
    print(v, end=' ')  # 탐색 출력
    for i in graph[v]: # 큐에서 마지막 요소를 꺼내서 인접한 방문하지 않은 노드 확인
        if visited[i] == False: # 방문하지 않은 노드라면
            queue.append(i)
            visited[i] = True



