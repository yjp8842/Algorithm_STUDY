def solution(k, ranges):
    answer = []
    
    n = 0
    lst = []
    lst.append((n, k))
    
    while True:
        if k == 1:
            break
        
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        
        n += 1
        lst.append((n, k))
    
    areas = []
    for i in range(len(lst) - 1):
        y1 = lst[i][1]
        y2 = lst[i + 1][1]
        area = (y1 + y2) / 2
        areas.append(area)

    total_len = len(areas)

    for r in ranges:
        start = r[0]
        end = total_len + r[1]

        if start > end:
            answer.append(-1.0)
        else:
            sum_area = 0
            for i in range(start, end):
                sum_area += areas[i]
            answer.append(sum_area)

    return answer