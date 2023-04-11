def solution(my_string):
    number = ["0","1","2","3","4","5","6","7","8","9"]
    answer = []
    for string in my_string:
        if string in number:
            answer.append(int(string))
    answer.sort()
    return answer