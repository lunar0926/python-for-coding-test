n = int(input()) # 시
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 문자열로 변환
            i = str(i)
            j = str(j)
            k = str(k)
            if i.find('3') != -1 or j.find('3') != -1 or k.find('3') != -1:
                count += 1
            # if '3' in str(i) + str(j) + str(k):
            #    count += 1
print(count)

# find() 함수는 문자열이나 리스트에서 해당 요소가 있는지를 확인하고 있으면 위치를 반환, 없으면 -1을 리턴