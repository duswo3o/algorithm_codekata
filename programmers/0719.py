# 로또의 최고 순위와 최저 순위


def solution(lottos, win_nums):
    lotto_rank ={0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}

    unknown_lotto = lottos.count(0)
    correct_lotto = len(set(lottos) & set(win_nums))

    return [lotto_rank[unknown_lotto+correct_lotto], lotto_rank[correct_lotto]]


print(solution([44,1,0,0,31,25],[31,10,45,1,6,19]))
print(solution([0,0,0,0,0,0], [38,19,20,40,15,25]))
print(solution([45,4,35,20,3,9], [20,9,3,45,4,35]))