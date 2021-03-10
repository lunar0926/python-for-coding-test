n = int(input()) # 사람의 수
t = list(map(int, input().split())) # 인출 시간 리스트
t.sort() # 오름차순 정렬
sum = 0 # 각 사람이 돈을 인출하는데 필요한 시간의 합
for i in range(n):
    for j in range(0, i+1):
        sum += t[j]
print(sum)

