from collections import deque

def solution(queue1, queue2):
    deque1, deque2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(deque1), sum(deque2)
    
    for cnt in range(300000):
        if sum1 == sum2:
            return cnt
        
        elif sum1 > sum2:
            n = deque1.popleft()
            deque2.append(n)
            sum1 -= n
            sum2 += n
            
        else:
            n = deque2.popleft()
            deque1.append(n)
            sum1 += n
            sum2 -= n     
            
    return -1