from collections import deque
import sys
input = sys.stdin.readline

mod = 998244353
inf = float('inf')


def bfs(i, j):
    seen = [[inf] for _ in range(m)]
    que = deque([])
    que.append(i)
    seen[i] = 1
    while que:
        a = que.popleft()
        if a == j:
            
        for t in l[a]:
            if seen[t]:
                continue
            seen[t] = 1
            que.append(t)



n, m, k = map(int, input().split())
li = list(map(int, input().split()))
l = [[] for _ in range(m)]
hen = {}

for _ in range(n-1):
    u, v = map(int, input().split())
    hen[(u-1, v-1)] = 0
    l[u-1].append(v-1)
    l[v-1].append(u-1)

print(hen)
