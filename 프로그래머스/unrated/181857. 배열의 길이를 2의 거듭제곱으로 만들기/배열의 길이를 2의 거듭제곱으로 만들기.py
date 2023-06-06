def solution(arr):
    a = 0
    
    while len(arr) > 2**a:
        a += 1
        
    while len(arr) != 2 ** a:
        arr.append(0)

    return arr
    