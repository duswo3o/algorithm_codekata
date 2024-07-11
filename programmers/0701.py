# 크기가 작은 부분 문자열

t = "500220839878"
p = "7"


# part_t = []
# for i in range(len(t)-len(p)+1):
#     part_t.append(int(t[i:i+len(p)]))

# answer = 0
# for i in part_t:
#     if i < int(p):
#         answer+=1

# print(part_t)
# print(answer)

def solution(t, p):
    # 길이가 p인 t의 부분 문자열 리스트
    part_t = [int(t[i:i+len(p)]) for i in range(len(t)-len(p)+1)]
    answer = 0

    # 부분문자열이 p보다 작은지 확인
    for i in part_t:
        if i <= int(p):
            answer +=1
    
    return answer