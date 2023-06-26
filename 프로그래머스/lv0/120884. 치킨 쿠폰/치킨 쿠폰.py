def solution(chicken):
    coupon = chicken
    r = 0
    answer = 0
    
    while coupon >= 10:
        answer += coupon // 10
        coupon = coupon // 10 + coupon % 10
    
    return answer