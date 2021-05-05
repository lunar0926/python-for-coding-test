def solution(nums):
    answer_list = [] # 새로운 종류의 폰켓몬을 선택하면 이 리스트에 넣음.
    for i in nums:
        try:
            if answer_list.index(i) >= 0: # 겹치면 answer_list에 추가하지 않기
                continue
        except: # 해당 원소가 없어서 예외가 발생하면
            answer_list.append(i)
            
    # 선택할 수 있는 폰켓몬 종류 개수의 최댓값은 N / 2
    '''
    if len(answer_list) >= len(nums) / 2:
        return len(nums) / 2
    else:
        return len(answer_list)
    '''
    return min(len(nums) / 2, len(answer_list)) # len()을 활용해서 더 간략하게 수정
