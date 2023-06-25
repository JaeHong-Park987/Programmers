def solution(id_pw, db):
    if id_pw in db: # db에 아이디 비번이 같은 경우가 있다면
        return "login"
    else: # 없다면
        for d in db:
            if id_pw[0] == d[0]: # 아이디만 같을 때
                return "wrong pw"
        return "fail"