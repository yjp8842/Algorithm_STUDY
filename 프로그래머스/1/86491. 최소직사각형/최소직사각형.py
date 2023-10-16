def solution(sizes):
    answer = 0
    max_w = []
    max_h = []
    for size in sizes:
        if size[0] >= size[1]:
            max_w.append(size[0])
            max_h.append(size[1])
        else:
            max_w.append(size[1])
            max_h.append(size[0])
    
    answer = max(max_w) * max(max_h)
    return answer