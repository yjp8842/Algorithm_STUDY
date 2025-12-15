def solution(N, number):
    answer = -1
    dp = [[] for _ in range(10)]
    flag = False
    
    for i in range(1, 9):
        dp[i].append(int((str(N) * i)))
        
        if int((str(N) * i)) == number:
            answer = i
            break
        
        if i != 1:
            for j in range(1, i):
                for num1 in dp[j]:
                    for num2 in dp[i - j]:
                        dp[i].append(num1 + num2)
                        dp[i].append(num1 - num2)
                        dp[i].append(num1 * num2)
                        
                        if num2 > 0:
                            dp[i].append(num1 // num2)
                    
                if number in dp[i]:
                    answer = i
                    flag = True
                    break
                    
        if flag:
            break
        
    return answer