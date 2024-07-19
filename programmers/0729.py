# 개인정보 수집 유효기간


def solution(today, terms, privacies):
    due = {} # 약관 종류별 유효 기간
    today_y, today_m, today_d = map(int, today.split(".")) # 오늘의 년, 월, 일
    for i in terms :
        t , term = i.split()
        due[t] = int(term)

    result = [] # 파기할 문서 번호
    for i, p in enumerate(privacies):
        date, t = p.split() # 개인정보 수집일자와 약관
        year, month, day = map(int, date.split('.')) # 개인정보 수집일자의 년, 월, 일
        month += due[t] # 유효기간 더해주기
        day -= 1

        while month > 12: # 월이 12월을 넘어가지 않을 때까지
            month -= 12 # 12월 이상이면 12를 빼주고
            year += 1 # 1년 추가

        if day == 0: # 0일인 경우
            month -= 1 # 한 달 빼고
            day = 28 # 모든 달은 28일까지만 존재
            if month == 0: # 월이 0이 되는 경우
                year -= 1 # 1년 빼기
                month = 12 # 월은 12월

        # 만료일의 년도가 오늘의 년도보다 작거나 / 같은 년도에 월이 작거나 / 같은년도 같은 월에 일이 작은 경우
        if (year < today_y) or (year == today_y and month < today_m) or (year == today_y and month == today_m and day < today_d):
            result.append(i+1) # 파기할 문서에 추가

    return result



print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01",["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2020.10.15", ["A 100"], ["2018.06.16 A", "2008.02.15 A"]))



