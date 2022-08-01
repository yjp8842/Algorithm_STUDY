import math

def is_prime(num):
    if num == 1:
        return False
    
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    
    return True

is_prime_list = [] # 빈 리스트 선언
nums = list(range(2, 246912)) # 범위를 제한하여 시간 초과 예방
for ns in nums:
    if is_prime(ns):
        is_prime_list.append(ns)
        
while True:
    cnt = 0
    N = int(input())
    if N == 0: # 마지막 입력값 0
        break
    
    for ns in is_prime_list:
        if N < ns < N * 2:
            cnt += 1
            
    print(cnt)