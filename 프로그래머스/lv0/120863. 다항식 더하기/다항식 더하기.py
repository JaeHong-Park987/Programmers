def solution(polynomial):
    list = polynomial.split('+') # 다항식 분리
    x = 0 # 일차항 계수
    num = 0 # 상수항
    for i in list:
        i = i.strip() # 공백 제거
        # 그냥 x라면 일차항 계수 +1
        if i == 'x':
            x += 1
        # 일차항 계수가 1인 아닌 경우에는 x에 계수만큼 더해주기
        elif 'x' in i:
            x += int(i[:-1])
        # 상수항일 때 상수항에 그 숫자만큼 더해주기
        else:
            num += int(i)
    # 상수항이 없다면
    if num == 0:
        answer = '{}x'.format(x)
        # 일차항 계수도 1이라면
        if x == 1:
            answer = 'x'
    # 일차항이 없다면
    elif x == 0:
        answer = '{}'.format(num)
    else:
        answer = '{}x + {}'.format(x,num)
        # 일차항 계수도 1이라면
        if x == 1:
            answer = 'x + {}'.format(num)

    return answer