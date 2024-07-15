# 펫


import sys

def pet_condition(proper_weight, now_weight):
    if now_weight <= 0:
        return "RIP"
    elif (now_weight > proper_weight*0.5) and (now_weight < proper_weight*2):
        return ":-)"
    return ":-("

def pet_weight(proper_weight, now_weight):
    while True:
        scenario = input()
        if scenario == '# 0':
            break

        if now_weight > 0:
            scenario = scenario.split()
            if scenario[0] == 'E':
                now_weight -= int(scenario[1])
            elif scenario[0] == 'F':
                now_weight += int(scenario[1])

    return pet_condition(proper_weight, now_weight)

cnt = 0
while True:
    condition = input()
    if condition == '0 0':
        break
    cnt += 1
    proper_weight, now_weight = map(int, condition.split())
    print(f"{cnt}",pet_weight(proper_weight, now_weight))