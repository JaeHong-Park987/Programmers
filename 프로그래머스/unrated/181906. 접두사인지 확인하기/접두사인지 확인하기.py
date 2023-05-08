def solution(my_string, is_prefix):
    # is_prefix가 접두사이면 my_string의 처음부터 is_prefix 길이까지 출력이 is_prefix와 같을 것이다.
    if is_prefix == my_string[:len(is_prefix)]:
        return 1
    else:
        return 0