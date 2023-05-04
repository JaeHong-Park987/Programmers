def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    
    # if ab > ba:
    #     return ab
    # else:
    #     return ba
    
    # max 함수 활용!!!
    
    return max(ab, ba)
    