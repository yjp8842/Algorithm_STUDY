import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 10 + 1):
    N = int(input())
    arr = input()
    # 수식 담을 리스트
    arr_l = []
    # 숫자 담을 리스트
    arr_n = []
    for i in arr:
        if i == '*':
            arr_l.append(i)
        elif i == '+':
            arr_l.append(i)
        else:
            arr_n.append(int(i))
            
    result = 0
    num = 1
    
    for i in range(int(N / 2)):
        if i != int(N / 2) - 1:
            if arr_l[i] == '+':
                if num != 1:
                    num *= arr_n[i]
                    result += num
                    num = 1
                    
                else:
                    result += arr_n[i]
                    
            else:
                num *= arr_n[i]
                
        else:
            if arr_l[i] == '+':
                if num != 1:
                    num *= arr_n[i]
                    result += num

                else:
                    result += arr_n[i]
                    
                result += arr_n[i + 1]
                
            else:
                num *= arr_n[i] * arr_n[i + 1]
                result += num
    
    print("#{} {}".format(tc, result))