n = int(input()) # 회의의 수 입력
time_list = [] # 회의 요청시간 리스트
con_list = [] # 가능한 회의 리스트
for i in range(n):
    time = list(map(int, input().split())) # 회의 시간 입력
    time_list.append(time)

for i in range(n):
    start_time = time_list[i][0]
    end_time = time_list[i][1]
    length = end_time - start_time # 각 회의 시간의 길이
    time_list[i].append(length)
time_list.sort(key= lambda x: [x[2], x[0]]) # 회의 시간의 길이가 짧은 순부터 오름차순 정렬 / 시작 시간 순으로 오름차순 정렬
print(time_list)



