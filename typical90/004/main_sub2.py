h, w = map(int, input().split())
masu = [list(map(int, input().split())) for _ in range(h)]
h_s = []
w_s = [0] * w
for l in masu:
    h_s.append(sum(l))
for l in masu:
    for i, j in enumerate(l):
        w_s[i] += j
ans = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] = h_s[i] + w_s[j] - masu[i][j]

for a in ans:
    print(*a)