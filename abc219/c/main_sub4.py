x = list(input())
n = int(input())
li = [input() for _ in range(n)]

nli = []
for l in li:
    ns = ''
    for s in l:
        for i in range(26):
            if s == x[i]:
                ns += chr(i + ord('a'))
                break
    nli.append([l, ns])
nli.sort(key=lambda x: x[1])
for s, _ in nli:
    print(s)
