# 주차 요금 계산

import math

# 출차할 때 주차한 시간 계산하기
def out(using, out):
    hh, mm = map(int, out.split(":"))
    hh, mm = 23-hh, 59-mm

    using -= (hh*60+mm)
    return using

def solution(fees, records):

    # 주차 시간 계산 계산하기
    parking_time = {}
    for r in records:
        r = r.split()
        if r[-1] == "IN":
            # 이전에 들어온 기록이 없는 경우
            if parking_time.get(int(r[1])) is None:
                h, m = map(int, r[0].split(":"))
                h, m = 23-h, 59-m
                parking_time[int(r[1])] = h*60+m
            # 재입장 하는 경우(in, out, in, ...)
            else:
                h, m = map(int, r[0].split(":"))
                h, m = 23 - h, 59 - m
                parking_time[int(r[1])] += h*60+m
        # 출차
        else:
            parking_time[int(r[1])] = out(parking_time[int(r[1])], r[0])

    # 차량 번호 오름차순 정렬
    car_numbers = list(parking_time.keys())
    car_numbers.sort()

    # 주차 요금 계산하기
    answer = []
    for car_num in car_numbers:
        p_time = parking_time[car_num] # 주차 시간 : 분
        if p_time-fees[0] <= 0:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((p_time-fees[0])/fees[2])*fees[3])
    return answer



print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN",
                "06:00 0000 IN",
                "06:34 0000 OUT",
                "07:59 5961 OUT",
                "07:59 0148 IN",
                "18:59 0000 IN",
                "19:09 0148 OUT",
                "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],  # [0,591]
               ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"])) # [14841]