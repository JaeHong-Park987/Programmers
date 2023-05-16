def solution(x):
    total = 0 # 자릿수의 합 변수 선언
    digit = str(x)
    
    for i in digit:
        total += int(i)
        
    return x % total == 0