C, R = map(int, input().split())
seat_list = [[0] * (C + 1) for _ in range(R + 1)]
K = int(input())
direction = 0
num = 1
x = y = 0

if K > C * R:
    print(0)
    
else:
    # 가장 겉에 부분에서 꺾어야 하는 부분에 0이 아닌 숫자를 넣어줌
    seat_list[0][0] = 1
    seat_list[R][0] = 1
    seat_list[R - 1][C] = 1
    seat_list[-1][C - 1] = 1
        
    while True:
        if num < K:
            
            # 방향 : 위
            if direction == 0:
                if seat_list[x + 1][y] == 0:
                    x += 1
                    num += 1
                    seat_list[x][y] = num
                else:
                    direction += 1
            
            # 방향 : 오른쪽        
            elif direction == 1:
                if seat_list[x][y + 1] == 0:
                    y += 1
                    num += 1
                    seat_list[x][y] = num
                else:
                    direction += 1
            
            # 방향 : 아래        
            elif direction == 2:
                if seat_list[x - 1][y] == 0:
                    x -= 1
                    num += 1
                    seat_list[x][y] = num
                else:
                    direction += 1
            
            # 방향 : 왼쪽        
            else:
                if seat_list[x][y - 1] == 0:
                    y -= 1
                    num += 1
                    seat_list[x][y] = num
                else:
                    direction = 0
                    
        if num == K:
            break
                    
    print(y + 1, x + 1)