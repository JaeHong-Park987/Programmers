def solution(bin1, bin2):
    # int(변수, 2) -> 변수를 이진수로 인식하여 십진수로 변환
    
    a = int(bin1,2)
    b = int(bin2,2)
    
    return bin(a+b)[2:] # bin함수를 활용하여 십진수를 이진수로 변환하고 앞에 '0b'를 제거하기