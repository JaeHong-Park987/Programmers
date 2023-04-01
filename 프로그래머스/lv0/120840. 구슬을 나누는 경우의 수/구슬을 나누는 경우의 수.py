# 팩토리얼 함수
def factorial(n):
    f = 1
    for i in range(n,0,-1):
        f *= i
    
    return f

def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    
    return answer