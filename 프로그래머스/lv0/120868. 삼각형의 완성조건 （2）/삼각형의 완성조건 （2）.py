def solution(sides):
    answer = 0
    for i in range(max(sides)-min(sides) + 1,sum(sides)):
        answer += 1
        
    return answer