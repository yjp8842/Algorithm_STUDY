def solution(n, m):
    answer = []
    n_lst, m_lst = [], []
    gcd, lcm = 0, 0
    
    if n > m:
        n, m = m, n
        
    for i in range(1, n + 1):
        if n % i == 0:
            n_lst.append(i)
    for j in range(1, m + 1):
        if m % j == 0:
            m_lst.append(j)
            
    for num1 in n_lst:
        for num2 in m_lst:
            if num1 == num2:
                gcd = num1
    
    answer.append(gcd)
    
    if m % gcd == 0 and gcd != 1:
        lcm = m * n // gcd
    else:
        lcm = m * n

    answer.append(lcm)
    
    return answer