# 크기가 작은 부분 문자열

t = "3141592"
p = "271"


part_t = []
for i in range(len(t)-len(p)+1):
    part_t.append(int(t[i:i+len(p)]))

answer = 0
for i in part_t:
    if i < int(p):
        answer+=1

print(part_t)
print(answer)