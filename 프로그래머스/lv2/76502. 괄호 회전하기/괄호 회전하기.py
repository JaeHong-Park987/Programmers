def solution(s):
    answer = 0
    
    for i in range(len(s)):
        s = s[1:len(s)+1] + s[0]
        new_s = ''
        
        for j in range(len(s)):
            new_s += s[j]
            if "()" or "{}" or "[]" in new_s:
                new_s = new_s.replace("()","").replace("{}","").replace("[]","")
        
        if len(new_s) == 0:
            answer += 1
        else:
            pass
    
    return answer
                
                