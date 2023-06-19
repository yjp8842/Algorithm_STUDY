def solution(s):
    answer = []
    dict = {}
    
    for idx, word in enumerate(s):
        if word not in dict:
            answer.append(-1)
            dict[word] = idx
    
        else:
            answer.append(idx - dict[word])
            dict[word] = idx
            
    return answer