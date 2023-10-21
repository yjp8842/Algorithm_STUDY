def solution(s):
    answer = s.split(" ")
    result = []
    for word in answer:
        if word:
            result.append(word[0].upper() + word[1:].lower())
        else:
            result.append(word)
            
    return " ".join(result)
