def solution(a, b):
    answer = 0
    
    if (a % 2 != 0) & (b % 2 != 0):
        answer = a ** 2 + b ** 2
    elif (a % 2 != 0) | (b % 2 != 0):
        answer = 2 * (a + b)
    else:
        answer = abs(a-b) # 절대값 -> abs 함수 사용
        
    return answer