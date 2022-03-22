import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n = int(input())
    li = [tuple(map(int, input().split())) for _ in range(n-1)]
    g = [[] for _ in range(n)]
    for a,b in li:
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    t = len(max(g, key=lambda x:len(x)))
    print(t)

    color = list(range(1, t+1))
    seen = [0] * n
    from collections import deque
    que = deque([[0, 0]])
    ans = dict()
    while que:
        a, c = que.popleft()
        seen[a] = 1
        vs = g[a]
        idx = 0
        for b in vs:
            p, q = min(a, b), max(a, b)
            if seen[b] != 0:
                continue
            if color[idx] == c:
                idx += 1
            que.append([b, color[idx]])
            ans[(p, q)] = color[idx]
            idx += 1
    for l in li:
        a, b = min(l)-1, max(l)-1
        print(ans[(a, b)])


if __name__ == '__main__':
    main()
