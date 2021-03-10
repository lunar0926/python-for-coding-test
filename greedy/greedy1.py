# 그리디 알고리즘 예제
# 각 동전의 개수를 구하고 그 합을 출력하기
'''
# 내 답안
n = int(input()) # 거슬러 줘야 할 돈, 10의 배수
five, hundred, fifty, ten = 0, 0, 0, 0 # 동전의 개수

five = n // 500
n = n % 500
hundred = n // 100
n = n % 100
fifty = n // 50
n = n % 50
ten = n // 10
n = n % 10
print('%d개'%(five+hundred+fifty+ten))
'''
'''
배열을 통해서 화폐 단위를 나타낼 수 있음 
같은 식이 반복되는데 나는 이것을 반복문으로 해결하지 않았음.

배열 사용하기!
문제의 답이 무엇을 구하는 것인지 생각 -> 동전의 개수. 그러면 동전의 개수를 변수로 지정 
변수 이름도 가능하면 직관적으로 명명할 수 있어야 함. 
'''
# 교재의 예시 답안
n = int(input())
array = [500, 100, 50, 10]
count = 0
for coin in array:
    count += n // coin
    n %= coin
print(count)