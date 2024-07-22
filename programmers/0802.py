# 최댓값과 최솟값

def solution(s):
    s = list(map(int, s.split(" "))) # 공백으로 분리하여 리스트 만들기
    return f'{min(s)} {max(s)}' # 최소값과 최대값

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
