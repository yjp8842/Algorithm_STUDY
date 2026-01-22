def solution(n, lost, reserve):
    answer = 0
    all_student = {}
    for i in range(1, n + 1):
        all_student[i] = 1
    
    for i in range(1, n + 1):
        if i in reserve:
            all_student[i] += 1
        if i in lost:
            all_student[i] -= 1
    
    for lost_n in sorted(lost):
        if all_student[lost_n] == 0:
            front = lost_n - 1
            back = lost_n + 1

            if front >= 1 and all_student[front] == 2:
                all_student[front] -= 1
                all_student[lost_n] = 1
            elif back <= n and all_student[back] == 2:
                all_student[back] -= 1
                all_student[lost_n] = 1

    for i in range(1, n + 1):
        if all_student[i] >= 1:
            answer += 1
    
    return answer