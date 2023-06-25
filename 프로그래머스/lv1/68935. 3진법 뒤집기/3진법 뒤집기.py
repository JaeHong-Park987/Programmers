def solution(n):
    r_num_3 = '' # 3진법(앞뒤 반전)
    answer = 0
    
    while n != 0:
        r = n % 3 # 나머지
        n = n // 3 # 몫
        r_num_3 += str(r)
        
    # for i in range(len(r_num_3)):
    #     answer += (3 ** (len(r_num_3) - 1 - i)) * int(r_num_3[i])
    
    return int(r_num_3, 3)