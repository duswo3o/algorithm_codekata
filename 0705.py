# 문자열 내 마음대로 정렬하기

strings = ["abce", "abcd", "cdx"]
n = 2

def solution(strings, n):
    new_sort = {} # 각문자열의 인덱스 n번째 글자를 key로 딕셔너리를 만들기 위함

    # 주어진 문자열 리스트를 반복
    for i in strings:
        # 만약 문자열의 n번째 값이 이미 존재하는 key값이라면
        if i[n] in new_sort.keys():
            new_sort[i[n]].append(i) # 같은 key값을 가진 value 리스트에 추가
            new_sort[i[n]].sort() # 사전순으로 정렬
        else: # 문자열의 인덱스 n번째 값이 새로운 key값이면
            new_sort[i[n]] = [i] # 새롭게 key값을 만들어 해당 문자열을 list형태의 value로 저장

    ''' key 값을 사전순으로 정렬한 후 해당 key 값에 대응대는 리스트를 순서대로 출력 
        -> 이중 리스트이므로 단순리스트로 풀어줌(sum() 이용)'''
    return sum([new_sort[i] for i in sorted(new_sort.keys())], [])

print(solution(strings,n))