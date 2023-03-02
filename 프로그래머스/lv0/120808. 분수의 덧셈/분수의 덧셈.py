def solution(numer1, denom1, numer2, denom2):
    answer = []
        
    # 분모구하기
    for i in range(max(denom1, denom2), (denom1 * denom2) + 1):
        if (i % denom1 == 0) & (i % denom2 == 0):
            denom = i
            break
    
    # 분자구하기        
    numer = numer1 * (denom // denom1) + numer2 * (denom // denom2)
    
    # 최종 분자 분모의 최대공약수 구하기
    for gcd in range(min(numer, denom), 0, -1):
        if (numer % gcd == 0) & (denom % gcd == 0):
            numer = numer // gcd
            denom = denom // gcd
    
    answer.append(numer)
    answer.append(denom)
    
    
    return answer