def solution(cipher, code):
    return cipher[code-1::code]

# 리스트 변환할 필요 없음
# [a::b] - a부터 끝까지 b만큼 더한 값 출력 