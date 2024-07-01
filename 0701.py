# 크기가 작은 부분 문자열

t = "500220839878"
p = "7"


part_t = []
for i in range(len(t)-len(p)+1):
    part_t.append(int(t[i:i+len(p)]))

answer = 0
for i in part_t:
    if i < int(p):
        answer+=1

# print(part_t)
# print(answer)

def solution(t, p):
    part_t = [int(t[i:i+len(p)]) for i in range(len(t)-len(p)+1)]
    answer = 0
    for i in part_t:
        if i <= int(p):
            answer +=1
    print(part_t)
    return answer