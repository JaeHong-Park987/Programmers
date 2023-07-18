import math

def solution(n):
    count = 0
    for i in range(n+1):
        j = n - i
        if j >= i:
            count += math.comb(j,i)
    
    return count % 1234567
        
        