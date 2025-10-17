def max_sum(arr):
    if not arr:
        return 0

    arr_max = arr[0] # 전체 최대합
    current_max = arr[0] # 현재 최대합

    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        arr_max = max(arr_max, current_max)

    return arr_max

def solution(sequence):
    answer = 0
    sequence_f = []
    sequence_s = []
    max_f = 0
    max_s = 0
    
    # 1 -1 1 -1 ..
    for i in range(len(sequence)):
        if i % 2 == 0:
            sequence_f.append(sequence[i])
        else:
            sequence_f.append(-sequence[i])
            
    # -1 1 -1 1 ..
    for i in range(len(sequence)):
        if i % 2 == 0:
            sequence_s.append(-sequence[i])
        else:
            sequence_s.append(sequence[i])     
    
    max_f = max_sum(sequence_f)
    max_s = max_sum(sequence_s)
    
    return max(max_f, max_s)