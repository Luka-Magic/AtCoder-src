from itertools import combinations
n = input()
l = len(n)
ans = -1
for i in range(1, l//2 + 1):
    for p in combinations(list(range(l)), i):
        s = []
        t = []
        for j in range(l):
            if j in p:
                s.append(n[j])
            else:
                t.append(n[j])
        s.sort(reverse=True)
        t.sort(reverse=True)
        ans = max(ans, int(''.join(s)) * int(''.join(t)))
print(ans)