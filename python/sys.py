# 데이터의 개수가 1000만 개를 넘어간다면 input() 함수를 사용했을 때 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있다.
# 이때는 sys 라이브러리의 readline() 함수를 사용하면 시간 초과를 피할 수 있다.
import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()
# 이때 rstrip()을 호출하는 이유는, 입력한 문자열 끝에 공백이 있다면 rstrip()을 통해서 제거한 뒤에 출력할 수 있기 때문
'''
strip() : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
lstrip() : 인자로 전달된 문자를 String의 왼쪽에서 제거합니다.
rstrip() : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.
인자를 전달하지 않을 수도 있으며, 인자를 전달하지 않으면 String에서 공백을 제거.
'''
# 입력받은 데이터 그대로 출력
print(input_data)
