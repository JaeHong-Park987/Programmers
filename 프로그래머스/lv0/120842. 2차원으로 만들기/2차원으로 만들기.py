def solution(num_list, n):
    # answer = [] # 2차원 리스트 선언
    # k = n # n씩 나눌 수 선언
    # for i in range(int(len(num_list) / n)):
    #     answer.append([])
    #     for j in range(n-k, n):
    #         answer[i].append(num_list[j])
    #     n += k
    # return answer
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer