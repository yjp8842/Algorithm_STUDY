def solution(s):
    answer = []
    zero_cnt = 0
    cnt = 0
    
    while True:
        if s == '1':
            break
        
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        cnt += 1
        
        s = str(bin(s.count('1'))[2:])
        answer = [cnt, zero_cnt]
    
    return answer