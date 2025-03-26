def solution(want, number, discount):
    days = 0
    l_discount = len(discount)
    l_want = len(want)
    s_number = sum(number)
    for i in range(l_discount - s_number + 1):
        flag = 0
        n_dis = discount[i:i + 10]
        for j in range(l_want):
            # print(j, want[j], n_dis.count(want[j]))
            if n_dis.count(want[j]) >= number[j]:
                flag += 1
                
        if flag == l_want:
            days += 1
            
    return days