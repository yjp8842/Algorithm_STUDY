import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    while True:
        if scoville[0] >= K:
            break
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        n_scoville = first + (second * 2)
        
        heapq.heappush(scoville, n_scoville)
        
        cnt += 1
        
    return cnt