def solution(gems):
    total = len(set(gems))        
    counter = {}                    
    answer = [0, len(gems) - 1]

    left = 0
    for right in range(len(gems)):
        counter[gems[right]] = counter.get(gems[right], 0) + 1

        while len(counter) == total:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]

            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1

    return [answer[0] + 1, answer[1] + 1]