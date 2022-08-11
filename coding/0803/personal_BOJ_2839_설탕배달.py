N = int(input())

if N % 5 == 0: # 5로 나누어 떨어질 때 
    print(N // 5)
    
else:
    sugar_cnt = 0
    while N > 0:
        N -= 3 # 3kg 만큼씩 뺀다
        sugar_cnt += 1 # 설탕 봉지 개수 +1
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
    