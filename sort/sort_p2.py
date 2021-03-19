# 입력
# n = int(input())
# array = []
# for i in range(n):
#     array.append(input().split()) # 공백 기준으로 문자열로 리스트에 추가 
#     # array[i][1] = int(array[i][1]) # 성적은 정수로 변환
#     int(array[i][1])
# array = sorted(array, key=lambda x:x[1]) # 성적을 기준으로 오름차순 정렬 
# for i in range(n):
#     print(array[i][0], end=' ') # 이름을 성적이 낮은 순서대로 출력

'''
입력 예시
2
홍길동 95
이순신 77
'''
# 튜플을 사용해보기 

# 입력
n = int(input())
array = []
for i in range(n):
    input_data = input().split() 
    array.append((input_data[0], int(input_data[1]))) # 튜플로 (이름, 점수) 저장
array.sort(key=lambda student:student[1])
for i in range(n):
    print(array[i][0], end=' ')