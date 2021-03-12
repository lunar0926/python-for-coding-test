# 내장 함수
# sum(): iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환함.
'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(list))
'''
# min(), max(): 파라미터가 2개 이상 들어왔을 때. 리스트를 입력받아도 원소의 최솟값, 최댓값을 찾아냄
'''
result = min(2, 5, 6)
print(result)
result2 = min([10, 2, 5])
print(result2)
'''
# eval() 함수. 수학 수식이 "문자열 형태"로 들어오면 해당 수식을 계산한 결과를 반환함.
'''
result = eval("10 - 5 * 2")
print(result)
'''
# sorted() 함수. sort() 함수와 구분하기. sort()함수는 리스트.sort() 와 같이 사용하지만, sorted(iterable 객체)로 사용
# key 속성으로 정렬 기준 명시, reverse 속성으로 내림차순 정렬 여부 설정할 수 있음.
result1 = sorted([4, 2, 3, 6, 7]) # 기본. 오름차순 정렬
result2 = sorted([4, 2, 3, 6, 7], reverse=True) # 내림차순 정렬
print(result1)
print(result2)
# key 속성 사용 예시(x:x[1] 원소에서 두 번째 원소를 기준으로 내림차순 정렬을 한다.)
# key 매개 변수의 값은 단일 인자를 취하고 정렬 목적으로 사용할 키를 반환하는 함수여야 함.
# key= str.lower와 같이 사용할 수도 있음.
# 원소 중 하나를 선택해서 기준으로 삼을 때 lambda 함수를 사용 lambda 인자:조건 의 형태
# lambda 함수는 이름이 없는 함수, 일회용으로 쓰는 용도
result3 = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key= lambda x:x[1], reverse=True)
print(result3)
