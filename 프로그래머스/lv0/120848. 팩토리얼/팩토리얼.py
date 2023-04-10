def solution(n):
    number = 1
    fac = 1
    
    while True:
        fac *= number
        # print(fac, n, number)
        
        if n == fac: 
            return number
        elif n < fac:
            return number - 1
        number += 1
        
    return number 
        