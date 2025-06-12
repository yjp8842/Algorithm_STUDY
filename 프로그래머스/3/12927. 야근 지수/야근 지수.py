import heapq

def solution(n, works):
    answer = 0
    queue = []
    
    if sum(works) <= n:
        return 0
    
    for work in works:
        heapq.heappush(queue, -work)
    
    for i in range(n):
        work = heapq.heappop(queue)
        
        if work == 0:
            return 0
        
        heapq.heappush(queue, work + 1)
        
    for work in queue:
        answer += work ** 2

    return answer