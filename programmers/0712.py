# 2016년

a, b = 5, 24


year_2016 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31,
             8:31, 9:30, 10:31, 11:30, 12:31}

week_2016 = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

day = 0

for i in range(a):
    day += year_2016[i+1]

print(week_2016[day%7-1])