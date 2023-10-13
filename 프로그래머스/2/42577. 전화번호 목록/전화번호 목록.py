def solution(phone_book):
    answer = True
    
    hashs = {}
    for nums in phone_book:
        hashs[nums] = 1
        
    for nums in phone_book:
        temp = ""
        
        for num in nums:
            temp += num
            # print("num : ", num)
            # print("temp : ", temp)
            # print(hashs)
#           hashs에는 있지만, phone_number와 같지 않을때
#           어떤 번호가 다른 번호의 접두어로 존재한다는 뜻
            if temp in hashs and temp != nums:
                answer = False
    
    return answer