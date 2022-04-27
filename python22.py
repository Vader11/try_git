freq = {}

value = input("input:")
value = value.split(' ')
for i in value:
    freq[i] = freq.get(i, 0) + 1
word = sorted(freq.keys())

for w in word:
    print(f"{w}:{freq[w]}")
