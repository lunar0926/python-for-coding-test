# + - 순서에 따라서 문자열 슬라이싱하는 함수
def isPlusOrMinus(x, y):
    global n1, n2, n3 # 전역함수 선언
    n1 = int(s[0:x])
    n2 = int(s[x+1:y])
    n3 = int(s[y+1: ])

s = input()
minus = s.find('-')
plus = s.find('+')

# 연산
if plus < minus: # + 가 - 앞에 나오는 경우
    isPlusOrMinus(plus, minus)
    '''
    n1 = s[0:plus]
    n2 = s[plus+1:minus]
    n3 = s[minus+1: ]
    '''
    # 연산 순서에 따라서 계산
    result1 = (n1 + n2) - n3
    result2 = n1 + (n2 - n3)
    if result1 < result2:
        print(result1)
    elif result1 > result2:
        print(result2)
elif minus < plus: # - 가 + 앞에 나오는 경우
    '''
    n1 = s[0:minus]
    n2 = s[minus + 1:plus]
    n3 = s[plus + 1:]
    '''
    isPlusOrMinus(minus, plus)
    # 연산 순서에 따라서 계산
    result1 = (n1 - n2) + n3
    result2 = n1 - (n2 + n3)
    if result1 < result2:
        print(result1)
    elif result1 > result2:
        print(result2)


# 경우의 수를 나눠서 최솟값을 구함