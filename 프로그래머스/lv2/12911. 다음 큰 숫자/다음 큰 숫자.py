def solution(n):
    count1 = bin(n)[2:].count("1")
    count2 = 0
    
    while count1 != count2:
        n+=1
        count2 = bin(n)[2:].count("1")
    
    return n