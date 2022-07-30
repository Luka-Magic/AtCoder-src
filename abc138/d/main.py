import sys
sys.setrecursionlimit(10 ** 6)

n, q = map(int, input().split())

li = [list(map(lambda x:int(x) - 1, input().split())) for _ in range(n-1)]
q_li = [list(map(int, input().split())) for _ in range(q)]

rin = [[] for _ in range(n)]

for a, b in li:
    rin[a].append(b)
    rin[b].append(a)

q_li.sort(key=lambda x: x[0])

q = [0] * n
for i, v in q_li:
    i -= 1
    q[i] += v

seen = [-1] * n

def dfs(i, x):
    # i番目のカウンターを検索
    x += q[i]
    seen[i] = x
    for k in rin[i]:
        if seen[k] == -1:
            dfs(k, x)

dfs(0, 0)

print(*seen)