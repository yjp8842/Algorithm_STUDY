T = int(input())

for tc in range(T):
    N = int(input())
    
    # 0과 1이 호출되는 경우의 수 
    temp_list = [[1, 0], [0, 1]]
    
    if N <= 1:
        print(temp_list[N][0], temp_list[N][1])
        
    else:
        for i in range(2, N + 1):
            # 그 전과 그 전전의 경우의 수를 더한 것
            temp_list[0].append(temp_list[0][i - 1] + temp_list[0][i - 2])
            temp_list[1].append(temp_list[1][i - 1] + temp_list[1][i - 2])
            
        print(temp_list[0][N], temp_list[1][N])