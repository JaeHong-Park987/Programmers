def solution(s):
    s = s.split() # s를 공백별로 나누어 리스트로 변환
    answer = 0 
    for i in range(0, len(s)):
        if s[i] != 'Z': # 숫자이면 우선 더하고
            answer += int(s[i])
        else: # 숫자가 아니면(Z이면) Z 앞에 숫자 빼기
            answer -= int(s[i-1])
    
    return answer