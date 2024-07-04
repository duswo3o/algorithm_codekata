# 숫자 문자열과 영단어

s = "one4seveneight"

def solution(s):
    num_dict = ["zero", "one", "two", "three", "four",
                "five", "six", "seven", "eight", "nine"]
    
    for i in range(10):
        s = s.replace(num_dict[i], f"{i}")
    return int(s)

print(solution(s))