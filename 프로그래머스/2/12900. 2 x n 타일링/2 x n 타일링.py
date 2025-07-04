# 1 2 3 4 5 6
# 1 2 3 5 8 13 ..

def solution(n):
    answer = 0
    a, b = 1, 2
    
    for i in range(3, n + 1):
        a, b = b, (a + b)
    
    answer = b % 1000000007
    
    return answer