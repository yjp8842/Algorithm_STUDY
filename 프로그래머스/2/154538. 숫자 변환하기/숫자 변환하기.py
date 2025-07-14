from collections import deque

def solution(x, y, n):
    visited = set()
    queue = deque()
    # (현재값, 연산횟수)
    queue.append((x, 0))
    
    while queue:
        current, count = queue.popleft()
        
        if current == y:
            return count
        
        for next_val in (current + n, current * 2, current * 3):
            if next_val <= y and next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, count + 1))
    
    return -1