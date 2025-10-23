# x = y
# 3x = 2y -> y = 3x // 2
# 4x = 2y -> y = 2x
# 4x = 3y -> y = 4x // 3

from collections import Counter

def solution(weights):
    answer = 0
    cnt_weight = Counter(weights)
    
    for w, cnt in cnt_weight.items():
        if cnt > 1:
            answer += cnt * (cnt - 1) // 2
            
    weight_set = set(weights)
    
    for weight in weight_set:
        if weight * 2 / 3 in weight_set:
            answer += cnt_weight[weight * 2 / 3] * cnt_weight[weight]
        if weight * 2 / 4 in weight_set:
            answer+= cnt_weight[weight * 2 / 4] * cnt_weight[weight]
        if weight * 3 / 4 in weight_set:
            answer+= cnt_weight[weight * 3 / 4] * cnt_weight[weight]
            
    return answer