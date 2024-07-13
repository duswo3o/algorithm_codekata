# 단어공부

def find_most_used_alphabet(s):
    s = [i.upper() for i in s]
    word = set(s)
    freq = {}
    for w in word:
        f = s.count(w)
        if f in freq:
            freq[f].append(w)
        else:
            freq[f] = [w]
    return freq[max(freq.keys())].pop() if len(freq[max(freq.keys())]) == 1 else "?"


print(find_most_used_alphabet("Mississipi"))
print(find_most_used_alphabet("zZa"))
print(find_most_used_alphabet("z"))
print(find_most_used_alphabet("baaa"))