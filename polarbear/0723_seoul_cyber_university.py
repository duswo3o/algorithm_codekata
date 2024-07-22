# 서울사이버대학을 다니고

N = int(input()) # 로고송의 길이
logo_song = input() # 영문 번역이 반복, 알파벳 소문자, 띄어쓰기, 쉼표, 마침표

# 띄어쓰기, 쉼표, 마침표 제거해야 함 -> replace 쓰면 시간복잡도 때문에 시간초과 뜨지 않을까...

cnt_logo = {}
for i in logo_song:
    if i.isalpha():
        if cnt_logo.get(i) is None:
            cnt_logo[i] = 1
        else:
            cnt_logo[i] += 1

print(max(cnt_logo.values()))


##############################################################

from collections import Counter

logo_song = logo_song.replace(" ", "")
logo_song = logo_song.replace(",","")
logo_song = logo_song.replace(".","")
logo_song = Counter(logo_song)

print(max(logo_song.values()))