def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    
    for s1 in s:
        s2 = s1.split(',')
        for s3 in s2:
            if int(s3) not in answer:
                answer.append(int(s3))
                
    return answer