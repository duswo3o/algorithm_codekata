# 알람 시계

def alarm_clock(hour, minute):
    minute = minute - 45
    if minute < 0:
        minute += 60
        hour -= 1
        if hour < 0:
            hour += 24
    return print(hour, minute)

hour, minute = input().split()
alarm_clock(int(hour), int(minute))