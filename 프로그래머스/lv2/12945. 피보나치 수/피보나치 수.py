def solution(n):
    n1 = 0
    n2 = 1
    i = 0
    
    while i < n-1:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        i += 1
    
    return n3 % 1234567