# 최고의 피자 : 1원당 열량이 가장 높은 피자
# k종류의 토핑
# 피자의 가격 = A + B * k
# 토핑의 종류의 수 N
N = int(input())
# 도우의 가격 A, 토핑의 가격 B
A, B = map(int, input().split())
# 도우의 열량
C = int(input())
# 토핑의 열량
D = []
for _ in range(N):
    D.append(int(input()))

# 토핑의 열량을 내림차순으로 정렬한 리스트
r_list = sorted(D, reverse=True)

for i in r_list:
    cal = C + i
    price = A + B
    
    if (cal / price) > (C / A):
        (C / A) == (cal / price)
        
        A += B
        C += i
    
    else:
        break

# 소수점 이하는 버리고 정수 값으로 출력
max_cal = int(C / A)

print(max_cal)