def solution(k, tangerine):
    answer = 0
    t_map = {}
#   각 크기의 귤이 몇 개씩 있는지 담아주기
    for i in tangerine:
        if i in t_map:
            t_map[i] += 1
        else:
            t_map[i] = 1
    
#   개수가 많은 크기의 귤부터 제거해주기 위해 내림차순 정렬
    sort_list = sorted(t_map.items(), key=lambda x:x[1], reverse=True)
    
    types = 0
    for i in range(len(sort_list)):
        k -= sort_list[i][1]
        types += 1
        if k <= 0:
            return types
    