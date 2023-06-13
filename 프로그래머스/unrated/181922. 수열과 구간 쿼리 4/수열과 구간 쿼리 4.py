def solution(arr, queries):
    for i in range(len(arr)):
        for j in queries:
            if (j[0] <= i <= j[1]) & (i % j[2] == 0):
                arr[i] += 1
                            
    return arr