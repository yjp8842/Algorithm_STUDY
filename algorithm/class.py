dct = {'0':'0000', '1':'0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E':'1110', 'F': '1111'}
T = int(input())
for tc in range(1, T + 1):
    st = input()
    lst = []
    for ch in st:
        lst += dct[ch]
 
    ans = []
    n = 0
    for i in range(len(lst)):
        n = int(lst[i]) + n * 2
        if (i % 7) == 6 or i == len(lst) - 1:
            ans.append(n)
            n = 0
 
    print("#{}".format(tc), *ans)