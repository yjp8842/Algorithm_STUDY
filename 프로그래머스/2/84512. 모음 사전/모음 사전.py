def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    
    def backtrack(alpha, dict):
        dict.append(alpha)
        for i in vowels:
#           5개가 다 채워지지 않았다면 다시 backtrack 호출
            if len(alpha) != 5:
                backtrack(alpha + i, dict)
#           5개가 다 채워졌다면 4개까지 자르기
            else:
                alpha[:-1]
    
    dict = []
    for i in range(len(vowels)):
        backtrack(vowels[i], dict)
    
    answer = dict.index(word) + 1
    
    return answer