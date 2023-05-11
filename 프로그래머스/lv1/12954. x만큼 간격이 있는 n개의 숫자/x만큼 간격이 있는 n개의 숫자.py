def solution(x, n):
    answer = []
    num = 0
    
    while n != 0:
        num += x
        answer.append(num)
        n -= 1
    
    return answer