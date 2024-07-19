# 알람 시계

def alarm_clock(hour, minute):
    minute = minute - 45 # 분
    if minute < 0: # 분이 마이너스 인 경우
        minute += 60 # 분을 양수값으로 변환
        hour -= 1 # -1시간
        if hour < 0: # 시간이 음수인 경우
            hour += 24 # 24를 더해줌
    return print(hour, minute)

hour, minute = input().split()
alarm_clock(int(hour), int(minute))