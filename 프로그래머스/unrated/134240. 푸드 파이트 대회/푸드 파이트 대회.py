def solution(food):
    answer = '0'
    for i in range(1,len(food)):
        answer = answer.ljust(len(answer) + food[-i] // 2, str(len(food) - i))
        answer = answer.rjust(len(answer) + food[-i] // 2, str(len(food) - i))
        
    return answer