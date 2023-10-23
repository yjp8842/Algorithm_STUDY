def solution(numbers):
    # 시간 초과
    # answer = []
    # for i in range(len(numbers)):
    #     flag = 0
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[j] > numbers[i]:
    #             answer.append(numbers[j])
    #             flag = 1
    #             break
    #     if flag == 0:
    #         answer.append(-1)
    
    answer = [-1] * len(numbers)  # 결과를 저장할 리스트, 초기값을 -1로 설정
    stack = []  # 인덱스를 저장할 스택

    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            # 스택이 비어있지 않고, 현재 원소가 스택의 맨 위 원소보다 크다면
            # 다음 큰 수를 찾았으므로 업데이트
            last = stack.pop()
            answer[last] = numbers[i]
        # 현재 원소의 인덱스를 스택에 추가
        stack.append(i)
            
    return answer