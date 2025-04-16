def count(num):
    cnt = 0
    while True:
        if num // 2 == 1:
            if num % 2 != 0:
                cnt += 1
            cnt += 1
            break
        
        if num % 2 != 0:
            cnt += 1
        
        num = num // 2
    
    return cnt

def solution(n):
    n_cnt = count(n)
    
    while True:
        n += 1
        if count(n) == n_cnt:
            return n
        
        count(n)