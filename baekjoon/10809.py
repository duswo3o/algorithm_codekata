# 알파벳 찾기

def find_alphabet(s):
    answer = ["-1"]*26

    for i in range(len(s)):
        if answer[ord(s[i])-97]=="-1":
            answer[ord(s[i])-97] = f"{i}"

    return " ".join(answer)

print(find_alphabet('baekjoon'))