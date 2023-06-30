def solution(a, b):
    num_list = []
    k = 2
    pf_list = []
    
    for i in range(1,a+1):
        if (a % i == 0) & (b % i == 0):
            num_list.append(i)
    gcd = max(num_list) # 최대공약수
    d = int(b / gcd) # 기약분수의 분모
    
    while k <= d:
        if d % k == 0:
            pf_list.append(k)
            d = d / k
        else:
            k += 1
    
    pf_list = list(set(pf_list))
    
    for p in pf_list:
        if p not in [2,5]:
            return 2
    return 1
            
        