# 정렬 순서 : 하위조건 -> 상위조건    
N = int(input())
word_list = []

for i in range(N):
    word_list.append(input())
    
words = list(set(word_list))  # 중복되는 값은 제외

words.sort()           # 하위조건
words.sort(key = len)  # 상위조건

for word in words:
    print(word)