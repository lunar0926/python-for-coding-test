# queue 예제
from collections import deque
queue = deque()
# 삽입(5) - 삽입(2) - 삽입(3) - 삭제() - 삽입(6) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(6)
queue.popleft()

print(queue)