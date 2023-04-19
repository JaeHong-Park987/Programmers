def solution(sides):
    sides.sort() # 오름차순으로 정렬
    
    if sides[-1] < sides[0] + sides[1]: # 가장 긴 변이 다른 두 변의 합보다 작다면
        answer = 1
    else:
        answer = 2

    return answer