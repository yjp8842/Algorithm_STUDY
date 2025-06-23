#1 1 11 21 41 111 121 141
#2 2 12 22 42 112 122 142
#3 4 14 24 44 114 124 144

def solution(n):
    answer = ''
    
    while True:
        # print(n)
        if n <= 0:
            break

        if n % 3 == 0:
            answer += str(4)
            n = n // 3 - 1
        else:
            answer += str(n % 3)
            n = n // 3
            
    return answer[::-1]