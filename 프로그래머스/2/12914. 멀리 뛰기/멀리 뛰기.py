def solution(n):
    answer = 0
    prev, next = 0, 1
    
    for i in range(n) :
        prev, next = next, prev + next
    
    answer = next % 1234567
    
    return answer