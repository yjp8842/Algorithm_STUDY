def solution(A, B):
    nums = 0
    new_a = sorted(A)
    new_b = sorted(B, reverse = True)
    
    for i in range(len(A)):
        nums += new_a[i] * new_b[i]

    return nums