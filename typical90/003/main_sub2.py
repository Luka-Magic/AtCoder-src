def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n-1)]

    g = [[] for _ in range(n)]
    for l in li:
        v = l[0]-1
        w = l[1]-1
        g[v].append(w)
        g[w].append(v)

    from collections import deque

    def bfs(s):
        seen = [float('inf')] * n
        seen[s] = 0
        que = deque([s])
        max_ = [s, 0]
        while que:
            a = que.popleft()
            for b in g[a]:
                if seen[b] == float('inf'):
                    que.append(b)
                    seen[b] = seen[a] + 1
                    m = max(max_[1], seen[b])
                    max_ = [b, m]
        return max_

    s, b = bfs(0)
    print(bfs(s)[1] + 1)


if __name__ == '__main__':
    main()
