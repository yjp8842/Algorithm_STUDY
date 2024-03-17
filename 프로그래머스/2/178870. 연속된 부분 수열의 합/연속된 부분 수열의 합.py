def solution(sequence, k):
    answer = []
    start = 0
    end = -1
    sum = 0
    
    while True:
        if sum < k:
            end += 1
            if end >= len(sequence):
                break
            sum += sequence[end]
        else:
            sum -= sequence[start]
            if start >= len(sequence):
                break
            start += 1

        if sum == k:
            answer.append([start, end])
    
    # 첫번째 우선순위 : 길이가 짧은 수열
    # 두번째 우선순위 : 가장 앞쪽에 나온 수열
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]