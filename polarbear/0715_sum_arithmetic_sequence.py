# 등차수열의 특정한 항만 더하기

def solution(a,d,included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += a+d*i
    return answer


# def test_solution(a,d,included):
#     return sum([a+d*i for i in range(len(included)) if included[i]==True])

# 숏코딩
test_solution = lambda a,d,included: sum([a+d*i for i in range(len(included)) if included[i]==True])




print(solution(3,4,[True, False, False, True, True]))
print(solution(7,1,[False, False, False, True, False, False, False]))
print(test_solution(3,4,[True, False, False, True, True]))
print(test_solution(7,1,[False, False, False, True, False, False, False]))