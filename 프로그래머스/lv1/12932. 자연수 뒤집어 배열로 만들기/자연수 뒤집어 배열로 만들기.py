def solution(n):
    num_list = list(str(n))
    answer = []
    
    for i in range(len(num_list)):
        answer.append(int(num_list[len(num_list)-1-i]))
    return answer