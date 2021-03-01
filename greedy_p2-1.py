n, m = map(int, input().split())
result = 0
for i in range(n):
    list = list(map(int, input().split()))
    min_value = min(list)
    result = max(result, min_value)
'''
min(), max() 함수 사용법 
하나의 인자가 제공된다면 min(), max() 안에는 iterable한 자료형이 들어가야 함. 
문자열, 리스트, 튜플 등이 해당됨.

두 개 이상의 인자가 제공되면 그 중 가장 작은 것을 돌려줌.  

min(iterable, key = , default = ) # 여기서 key와 default는 키워드 전용 인자
key 인자는 단일 인자 순서 함수를 지정함. list.sort()에서의 쓰임과 같이
default 인자는 제공된 iterable이 비어있는 경우 돌려줄 인자를 지정함.
iterable이 비어 있고 default가 제공되지 않으면 valueError가 발생함. 
'''