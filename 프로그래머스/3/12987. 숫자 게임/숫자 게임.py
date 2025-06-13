def solution(A, B):
    answer = 0
    
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    
    bi = 0
    for i in range(len(A)):
        if B[bi] > A[i]:
            answer += 1
            bi += 1
    
    return answer