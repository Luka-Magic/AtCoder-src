import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n, x, y = map(int, input().split())
    g = [[] for _ in range(n)]
    for i in range(n):
        a, b = i+1, i-1
        if a < n:
            g[i].append(a)
        if b >= 0:
            g[i].append(b)
    g[x-1].append(y-1)
    g[y-1].append(x-1)
    from collections import deque
    ans = [0] * (n)
    def bfs(s):
        seen = [-1] * n
        seen[s] = 0
        que = deque([s])
        while que:
            t = que.popleft()
            for to in g[t]:
                if seen[to] == -1:
                    c = seen[t] + 1
                    seen[to] = c
                    ans[c] += 1
                    que.append(to)
    for i in range(n):
        bfs(i)
    for a in ans[1:]:
        print(a//2)

if __name__ == '__main__':
    main()
