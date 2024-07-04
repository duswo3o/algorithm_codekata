# 숫자 문자열과 영단어

s = "one4seveneight"

def solution(s):
    # 숫자 사전에서 문자열에 해당 값이 있으면 repalace 할 것임!
    num_dict = ["zero", "one", "two", "three", "four",
                "five", "six", "seven", "eight", "nine"]
    # 0부터 9까지 반복
    for i in range(10):
        # 해당하는 문자가 있으면 문자의 인덱스로 치환
        s = s.replace(num_dict[i], f"{i}")
    return int(s) # 정수값으로 반환

print(solution(s))