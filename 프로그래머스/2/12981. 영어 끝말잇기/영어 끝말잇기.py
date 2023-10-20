def solution(n, words):
    answer = []
    
    lists = []
    # for i in range(n):
    #     lists.append(words[i * n:i * n + n])
    
    num = 0
    cnt = 0
    lists.append(words[0])
    for i in range(1, len(words)):
        if words[i] not in lists and words[i - 1][-1] == words[i][0]:
            lists.append(words[i])
        else:
            num = (i % n) + 1
            cnt = (i // n) + 1
            break
    
    return num, cnt