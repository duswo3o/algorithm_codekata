# 2개 이하로 다른 비트


def transfer_binary(n):
    binary = []
    while n > 0:
        binary.append(n%2)
        n //= 2
    return binary

def trans_bit(binary):
    if len(binary) == sum(binary):
        binary.pop()
        binary += [0, 1]
        return binary

    for idx, b in enumerate(binary):
        if b == 0:
            if idx == 0:
                binary[idx] = 1
                return binary
            else:
                binary[idx] = 1
                binary[idx-1] = 0

def make_decimal(binary):
    decimal = 0
    for idx, b in enumerate(binary):
        decimal += b*(2**idx)

    return decimal

def solution(numbers):
    answer = []
    for n in numbers:
        t_binary = transfer_binary(n)
        t_bit = trans_bit(t_binary)
        answer.append(make_decimal(t_bit))

    return answer


print(solution([2,7]))
