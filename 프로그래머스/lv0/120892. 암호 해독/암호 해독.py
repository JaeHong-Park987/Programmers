def solution(cipher, code):
    cipher = list(cipher) # 암호화된 문자열을 리스트로 변환
    real_code = '' # 실제 코드 변수 선언
    
    for i in range(1, len(cipher) + 1):
        if i % code == 0:
            real_code += cipher[i-1]
            
    return real_code