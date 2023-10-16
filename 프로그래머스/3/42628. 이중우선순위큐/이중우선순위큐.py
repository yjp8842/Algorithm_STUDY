import heapq

def solution(operations):
    heap = []
    for i in range(len(operations)):
        oper, num = map(str, operations[i].split())
        
        if oper == 'I':
            heapq.heappush(heap, int(num))
            
        elif oper == 'D' and len(heap) > 0:
            if int(num) == -1:
                heapq.heappop(heap)
            else:
                max_heap = []
                for n in heap:
                    heapq.heappush(max_heap, -n)
                heapq.heappop(max_heap)
                
                heap = []
                for n in max_heap:
                    heapq.heappush(heap, -n)
    
    ans = []
    if len(heap) == 0:
        return [0, 0]
    else:
        max_heap = []
        for n in heap:
            heapq.heappush(max_heap, -n)
        ans.append(-heapq.heappop(max_heap))
        ans.append(heapq.heappop(heap))
        
        return ans
