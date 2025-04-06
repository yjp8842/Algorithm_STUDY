def solution(n):
    sums = 0
    first = 0
    next = 1
    for _ in range(n - 1):
        sums = first + next
        first = next
        next = sums
    
    answer = sums % 1234567
    return answer