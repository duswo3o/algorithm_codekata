# 음양 더하기


# def solution(absolute, signs):
#     answer = 0
#     for i in range(len(absolute)):
#         if signs[i] == True:
#             answer += absolute[i]
#         else:
#             answer -= absolute[i]
#     return answer


def solution(absolute, signs):
    return sum([absolute[i] if signs[i]==True else -absolute[i] for i in range(len(absolute)) ])

print(solution([4,7,12],[True,False, True]))
print(solution([1,2,3],[False, False, True]))