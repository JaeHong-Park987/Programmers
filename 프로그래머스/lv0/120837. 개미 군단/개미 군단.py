def solution(hp):
    g_attack = 5 # 장군개미 공격력
    s_attack = 3 # 병정개미 공격력
    w_attack = 1 # 일개미 공격력
    
    general = hp // g_attack # 장군개미 수
    soldier = (hp-general*g_attack) // s_attack # 병정개미 수
    work = (hp-general*g_attack - soldier * s_attack) // w_attack # 일개미 수
    
    total = general + soldier + work # 총 개미 수
    
    return total