# 2016년

a, b = 5, 24

#
# year_2016 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31,
#              8:31, 9:30, 10:31, 11:30, 12:31}
#
# week_2016 = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
#
# day = 0
#
# for i in range(a):
#     day += year_2016[i+1]
#
# print(week_2016[day%7-1])

def solution(a,b):
    year_2016 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
                 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} # 2016년 달력
    week_2016 = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"] # 2016년의 시작 요일이 금요일
    day = 0 # 1/1일부터 며칠이나 지났는지

    # 현재 달의 이전 달까지 더하기
    for i in range(a-1):
        day += year_2016[i+1]

    return week_2016[(day+b)%7-1]

# print(solution(3,1))