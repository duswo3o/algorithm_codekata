# 둘만의 암호

def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    idx = 0
    pw_alphabet = []
    idx_pw = {}
    for a in alpha:
        if a not in skip:
            pw_alphabet.append(a)
            idx_pw[a] = idx
            idx +=1

    answer = ''
    for i in s:
        find_idx = idx_pw[i] + index
        if find_idx >= len(pw_alphabet):
            find_idx -= len(pw_alphabet)

        answer+=pw_alphabet[find_idx]

    return answer

print(solution("aukks", "wbqd", 5))