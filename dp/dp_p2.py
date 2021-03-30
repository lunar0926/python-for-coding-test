# 입력받기
n = int(input()) # 식량창고 개수
array = list(map(int, input().split())) # 식량창고 리스트로 받기
# 다시 방문할 수 없는 창고를 표시하는 dp 테이블
d = [0] * 100
# 선택한 식량의 합
sum = 0
# 창고 크기 확인용 리스트
compare_array = sorted(array) # 리스트를 반환해주는 것은 sorted() 함수. 주의하기

# 최대한 많은 식량 얻기(가장 큰 값 찾고, 인접한 창고는 방문불가 표시, 그 다음으로 큰 값 찾고 인접한 창고 방문불가 표시, 반복하기)
for i in range(n-1, -1, -1):
    biggest = compare_array[i] # 뒤에서부터 가장 큰 값 구하기
    b = array.index(biggest) # 가장 큰 값의 위치
    # 방문할 수 없는 창고라면 continue
    if d[b] != 0:
        continue
    else:
        d[b] = 1
        # 인접한 창고는 방문불가 표시
        if b-1 >= 0:
            d[b-1] = 1
        if b+1 < n:
            d[b+1] = 1
        # 선택한 식량값 합계에 넣기
        sum += array[b]
# 결과 출력
print(sum)