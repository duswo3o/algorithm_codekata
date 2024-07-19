# 개인정보 수집 유효기간


def solution(today, terms, privacies):
    due = {}
    today_y, today_m, today_d = map(int, today.split("."))
    for i in terms :
        t , term = i.split()
        due[t] = int(term)

    result = []
    for i, p in enumerate(privacies):
        date, t = p.split()
        year, month, day = map(int, date.split('.'))
        month += due[t]

        if month > 12:
            month -= 12
            year += 1

        if (year < today_y) or (year == today_y and month < today_m) or (year == today_y and month == today_m and day < today_d):
            result.append(i+1)

    return result

# print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01",["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2022.02.19 C"]))



