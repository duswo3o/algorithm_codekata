# 둘만의 암호

def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz" # ascii_lowercase
    idx = 0 # 암호 문자의 인덱스
    pw_alphabet = [] # 암호 문자
    idx_pw = {} # 암호 문자와 인덱스로 이후어진 딕셔너리
    for a in alpha: # 앒파벳을 돌면서
        if a not in skip: # 스킵해야 할 문자가 아니면
            pw_alphabet.append(a) # 암호 문자에 추가
            idx_pw[a] = idx # 딕셔너리 추가
            idx +=1 # 인덱스 증가

    answer = ''
    for i in s: # 변환해야 할 문자에서
        find_idx = idx_pw[i] + index # 문자를 인덱스만큼 밀고
        while find_idx >= len(pw_alphabet): # 인덱스가 암호의 길이보다 작아질때까지 반복
            find_idx -= len(pw_alphabet)

        answer+=pw_alphabet[find_idx] # 엄호 문자 만들기

    return answer

print(solution("aukks", "wbqd", 5))