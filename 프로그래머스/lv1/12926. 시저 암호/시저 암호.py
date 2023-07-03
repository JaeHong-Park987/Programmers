def solution(s, n):
    s_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    c_list = []
    answer = ''
    
    for i in s_list:
        c_list.append(i.upper())
        
    for i in s:
        if i.isupper():
            if c_list.index(i) + n > 25:
                answer += c_list[c_list.index(i) + n - 26]
            else:
                answer += c_list[c_list.index(i) + n]
                
        elif i.islower():
            if s_list.index(i) + n > 25:
                answer += s_list[s_list.index(i) + n - 26]
            else:
                answer += s_list[s_list.index(i) + n]
        else:
            answer += i
    return answer