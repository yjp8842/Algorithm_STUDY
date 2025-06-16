def solution(msg):
    answer = []
    dic = {chr(i + 65): i + 1 for i in range(26)}
    idx = 27
    i = 0

    while i < len(msg):
        w = msg[i]
        j = i + 1

        while j <= len(msg) and msg[i:j] in dic:
            w = msg[i:j]
            j += 1

        answer.append(dic[w])

        # 사전에 w + 다음 글자 추가
        if j <= len(msg):
            dic[msg[i:j]] = idx
            idx += 1

        i += len(w)
    
    return answer