def solution(N, stages):
    answer = []
    dic = {}
    users = len(stages)
    
    for stage in range(1, N + 1):
        cnt = stages.count(stage)
        
        if users == 0:
            failure_rate = 0
        else:
            failure_rate = cnt / users
        
        dic[stage] = failure_rate
        users -= cnt
    
    sorted_dic = sorted(dic.items(), key=lambda item: (-item[1], item[0]))
    
    for n in range(N):
        answer.append(sorted_dic[n][0])
    
    return answer