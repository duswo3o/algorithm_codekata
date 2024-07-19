# 배수와 약수

while True:
    command = input()
    if command == "0 0":
        break

    a, b = map(int, command.split())
    if a < b and b % a == 0:
        print("factor")
    elif a>b and a%b == 0:
        print("multiple")
    else:
        print("neither")