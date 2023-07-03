def solution(s):
    new_s = [s[0]]
    
    for i in range(1,len(s)):
        if len(new_s) > 0 and new_s[-1] == s[i]:
            new_s.pop()
        else:
            new_s.append(s[i])

    if len(new_s) == 0:
        return 1
    else:
        return 0