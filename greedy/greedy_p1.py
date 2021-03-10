# 다양한 수의 배열, M번 더하여 가장 큰 수를 만드는 법칙
# 연속해서 K번까지만 더해질 수 있음. 다른 인덱스는 다른 수로 간주
# 배열의 크기 N 더해지는 횟수 M 연속 횟수 K
# 총합을 출력하기
N, M, K = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
# 리스트에서 맨 마지막부터 차례차례 골라서 K번 더해주기
sum = 0
index = -1
count = 0
for i in range(M):
    sum += array[index]
    count += 1
    if count == 3:
        index -= 1
    elif count == 4:
        index = -1
        count = 0
print(sum)
# 예시를 통해서 최대한 문제 이해를 한 다음에 답안을 작성해야함.
