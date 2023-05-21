def solution(s):
    middle_num = int(len(s) / 2)
    
    if (len(s) % 2) != 0:
        return s[int(middle_num)]
    else:
        return s[middle_num-1:middle_num+1]
        