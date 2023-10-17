from itertools import permutations

# 소수 판별하는 함수
def is_prime(n):
    if n < 2:
        return 0
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
        
    return 1

def solution(numbers):
    answer = 0
    num_list = list(map(int, numbers))
    
    perm = []
    # 최대 numbers 길이만큼의 만들 수 있는 순열 만들기
    for i in range(1, len(numbers) + 1) :
        perm.append(list(set(map(''.join, permutations(numbers, i)))))
        
    # 중복되는 숫자를 제외한 리스트 생성
    perm_list = list(set(map(int, set(sum(perm, [])))))
    
    for num in perm_list:
        if is_prime(num):
            answer += 1
    
    return answer