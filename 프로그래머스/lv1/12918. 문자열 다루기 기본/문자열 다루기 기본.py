def solution(s):
    length = len(s)
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    
    if length == 4 or length == 6:
        for i in s:
            if i not in num_list:
                return False
        return True
    else:
        return False