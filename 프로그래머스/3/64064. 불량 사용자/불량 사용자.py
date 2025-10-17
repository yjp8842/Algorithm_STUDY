from itertools import product

def solution(user_id, banned_id):
    answer = 0
    dict = {}
    
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[j]):
                flag = 0
                for k in range(len(user_id[j])):
                    if banned_id[i][k] != user_id[j][k]:
                        if banned_id[i][k] == '*':
                            continue
                        else:
                            flag = 1
                            break
            else:
                flag = 1

            if flag == 0:
                if i in dict:
                    if user_id[j] not in dict[i]:
                        dict[i] += [user_id[j]]
                else:
                    dict[i] = [user_id[j]]
    
    lst = []
    for i in range(len(dict)):
        lst.append(dict[i])
        
    results = list(product(*lst))
    
    tmps = []
    for result in results:
        tmp = set(result)
        if len(tmp) == len(banned_id) and tmp not in tmps:
            tmps.append(tmp)
            answer += 1
    
    return answer