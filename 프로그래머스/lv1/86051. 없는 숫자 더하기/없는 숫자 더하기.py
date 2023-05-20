def solution(numbers):
    total = 0+1+2+3+4+5+6+7+8+9
    
    for i in numbers:
        total -= i
        
    return total