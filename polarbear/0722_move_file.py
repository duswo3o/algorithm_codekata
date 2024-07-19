# 파일 옮기기

b1_apple, b1_orange = map(int, input().split())
b2_apple, b2_orange = map(int, input().split())

print(min(b1_apple+b2_orange, b1_orange+b2_apple))