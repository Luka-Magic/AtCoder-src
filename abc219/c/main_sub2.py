x = list(input())
n = int(input())

li = [input() for _ in range(n)]

dic = {}
for i, s in enumerate(x):
    dic[s] = i+1

d = {}
for l in li:
    k = []
    for s in l:
        k.append(dic[s])
    d[l] = k

d = sorted(d.items(), key=lambda x: x[1])

for i in d:
    print(i[0])
