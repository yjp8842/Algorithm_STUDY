import sys
sys.stdin = open('sample_input.txt', 'r')

def len(a_list) :
	cnt = 0
	for _ in a_list :
		cnt += 1
	return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0
    price = 0

    for i in range(len(num_list) - 1):
        result = 0
        while num_list[i] < num_list[i + 1]:
            price += num_list[i]
            cnt += 1
            break

        result = (num_list[i + 1] * cnt) - price
        

    print("#{} {}".format(tc, result))