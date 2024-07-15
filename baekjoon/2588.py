# 곱셈

def vertical_multiplication(a,b):
    for i in b[::-1]:
        print(a*int(i))
    print(a*int(b))

a = int(input())
b = input()
vertical_multiplication(a,b)