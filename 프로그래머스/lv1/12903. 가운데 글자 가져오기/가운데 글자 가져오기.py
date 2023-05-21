def solution(s):
    middle_num = int(len(s) / 2) # len(s) // 2로도 가능하다.
    
    if (len(s) % 2) != 0:
        return s[middle_num]
    else:
        return s[middle_num-1:middle_num+1]
        