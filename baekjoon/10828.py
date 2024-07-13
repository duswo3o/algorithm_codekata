# 괄호

def is_vps(s):
    l = []
    for i in range(len(s)):
        if s[i] == '(':
            l.append(s[i])
            continue

        if len(l) == 0:
            return "NO"
        else:
            l.pop()
    if len(l) != 0:
        return "NO"
    return "YES"

# print(is_vps("(())())"))
# print(is_vps("(((()())()"))
# print(is_vps("(()())((()))"))
# print(is_vps("((()()(()))(((())))()"))
# print(is_vps("()()()()(()()())()"))
# print(is_vps("(()((())()("))
#
#
# repeat = input()
# for r in range(int(repeat)):
#     print(is_vps(input()))