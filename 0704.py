# 숫자 문자열과 영단어

num_dict = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
s = "one4seveneight"

for i in range(10):
    s = s.replace(num_dict[i], f"{i}")

print(s)