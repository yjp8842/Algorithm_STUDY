from itertools import permutations

def solution(k, dungeons):
    answer = -1
    arr = [i for i in range(len(dungeons))]
    perm = list(permutations(arr, len(arr)))
    
    max_cnt = 0
    for i in range(len(perm)):
        cnt = 0
        cal_k = k
        for j in range(len(perm[i])):
            # print(dungeons[perm[i][j]][0])
            if cal_k >= dungeons[perm[i][j]][0]:
                cal_k -= dungeons[perm[i][j]][1]
                cnt += 1
        
        if max_cnt < cnt:
            max_cnt = cnt
            # print(max_cnt)
        
    return max_cnt