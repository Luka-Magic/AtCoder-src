import sys
input = sys.stdin.readline


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
        seen = [[] for _ in range(n)]
        seen[s].append(s)
        que = deque([s])
        while que:
            a = que.popleft()
            for b in g[a]:
                if seen[b] != []:
                    continue
                que.append(b)
                seen[b] = seen[a] + [b]
        return seen

    tree = bfs(0)
    l = max(tree, key=len)
    k = l[-1]
    del tree
    tree2 = bfs(k)
    print(len(max(tree2, key=len)))


if __name__ == '__main__':
    main()
