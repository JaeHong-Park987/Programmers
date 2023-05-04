def solution(num_list):
    # minus_list = [] # 음수 리스트
    for i in range(len(num_list)):
        if num_list[i] < 0:
            # minus_list.append(num_list[i])
            return i
    # if len(minus_list) == 0: # 음수 리스트에 아무것도 없다면 -> num_list가 모두 양수
    return -1

# 굳이 새로운 리스트 만들 필요 없음 -> for문이 끝날때까지 return 되는 값이 없다면 for문 밖에서 -1 return 해주면 된다.