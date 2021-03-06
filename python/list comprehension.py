# 리스트 컴프리헨션은 리스트를 초기화하는 방법 중 하나. 코드 길이를 줄일 수 있음

## 0~19까지의 수 중에서 홀수만 포함하는 리스트
'''
# 일반적인 소스코드

list = [0, 1]
for i in range(2, 20):
    if i % 2 == 1:
        list.append(i)
print(list)

# 리스트 컴프리헨션 이용
list = [i for i in range(1,20) if i % 2 == 1]
print(list)
# for문과 if문에서 : 가 없이 나열되는 것이 특징

## 1부터 9까지의 수의 제곱 값을 포함하는 리스트
# 리스트 컴프리헨션 이용
list = [i * i for i in range(1, 10)]
print(list)
'''

## N * M 크기의 2차원 리스트 초기화하기
# 리스트 컴프리헨션 이용
n = 3
m = 4
list = [[0] * m for _ in range(n)]
print(list)
# 이때 _ 언더바의 기능을 잘 이해해야함. 반복을 수행하되, 반복을 위한 변수의 값을 무시하고자 할 때 사용.
# 쉽게 말해 반복문 횟수를 돌리기만 하고 싶고 변수를 넣을게 없으면 언더바를 사용.
# 2차원 리스트를 초기화할 때는 리스트 컴프리헨션을 사용하도록 하자. 내가 의도하지 않은 결과가 나올 수 있기 때문.