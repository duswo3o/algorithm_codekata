# 문자열 내 마음대로 정렬하기

strings = ["sun", "bed", "car"]
n = 1

new_sort = {}
for i in strings:
    new_sort[i[n]] = i

print(sorted(new_sort.keys()))

answer = [new_sort[i] for i in sorted(new_sort.keys())]
print(answer)