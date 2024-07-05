# 문자열 내 마음대로 정렬하기

strings = ["abce", "abcd", "cdx"]
n = 2

def solution(strings, n):
    new_sort = {}

    for i in strings:
        if i[n] in new_sort.keys():
            new_sort[i[n]].append(i)
            new_sort[i[n]].sort()
        else:    
            new_sort[i[n]] = [i]

    return sum([new_sort[i] for i in sorted(new_sort.keys())], [])

print(solution(strings,n))