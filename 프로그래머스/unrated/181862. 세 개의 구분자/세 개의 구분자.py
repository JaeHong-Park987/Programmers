def solution(myStr):
    new_str = myStr.replace('a',' ').replace('b',' ').replace('c', ' ')
    
    k = new_str.split()
    
    if len(k) != 0:
        return k
    else:
        return ['EMPTY']