def solution(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    
    return b % 1234567
        
# math에 내장된 조합 함수를 사용해서 푸는 것 보다 훨씬 효율적이다. 문제가 피보나치 형태로 간다는 것을 발견하는게 어려울뿐...