def solution(s):
    answer = []
    dic = dict() 
    # dict로 구현하게 되면 기존 문자를 다른 문자로 대체하지 않고 기존 문자(key) 에 해당하는 value 값만 변경이 가능하다.
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
    return answer