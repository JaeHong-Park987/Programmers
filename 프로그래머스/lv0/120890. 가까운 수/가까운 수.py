def solution(array, n):
    array.sort()
    dif = []
    for i in array:
        dif.append(abs(i-n))
        
    return array[dif.index(min(dif))]