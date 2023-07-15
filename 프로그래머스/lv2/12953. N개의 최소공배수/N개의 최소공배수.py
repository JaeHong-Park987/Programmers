def solution(arr):
    i = 1
    
    while True:
        r = 0
        num = arr[-1] * i
        for j in range(len(arr)-1):
            r += num % arr[j]
        i += 1
        if r == 0:
            return num