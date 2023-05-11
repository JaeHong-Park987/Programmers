def solution(arr):
    total = 0
    
    for i in arr:
        total += i
        
    answer = total / len(arr)
    return answer