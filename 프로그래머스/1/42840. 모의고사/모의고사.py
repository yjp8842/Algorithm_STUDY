def solution(answers):
    answer = []
    a_len = len(answers)
    firsts = [1, 2, 3, 4, 5] * 2000
    seconds = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    thirds = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    first = firsts[0:a_len]
    second = seconds[0:a_len]
    third = thirds[0:a_len]
    
    cnt = [[0, 0], [1, 0], [2, 0]]
    for i in range(len(answers)):
        if first[i] == answers[i]:
            cnt[0][1] += 1
        if second[i] == answers[i]:
            cnt[1][1] += 1
        if third[i] == answers[i]:
            cnt[2][1] += 1
    
    sort_cnt = sorted(cnt, key=lambda x : x[1], reverse=True)
    max_cnt = sort_cnt[0][1]
    
    for idx, cnt in sort_cnt:
        if cnt == max_cnt:
            answer.append(idx + 1)
    
    return answer