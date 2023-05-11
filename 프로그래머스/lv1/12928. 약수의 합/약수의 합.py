def solution(n):
    divisor = [] # 약수를 저장할 리스트
    for i in range(1,n+1):
        if n % i == 0:
            divisor.append(i)
    
    return sum(divisor)