def solution(a, b, n):
    answer = 0
    
    while n // a >= 1:
        r = n % a
        n = (n // a) * b
        answer += n
        n += r
    
    return answer