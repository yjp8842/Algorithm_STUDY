def solution(topping):
    answer = 0
    first_cake = {}
    second_cake = {}
    
    for t in topping:
        if t in first_cake:
            first_cake[t] += 1
        else:
            first_cake[t] = 1
            
    for t in topping:
        if len(first_cake) == len(second_cake):
            answer += 1
            
        first_cake[t] -= 1
        
        if t not in second_cake:
            second_cake[t] = 1
        
        if first_cake[t] == 0:
            del first_cake[t]
    
    return answer