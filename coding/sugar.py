N = int(input())

if N % 5 == 0:
    print(N // 5)
    
else:
    sugar_cnt = 0
    while N > 0:
        N -= 3
        sugar_cnt += 1
        if N % 5 == 0:
            sugar_cnt += N // 5
            print(sugar_cnt)
            break
        elif N == 0:
            print(sugar_cnt)
            break
        else:
            print(-1)
            break
    