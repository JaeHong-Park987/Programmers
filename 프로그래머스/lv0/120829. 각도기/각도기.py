def solution(angle):
    if angle < 90:
        result = 1
    elif angle == 90:
        result = 2
    elif angle < 180:
        result = 3
    else:
        result = 4
    
    return result