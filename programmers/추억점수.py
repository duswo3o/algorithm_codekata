# 프로그래머스 추억 점수

def solution(name, yearing, photos):
    # 각 인물에 대한 그리움 점수
    score = {}
    for i,n in enumerate(name):
        score[n] = yearing[i]

    # 사진들의 추억 점수
    answer = []
    for photo in photos:
        s = 0 # 추억점수 총 합
        for p in photo:
            s += score.get(p,0)
        answer.append(s)
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may"],["kein", "deny", "may"], ["kon", "coni"]]))