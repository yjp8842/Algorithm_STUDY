def solution(s):
    answer = []
    nums = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    value = ""
    
    for i in range(len(s)):
        if s[i] in '0123456789':
            answer.append(s[i])
        else :
            value += s[i]
            if value in nums.keys():
                answer.append(nums[value])
                value = ""
                
    return int("".join(answer))