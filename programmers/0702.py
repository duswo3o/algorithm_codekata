# 최소직사각형

def solution(sizes):
    width =  [] # 가로길이 리스트
    length = [] # 세로길이 리스트

    for i in sizes:
        width.append(max(i)) # 긴 쪽만 가로 길이에 추가
        length.append(min(i)) # 짧은 쪽만 세로 길이에 추가
    # 가로 리스트와 세로 리스트의 가장 큰 값을 곱해서 리턴
    return max(width) * max(length)