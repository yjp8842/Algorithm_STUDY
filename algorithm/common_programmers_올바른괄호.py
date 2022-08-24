def solution(s):
    
    list = []
    for i in s:
        # (가 나오면 list에 넣어주기
        if i == '(':
            list.append('(')
        # )가 나올 경우
        else:
            # 리스트가 비어있다면 False
            if list == []:
                return False
            # 리스트가 비어있지 않다면 즉, (가 들어있다면 추출 -> 즉, () 한 쌍이 빠지게 됨
            else:
                list.pop()
    
    # for문이 끝나고 list가 비어있다면 True    
    if list == []:
        return True
    else:
        return False