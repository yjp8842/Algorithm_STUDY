import math

def is_prime(num): # 소수 구하는 함수
    if num == 1:
        return True
    else:
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
    
    for value in is_prime_list:
        if N < value <= N * 2: # 주어진 범위 안에 있는 소수 카운트
            cnt += 1
            
    print(cnt)