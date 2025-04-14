def solution(arr1, arr2):
    n_arr = [len(arr2[0]) * [0] for i in range(len(arr1))]
    
    for i in range (len(n_arr)):
    	for j in range (len(n_arr[i])):
    		for k in range (len(arr1[i])):
    			n_arr[i][j] += arr1[i][k] * arr2[k][j]
                
    return n_arr